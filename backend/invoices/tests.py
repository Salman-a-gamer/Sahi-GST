from django.test import TestCase, Client
from .rules import validate, correction_draft
from .parser import parse_text

def sample():
    return {'supplier_name': 'Demo Supplies', 'supplier_gstin': '27ABCDE1234F1Z5', 'buyer_name': 'Demo Buyer', 'buyer_gstin': '27PQRST5678L1Z2', 'invoice_number': 'DEMO/001', 'invoice_date': '2026-10-09', 'description': 'Synthetic goods', 'taxable_value': '10000', 'cgst': '900', 'sgst': '900', 'igst': '0', 'tax_rate': '18', 'total': '12800', 'round_off': '0'}

class RuleTests(TestCase):
    def test_difference(self):
        r = validate(sample())
        f = next(x for x in r['findings'] if x['rule_id'] == 'M04')
        self.assertEqual(f['expected'], '11800.00')
        self.assertEqual(f['status'], 'issue')
        self.assertIn('not changed', correction_draft(r['fields'], r))

    def test_clean_and_decimal(self):
        data = sample() | {'taxable_value': '0.10', 'cgst': '0', 'sgst': '0', 'igst': '0', 'tax_rate': '0', 'total': '0.10'}
        self.assertEqual(validate(data)['counts']['issue'], 0)

    def test_unknown_not_zero(self):
        r = validate(sample() | {'igst': None})
        self.assertEqual(next(x['status'] for x in r['findings'] if x['rule_id'] == 'M04'), 'not_checked')

    def test_nonfinite_and_negative(self):
        for bad in ['NaN', 'Infinity', '-10']:
            r = validate(sample() | {'taxable_value': bad})
            self.assertEqual(next(x['status'] for x in r['findings'] if x['rule_id'] == 'M04'), 'not_checked')

    def test_invalid_shapes(self):
        with self.assertRaises(ValueError): validate({'total': {'nested': 1}})

    def test_parse_no_hallucination(self):
        p = parse_text('Supplier: Demo\nGrand total: 12,800.00\nCGST: 900\n')
        self.assertEqual(p['total'], '12800.00')
        self.assertIsNone(p['buyer_gstin'])

class ApiTests(TestCase):
    def test_session_isolation_and_draft(self):
        a, b = Client(), Client()
        a.get('/api/session/')
        response = a.post('/api/reviews/', data={'fields': sample(), 'source': 'manual', 'scope_confirmed': True}, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        ident = response.json()['id']
        self.assertEqual(a.get('/api/reviews/').json()['reviews'][0]['id'], ident)
        self.assertEqual(b.get(f'/api/reviews/{ident}/').status_code, 404)
        self.assertEqual(b.delete(f'/api/reviews/{ident}/').status_code, 404)
        self.assertIn('corrected document', a.get(f'/api/reviews/{ident}/').json()['draft'])

    def test_scope_required(self):
        self.assertEqual(Client().post('/api/reviews/', data={'fields': sample()}, content_type='application/json').status_code, 400)

    def test_csrf_enforced(self):
        self.assertEqual(Client(enforce_csrf_checks=True).post('/api/reviews/', data={}, content_type='application/json').status_code, 403)

    def test_bad_json(self):
        self.assertEqual(Client().post('/api/parse/', data='[]', content_type='application/json').status_code, 400)
