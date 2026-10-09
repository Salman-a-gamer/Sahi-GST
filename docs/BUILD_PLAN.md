# Two-person build plan

Deadline: Sunday 11 October 2026, 09:00 IST. Internal submission: 07:00 IST. Planning starts Friday 9 October. Twenty combined person-hours is the conservative baseline; if twenty hours are available per teammate, use the extra hours for reliability and then stretch work. These are estimates, not delivery guarantees.

## Ownership

| Owner | Primary responsibility | Review responsibility |
|---|---|---|
| You (A; skills still to confirm) | User/problem validation, Next.js screens with Codex, evidence fixtures, pitch/video and submission | Try the backend with known cases; verify the user story |
| Friend (B; familiar with locked stack) | Django, PostgreSQL, Allauth, extraction adapter, rule engine and deployment | Review frontend/API handling and core demo claims |
| Both | API contract, end-to-end rehearsal, integration and contribution logs | Cross-review each other's changes |

If you are not comfortable debugging frontend code, you still own acceptance and the user flow; ask your friend to review the scaffold early. Codex accelerates scoped work, but does not remove integration or testing.

## Twenty-person-hour baseline

Hours below are combined effort, not wall-clock duration. Some tasks run concurrently; pair-work counts both people's time.

| Phase | A hours | B hours | Deliverable and gate |
|---|---:|---:|---|
| 1. Scope, interview and fixture/API agreement | 1.0 | 1.0 | One supported invoice case, expected fields/findings and shared JSON schema |
| 2. Scaffold and early hosting | 0.5 | 1.5 | Next.js talks to Django; PostgreSQL migration and Allauth login work; deployed health check |
| 3. First working vertical slice | 2.0 | 3.0 | Real image extraction, user confirmation, core arithmetic/presence checks and correction draft |
| 4. Failure handling and tests | 1.5 | 1.5 | Bad input, timeout, authorization and supported-rule cases handled |
| 5. Mobile clarity and measured demo | 1.0 | 1.0 | Phone flow, legible results, latency/accuracy evidence and no misleading claims |
| 6. Pitch, video, ZIP and submission | 2.0 | 0.5 | Live URL, slides, 2-minute video, tested ZIP and submission fields |
| 7. Reserve | 1.0 | 0.5 | Fix the biggest actual blocker; do not pre-spend on features |
| 8. Additional unassigned buffer | 1.0 | 1.0 | Hold for integration or submission problems |
| **Total** | **10.0** | **10.0** | **20 person-hours** |

The phase allocations include 1.5 hours of reserve plus 2 additional unassigned buffer hours. Do not pre-spend these on stretch features.

## Calendar gates

- **Saturday early morning (this work session):** build and test the local image-to-request loop, lock the free route and push Sahi-GST.
- **Saturday 12:00 IST target:** frontend/backend/PostgreSQL connectivity and authentication hosted. If hosting access is unavailable, complete reproducible deployment files and get the account setup done immediately.
- **Saturday 18:00 IST:** feature freeze. End-to-end checks on phone and desktop; fix the core flow, do not add major modules.
- **Saturday 22:00 IST:** UI/demo freeze; record the two-minute demo on the final deployed version.
- **Sunday 04:00 IST:** source ZIP, slides, video, contribution entries and live links ready.
- **Sunday 06:00 IST:** verify signed-out access, fresh input and final submission fields.
- **Sunday 07:00 IST:** submit and save confirmation. Do not wait for the 09:00 lock.

If starting later than a target, preserve the final submission buffer and cut scope. Twenty hours is aggressive for a polished full stack; the reserve is essential.

The deadline was corrected by the user on 10 October: **Sunday 09:00 IST**, not Sunday evening. The working/product name is **Sahi GST**, and the GitHub slug is **Sahi-GST**. No paid API or paid hosting may be enabled. Build an integrated invoice workspace around the core loop; do not treat unfinished roadmap tiles as working features.

## Cut list when behind

Cut in this order: animations → PWA install → extra languages → source bounding boxes → PDF import → duplicate detection → reconciliation. Keep real extraction, manual review, deterministic useful checks, clear results, failure handling and live deployment. Restrict to three well-tested arithmetic checks plus missing fields if necessary, and describe scope honestly.

If extraction is blocked, manual input preserves the rule-engine demonstration, but does not meet the intended AI value proposition. Show it as fallback; spend remaining effort restoring real extraction. A recorded success is backup evidence, not a substitute for the rubric's live MVP.

## With an additional twenty person-hours

Allocate 6 to unseen-image evaluation and fixes, 4 to deployment/device reliability, 4 to evidence UI and accessibility, 3 to user tests, 2 to pitch/video improvements and 1 to reserve. Add a stretch feature only after the core gate; do not automatically consume the extra budget with reconciliation.

## Working together with two Codex accounts

Use one shared Git repository, separate local clones and individual accounts. Codex chats do not automatically share project history across your accounts. The shared truth is committed files: README, specification, API schema, fixtures and logs.

Suggested branches: `feature/frontend-review` owned by A and `feature/backend-validation` owned by B. One person owns `contracts/` changes at a time. Both branch from the same baseline. Small pull requests or reviewed merges, every 60–90 minutes or at each working milestone, reduce integration surprises.

