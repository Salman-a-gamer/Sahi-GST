"""Best-effort labelled-text extraction after browser OCR. Unknown stays null."""
import re
from .rules import FIELDS

def parse_text(text):
    text = re.sub(r'^\s*Stated round[ -]?off', 'Round-off', text, flags=re.I | re.M)
    text = re.sub(r'^\s*Goods description', 'Description', text, flags=re.I | re.M)
    result = {k: None for k in FIELDS}
    labels = {'supplier_name': r'(?:supplier|seller)(?:\s+name)?', 'supplier_gstin': r'(?:supplier|seller)\s+gstin', 'buyer_name': r'(?:buyer|recipient)(?:\s+name)?', 'buyer_gstin': r'(?:buyer|recipient)\s+gstin', 'invoice_number': r'invoice\s*(?:number|no\.?|#)', 'invoice_date': r'(?:invoice\s*)?date', 'description': r'(?:description|goods)', 'place_of_supply': r'place\s+of\s+supply', 'taxable_value': r'(?:taxable\s*(?:value|amount)|subtotal)', 'cgst': r'cgst(?:\s+amount)?', 'sgst': r'sgst(?:\s+amount)?', 'igst': r'igst(?:\s+amount)?', 'tax_rate': r'(?:gst|tax)\s+rate', 'total': r'(?:grand\s+total|invoice\s+total|total\s+amount)', 'round_off': r'round[ -]?off'}
    for key, label in labels.items():
        match = re.search(r'^\s*' + label + r'\s*[:=]\s*(.+?)\s*$', text, re.I | re.M)
        if match:
            value = match.group(1).strip()
            if key in ['taxable_value', 'cgst', 'sgst', 'igst', 'tax_rate', 'total', 'round_off']:
                m = re.search(r'-?[\d,]+(?:\.\d+)?', value)
                value = m.group(0).replace(',', '') if m else None
            result[key] = value
    return result
