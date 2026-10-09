# Product strategy and problem definition

## Recommendation

Build **a lightweight invoice review and correction assistant for GST-registered small-business buyers**, starting with ordinary domestic goods purchases. Own the moment an invoice arrives, before the owner hands it to a bookkeeper or spends days requesting clarification.

This is a product hypothesis, not validated demand. Choose an accessible local trading business, interview the owner/bookkeeper, and narrow further if its real workflow differs.

## What is the actual problem?

An invoice can look professional while containing a missing recipient GSTIN, inconsistent tax amounts, or a mismatch against the buyer's records. A small business needs to answer three practical questions:

1. What exactly is wrong or uncertain?
2. What evidence supports that finding?
3. What should I ask the supplier to do next?

Tax expertise, document quality and fragmented handoffs make those answers harder than a generic “valid/invalid” badge suggests. The hypothesised cost is re-entry time, clarification messages and delayed resolution. Tax-credit timing may be affected, but an invoice-only check cannot calculate guaranteed credit or savings. GST's own GSTR-2B guidance says eligibility requires assessment beyond appearing in that statement. [GST portal FAQ](https://tutorial.gst.gov.in/userguide/returns/FAQ_gstr2b.htm)

### Who faces what?

| Person | Job and pain hypothesis | Our decision |
|---|---|---|
| Ordinary consumer | Understand a charge and whether the bill is credible | Different product; no ITC promise; later consumer mode only if researched |
| GST-registered small-business buyer | Check incoming supplier documents and request corrections | Primary MVP user |
| Small seller | Produce a correct invoice before sharing | Adjacent later workflow; many billing tools already help |
| Bookkeeper/CA | Review many documents, reconcile and chase exceptions | Interview partner and potential distribution channel; bulk workspace later |
| Large enterprise | Integrate ERP, tax filings, audit and reconciliation | Incumbent strength; outside the initial target |

### Root causes and what can actually be removed

| Root cause | Our intervention | Remaining dependency |
|---|---|---|
| Re-entry across photos, email, spreadsheets and accounting software | Extract once; show source beside fields | OCR still needs human review |
| Checks occur after handoff | Give immediate feedback on receipt | Customer must use the tool early |
| Findings lack a clear action | Produce field-specific correction request | Supplier must act |
| Tax decisions depend on context | Ask for context; abstain when missing | Complex classification and eligibility need broader review |
| Separate invoice and GST reporting systems | Later compare user-provided exports | Supplier filing, portal timing and access cannot be controlled |

We can reduce avoidable delay and ambiguity. We cannot eliminate GST complexity, supplier behaviour or filing dependencies. Long-term prevention means putting validated structured data into the seller's invoicing flow; that is an integration roadmap, not this weekend's build.

## Why this focus beats a broad “average Indian” app

“Every Indian” gives weak customer acquisition, weak willingness-to-pay assumptions and incompatible workflows. A regular GST-registered goods trader has repeated invoices, an identifiable correction workflow and someone who can judge whether our output is useful. Exclude composition/exempt-supply workflows from the first version; do not imply all small shops issue ordinary GST tax invoices.

The stronger value proposition is **fewer avoidable invoice follow-ups with clear evidence**. “Never lose tax credit” is unprovable here. “Detect invoice fraud” is unsupported by arithmetic and format checks.

## Existing products: what is and is not original

These are incumbent product benchmarks, not verified winners of this hackathon. No past winning entry or hackathon identity was supplied.

| Benchmark | What official product material establishes | Our proposed difference | Honest limitation |
|---|---|---|---|
| Clear GST | AI reconciliation, filing workflows and vendor communication | A focused, document-first review and correction experience for a small owner | AI plus follow-up is already offered; no novelty claim on those features |
| Zoho Books India | Accounting-linked GST configuration, filing and GSTR-2B reconciliation | Quick review of an incoming document without moving accounting systems | Integration and ongoing bookkeeping are stronger reasons to choose Zoho |
| TallyPrime IMS | Reconciliation and invoice actions in an accounting workflow | Accessible intake and understandable evidence before bookkeeping handoff | Installed accounting workflows may be faster for existing users |
| Manual review by owner/bookkeeper | Existing practical alternative to validate in interviews | Less transcription and more consistent exception presentation | A skilled reviewer may handle low volumes well without another app |

