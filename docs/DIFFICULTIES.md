# Difficulties, decisions and outcomes

Record actual events. Status values: resolved in planning, verified fixed, open, or anticipated risk. A design mitigation is not a verified code fix.

| Date IST | Difficulty encountered | Action and reason | Evidence / outcome | Status |
|---|---|---|---|---|
| 2026-10-09 | Problem statement spans consumers, sellers and buyers | Recommended registered small-business buyer and ordinary domestic goods invoices | STRATEGY.md; segment still awaits user interviews | Resolved in planning |
| 2026-10-09 | Attached proposal assumes unserved sub-threshold market and unique AI/follow-up | Checked incumbent primary pages; removed blanket novelty claims | Clear and Zoho sources in RESEARCH.md | Resolved in planning |
| 2026-10-09 | Proposal used FastAPI contrary to team stack | Locked Django with Next.js, PostgreSQL and Allauth | MVP_SPEC.md | Resolved in planning |
| 2026-10-09 | One-tap “fix” could misrepresent supplier document correction | Separated transcription edits, correction requests and revised-document checks | MVP_SPEC.md workflow and statuses | Resolved in planning |
| 2026-10-09 | Some government pages failed direct retrieval | Retained indexed official evidence, recorded access limits and deferred unverified applicability assertions | RESEARCH.md; no full current-law verification claimed | Open |
| 2026-10-09 | Deadline and effort initially unknown | Asked early; initial deadline was Sunday evening, later corrected by the user | Superseded by Sunday 11 October 09:00 IST; conservative combined-hour budget | Resolved in planning; effort interpretation open |
| 2026-10-09 | First reminder request lacked thread destination | Retried with current-thread destination | Tool confirmed active daily automation: log-hackathon-team-contributions | Verified fixed |

## Anticipated risks — not incidents yet

### Implementation incidents on 10 October

- **Corrected deadline and brand:** user changed deadline to Sunday 09:00 IST and product name to Sahi GST. Updated all planning documents and replaced the calendar gates. Internal submission is 07:00 IST.
- **GitHub CLI absent:** existing Git Credential Manager account was available with required access. Created private Salman-a-gamer/Sahi-GST through GitHub API without printing credentials.
- **Network/file sandbox restrictions:** dependency installation and production export initially failed. Reran narrowly scoped installs/builds with reviewed access; both completed.
- **OCR identifier errors:** real Tesseract.js scan misread two GSTINs; human confirmation corrected them. A total discrepancy then generated the expected supplier request. Improved label handling for goods description and stated round-off. No claim of perfect extraction.
- **PostgreSQL encoding:** Windows default WIN1252 could not store the rupee sign in JSON. Initialized a separate UTF-8 local cluster; the complete 10-test suite then passed on PostgreSQL. The original local cluster was not destructively deleted.
- **Hosting:** user has Vercel, not Render/Neon accounts. Verified official Django support and prepared a single-project deployment; sign-in completed, free PostgreSQL provisioning still to complete.
- **Reminder state:** found the previously created reminder paused. Updated name/deadline while preserving that paused state.

| Risk | Planned response | Owner |
|---|---|---|
| Vision extraction mistakes | Critical-field confirmation, nulls and held-out tests | B + A testing |
| API/network failure | Timeout, retry and explicitly manual fallback | B |
| Over-scoping | Gate stretch features behind live core loop | Both |
| Tax false positives | Scoped rules, explicit prerequisites, abstention | B + knowledgeable reviewer |
| Frontend/backend drift | Freeze shared schema and integrate early | Both |
| Deployment trouble | Hosted skeleton early; reserve and simple topology | B |
| Unclear customer value | Interview owners/bookkeeper and observe task | A |
| Missed submission | 07:00 internal deadline, signed-out link checks | A |

## Append template

- Date/time IST:
- Owner:
- Observed problem and reproduction:
- Impact on user/demo/deadline:
- Attempts and evidence:
- Chosen fix and reason:
- Verification performed and outcome:
- Remaining limitation:
- Related commit/artifact:

Never write “fixed” without verification. Record failed attempts when they explain the final decision, without including secrets or customer data.