Do not ask both Codex sessions to rewrite the whole app. Give each a bounded directory, acceptance criteria, required tests and an explicit API schema. Review generated diffs before merging. B owns database migrations; A owns UI styling. If both need one shared file, coordinate first.

Codex supports separate Git worktrees for isolated work; worktrees need a Git repository, and a branch cannot be checked out in multiple worktrees simultaneously. Separate clones across your two machines are already sufficient. [Official worktree documentation](https://learn.chatgpt.com/docs/environments/git-worktrees)

Plus usage is limited and task-dependent; check the actual usage dashboard instead of planning around unlimited requests. Save complex reasoning for architecture, rules and debugging. Reuse concise committed specs rather than pasting the entire conversation into every task. [Official pricing and usage guidance](https://learn.chatgpt.com/docs/pricing)

Treat the app's runtime vision API credential/quota as a separate requirement. Do not assume a coding subscription gives the deployed Django server API access. Verify provider billing and a working server-side test call before depending on it.

## First shared contract session

1. Agree one synthetic invoice and its exact expected JSON.
2. Agree null/money/date types, field paths, result statuses and error payloads.
3. Decide how the browser reaches Django and how sessions/CSRF work.
4. Agree one account/workspace for demo; include a synthetic guest sample if time allows.
5. Both run the same fixture through their respective sides.

No database schema or endpoint changes without informing the other teammate. Add an API-contract version to fixtures.

## Copy-ready Codex tasks using your C-R-I-S-P-E format

These prompts are implementation handoffs for a later build turn. They do not claim the app exists.

### Backend task — friend

**C — Context:** We are two people building Sahi GST for a hackathon due 11 October 2026 at 09:00 IST. Read README.md and docs/MVP_SPEC.md. Stack is Next.js, Django, PostgreSQL and Django Allauth. Work on backend/ and backend tests only; coordinate contracts/ changes before editing them.

**R — Role:** Act as a Django engineer responsible for correctness, secure ownership checks and a small deployable MVP.

**I — Instruction:** Build the first vertical backend slice: supported image input, structured extraction through one configured provider, human-confirmed fields, deterministic missing-field/arithmetic checks and correction-request draft. Preserve original data and distinguish extraction edits from supplier corrections.

**S — Specification:** Agree the shared schema before coding. Use Decimal and null for unknowns. Include environment-variable examples without secrets, migrations, bounded errors/timeouts, setup steps and focused tests. Implement Allauth authentication using verified documentation for the chosen version. No alternative framework, tax-rate guessing or live GSTN claim.

**P — Performance:** A supported synthetic invoice completes the flow; known wrong totals are detected; unknown context abstains; another user cannot read the review. Run the relevant tests and report commands/results. Keep the source ZIP lean. Update the difficulties log with actual incidents and your contribution evidence.

**E — Example:** Confirmed taxable value 10000.00, CGST 900.00, SGST 900.00 and displayed total 12800.00 should yield expected arithmetic total 11800.00 and difference 1000.00, with a request to confirm then clarify with the supplier. Do not label this money recovered.

### Frontend task — you

**C — Context:** Read README.md and docs/MVP_SPEC.md. Backend teammate owns Django and migrations. Build the responsive Next.js UI against the agreed contract; work in frontend/ and frontend tests. Deadline is 11 October 2026, 09:00 IST.

**R — Role:** Act as a product designer and frontend engineer optimizing a short live demo for a small-business owner.

**I — Instruction:** Implement upload, source/field review, findings and copyable supplier-request screens. Start with explicit synthetic fixtures, then integrate the real API. Show Issue found, Needs review, Checked and Not checked separately.

**S — Specification:** Mobile-first layout, accessible contrast, keyboard labels, readable currency, text as well as colour, loading/error/retry states. Preserve original invoice. No fake source boxes, compliance percentages or unsupported guarantees. Mark fixture mode clearly until real integration.

**P — Performance:** No horizontal overflow at a narrow phone width; all primary actions keyboard-accessible; real API integration handles null/error states. Run appropriate checks and manually inspect phone/desktop views. Update contribution evidence and actual blockers.

**E — Example:** A total mismatch card says “Total differs by ₹1,000,” shows observed ₹12,800 versus arithmetic expected ₹11,800, and offers “Review amounts” followed by “Copy supplier request.”

### Integration review task — use after the two slices merge

**C — Context:** The merged Sahi GST MVP must work live before Sunday submission. Read the current spec and actual diff; do not assume planned features exist.

**R — Role:** Act as a skeptical reviewer and demo evaluator.

**I — Instruction:** Run the image-to-request journey, test missing/ambiguous input and authorization, and identify false tax claims or contract mismatches. Fix confirmed blockers within existing scope.

**S — Specification:** Return blockers ordered by demo impact with reproduction and evidence; update README status and the difficulties log. Do not expand feature scope.

**P — Performance:** Verify a fresh image, a clean case, an error case, unsupported context and provider failure. Report untested devices honestly. Check that secrets/customer data are absent from submitted artifacts.

**E — Example:** If an unknown place of supply produces “intra-state valid,” treat it as a bug; the result must ask for context or remain not checked.

## While Codex runs

You: contact one business owner/bookkeeper, draft the narration, collect consented/redacted examples or create synthetic ones, and rehearse the supplier-message wording.

Friend: verify hosting/database accounts, AI API credential and budget, deployment path and Allauth version integration. Both update contributions after each completed work block. These activities reduce the critical path more than watching generation.
