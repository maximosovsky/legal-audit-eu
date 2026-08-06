# EU/UK Legal Audit — example.com — 2026-08-04
> Example output only. Legal-engineering audit, not legal advice.

## Executive summary

- 🔴 GA4 and Meta Pixel are present in source and appear to load before an affirmative cookie choice.
- 🟠 Privacy Notice mentions “service providers” generically but the code names Stripe, SendGrid, Sentry, and OpenAI.
- 🟡 Owner/legal tasks: Art. 28 DPA review, SCC/transfer review for US vendors, DPIA screening for AI chat logs.

## Evidence inspected

- Local repo: `example-app` at commit `abc1234`
- Live URL: `https://example.com`
- Legal docs: Privacy Notice, Cookie Policy, Terms, Refund Policy
- Scanner command: `python scripts/scan.py --jurisdiction eu --samples example-app https://example.com`

## App reality inventory

| Category | Evidence | Data/purpose/vendor | Notes |
|---|---|---|---|
| Contact form | `src/components/Contact.tsx` | name, email, message | Requires privacy link and lawful basis. |
| Trackers | `gtag`, `facebook.com/tr` | analytics/ad measurement | Must be blocked until consent unless exempt. |
| Vendors | Stripe, SendGrid, Sentry, OpenAI | payments, email, errors, AI chat | Add to processor/transfer review. |

## Findings

| Severity | Area | Evidence | Rule/article | Required fix | Owner |
|---|---|---|---|---|---|
| 🔴 | Cookie consent | GA4/Meta script loads before choice | ePrivacy/PECR + GDPR Art. 7 | Block non-essential trackers until opt-in; add reject/preferences controls | Code + docs |
| 🟠 | Vendor disclosure | Policy says “service providers” only | GDPR Arts. 13-14, 28 | Name or clearly categorize processors and purposes | Docs + legal |
| 🟡 | Transfers | US vendors present | GDPR Arts. 44-49 | SCC/transfer-impact review | Legal/ops |

## Code fixes available now

- Gate analytics/ad pixels behind CMP consent.
- Add footer links to Privacy Notice, Cookie Policy, Terms, Returns.
- Add unsubscribe link and suppression handling for newsletters.

## Document fixes

- Add lawful basis per purpose.
- Add retention periods/criteria.
- Add cookie table with provider/purpose/duration.

## Owner/legal/operations tasks

- Art. 28 DPA/vendor review.
- Art. 30 RoPA update.
- Art. 35 DPIA screening for AI chat logs.
- SCC/UK IDTA/Addendum transfer review.