Sources: [Clear](https://cleartax.in/gst), [Zoho](https://www.zoho.com/in/books/help/gst/), [Tally](https://tallysolutions.com/gst/gst-invoice-reconciliation-tallyprime-ims/). Competitor absence of an equivalent lightweight flow has not been established by hands-on testing. Do not pitch “nobody else does this.”

### Difference in elevator framing

- Broad accounting platform framing, paraphrased: manage accounting, reconciliation and GST workflows together.
- Original problem statement: “Check invoices and GST data for missing fields and mismatches.” Accurate, but describes a feature category.
- Our framing: **“Send the supplier the right correction request while the invoice is still in front of you.”** The check is the means; resolution is the outcome.

## Side-by-side evaluation requested

“Winning project” below means a strong project under this rubric, not a claim about an actual winner.

| Dimension | What a winning project does right | How the initial idea compares | Leverage tactic to adopt | Blind spot to address |
|---|---|---|---|---|
| Strategic framing | Picks one person, one painful moment and one measurable result | “GST data validation for everyone” is too broad | Focus on a registered small-business buyer reviewing supplier invoices on receipt | An extra upload step may be unwanted; validate actual frequency and workflow |
| Value proposition clarity | Shows what the user can do immediately after using it | “AI validator” explains technology but not resolution | Demo a finding becoming an evidence-backed supplier request | Sending a request is not resolving the invoice; measure follow-through separately |
| Innovation edge | Makes a distinctive behaviour visible and reliable | OCR, rules, reconciliation and follow-up already exist | Show source evidence, missing-context abstention and the correct next action in one screen | This is a workflow advantage, not a defensible technical moat yet |
| Market relevance | Names buyer, payer, channel and economic benefit | India's GST relevance is clear; willingness to pay is untested | Start with one local trader and bookkeeper, then CA referrals | Incumbent bundles, free alternatives and review support costs may overwhelm pricing |
| Execution realism | Has a working narrow flow and a credible fallback | All-platform apps, multilingual AI and live reconciliation exceed a weekend | Deliver responsive Next.js + Django image-to-correction loop, then polish | AI extraction, deployment and authentication can each break the demo; test early |

## VC assessment

Promising hackathon scope; an unproven standalone business. A thin invoice checker is easy to copy. Investability would come later from repeated use, distribution through trusted bookkeepers, measured resolution improvements and integration into purchase workflows. Do not call user data a moat without consent, lawful use and real learning benefit.

First payer hypothesis: bookkeeper or small business with enough recurring invoices to value review time. Acquisition hypothesis: CA/bookkeeper referrals and direct onboarding in one local trade cluster. Ask for a follow-up trial or paid pilot rather than treating compliments as demand.

Pricing experiments, not market facts: a small monthly invoice allowance, then a capped business plan; later per-client bookkeeper workspaces. Do not implement billing this weekend. Calculate contribution margin as revenue minus extraction/retry cost, hosting, support and payment fees. Benchmark actual model cost per page before setting any unlimited plan.

Market sizing should be bottom-up: reachable businesses × observed invoice volume × measured adoption × tested price. Total Indian MSMEs are not an addressable paying market estimate. No market-size statistic has been invented for the pitch.

## Fast user validation: 45–60 minutes

Speak with two owners and one bookkeeper if available. Do not lead with “would you like AI?” Ask:

1. Show the last invoice that required a correction. What happened next?
2. Who first noticed it, and how long after receipt?
3. What software or spreadsheet already checked it?
4. How many documents do you personally review in a normal week?
5. Which errors waste the most time? Which require professional judgment?
6. Would you upload a document here, and what would prevent that?
7. Is this proposed correction message actionable and accurate?
8. Would you test five more invoices next week? Who would approve payment?

Use consented/redacted examples; do not put real customer invoices in Git or public demos. Record interview evidence, contradictions and dates. If users already solve this effortlessly, narrow to messy external documents or reconsider the segment. No interviews completed yet.

## Evaluation of the attached AI proposal

| Proposal | Decision and reason |
|---|---|
| AI reads, rules decide | Keep; add human confirmation and unsupported-state handling |
| Small sellers below the e-invoice threshold have no automatic checks | Reject as a blanket statement: billing products can validate regardless of mandate |
| E-invoice threshold determines our market | Avoid; eligibility has historical-turnover and exemption details, and is not willingness to pay |
| One wrong digit means credit is lost | Replace with possible correction and reconciliation difficulty; no guaranteed loss inference |
| Fifteen rules before a live flow | Shrink to a useful, tested subset; add conditional rules only with verified applicability |
| Infer tax type from buyer/seller state | Reject simplification; place of supply and exceptions matter |
| “PAN inside GSTIN” validates identity | Only structural consistency unless independently verified; not separate proof of authenticity |
| One-tap fix makes the invoice clean | Replace with extraction correction versus supplier correction; preserve original |
| Any photo/PDF | Narrow supported formats and quality; abstain on unreadable input |
| FastAPI | Reject; Django is locked by the team |
| Full reconciliation in the first demo | Defer until the core loop passes; no fake GSTN integration |
| Hindi/Telugu | One reviewer-verified language as stretch, chosen by actual users |
| PWA | Keep as enhancement; browser support differs, so test target devices |
| Three-second scan and accuracy claim | Use only measured results; no invented performance |
| Store nothing by default | Turn into an implemented retention policy; external AI processing still matters |
| Rules in configuration | Version sources, applicability and code tests; configuration alone cannot model all tax logic |

## Three-point upgrade summary

1. Reframe from **GST validator** to **a clear path from invoice doubt to supplier correction**.
2. Replace “everyone” with **GST-registered small-business buyers receiving ordinary supplier invoices**.
3. Make **evidence, honest uncertainty and a working resolution loop** the visible innovation; earn speed and accuracy claims through tests.
