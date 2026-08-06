---
name: legal-audit-eu
description: "Use when auditing EU/EEA/UK websites or web apps as a privacy-lawyer-grade engineering review: compare real data flows and legal documents against GDPR, ePrivacy/PECR, UK GDPR, consumer/ecommerce rules, DSA/platform duties, AI Act triage, accessibility, marketing, transfers, processors, DPIA/DPO/RoPA, and security-disclosure signals."
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [legal-audit, gdpr, eprivacy, cookies, uk-gdpr, dsa, ai-act, ecommerce, accessibility, eu]
    related_skills: []
---

# Legal Audit EU — privacy-lawyer-grade website compliance review

> This is a legal-engineering audit workflow, not legal advice. It is designed to help an agent or engineer produce a lawyer-reviewable evidence pack. Final conclusions, regulated-sector decisions, and public legal wording should be reviewed by qualified EU/UK counsel.

## Overview

This skill audits whether an EU/EEA/UK-facing website or web app has legally coherent public documents and user flows. The core method is not “does the site have a privacy policy?” but:

1. **App reality** — what the code/site actually collects, stores, tracks, shares, sells, profiles, emails, texts, uploads, recommends, or moderates.
2. **Legal-document claims** — what the Privacy Notice, Cookie Policy, Terms, DPA, refund/withdrawal terms, accessibility statement, and platform rules say.
3. **Gap analysis** — mismatches between reality and documents, plus missing user controls and owner-side legal tasks.
4. **Article/rule mapping** — findings mapped to GDPR/ePrivacy/PECR/consumer/DSA/AI/accessibility obligations.
5. **Action plan** — code fixes, document fixes, and owner/legal tasks separated clearly.

Use this when the user asks to check a website, SaaS, ecommerce store, landing page, marketplace, community, newsletter, AI app, or mobile/web app for EU/UK privacy/legal compliance signals.

## Scope

### Core EU/UK regimes

- **EU GDPR / UK GDPR** — transparency, lawful basis, privacy notice, consent, data-subject rights, retention, processors, security, breach, DPIA, DPO, RoPA, representatives, transfers.
- **ePrivacy Directive / UK PECR** — cookies, pixels, analytics, session replay, social embeds, direct marketing consent.
- **EU consumer/ecommerce law** — trader identity, price transparency, 14-day withdrawal where applicable, returns/refunds, subscriptions, unfair practices, digital content/service exceptions.
- **Digital Services Act (DSA)** — if the service hosts user content, marketplace listings, ads, recommender systems, or moderation flows.
- **AI Act triage** — if the site uses chatbots, scoring, profiling, biometric-like features, recommender AI, safety/eligibility decisions, or generated content.
- **Accessibility** — WCAG / European Accessibility Act / UK accessibility risk signals.
- **Security disclosure hygiene** — HTTPS, secrets, sensitive data in URLs, security contact, basic technical safeguards.

### Out of scope unless explicitly requested

- Full DPA/SCC drafting.
- Data-protection impact assessment completion.
- Country-by-country local counsel opinion.
- Regulated-sector licensing analysis.
- Penetration testing.

## Inputs to collect

Prefer source/code plus live site. Do not rely only on marketing claims.

| Input | Why it matters |
|---|---|
| Local repo or GitHub URL | Extract real forms, SDKs, trackers, APIs, storage, auth, email/SMS, payments, AI vendors. |
| Live URL | Check deployed scripts, cookie banner, forms, legal footer links, network/tracker timing. |
| Privacy Notice / Privacy Policy | GDPR Arts. 12-14 transparency baseline. |
| Cookie Policy / CMP text | ePrivacy consent and tracker disclosure. |
| Terms / Terms of Sale | Consumer, subscription, marketplace, and service contract terms. |
| Refund/withdrawal policy | EU consumer rights and digital-content exceptions. |
| DPA/subprocessor list | Processor/vendor reality and Art. 28 obligations. |
| Country/user targeting | EU-only, UK-only, global, children, sector-specific. |

## Fast workflow

1. **Run signal scan**

```bash
python scripts/scan.py --jurisdiction eu [path_to_project] [https://example.eu]
python scripts/scan.py --jurisdiction uk [path_to_project] [https://example.co.uk]
python scripts/scan.py --jurisdiction all [path_to_project] [https://example.com]
```

2. **Inventory app reality**

Extract and name concrete evidence:

- forms and fields: email, phone, address, payment, health, biometrics, profile, uploaded files;
- auth: email/password, OAuth, SSO, social login, session cookies;
- trackers: GA4/GTM, Meta, TikTok, LinkedIn, Hotjar, Clarity, Segment, Amplitude;
- vendors/processors: hosting, DB, auth, email, CRM, payments, support, AI APIs, analytics, storage;
- storage and retention: DB tables, logs, backups, object storage, localStorage/cookies;
- communications: newsletter, transactional email, SMS/WhatsApp, push;
- user controls: export, delete, unsubscribe, cookie preferences, account closure;
- marketplace/platform flows: user content, sellers, moderation, complaints, recommendations, ads;
- AI flows: chatbot disclosure, generated content, scoring/profiling, human review.

3. **Extract legal-document claims**

For each document, extract claims about controller identity, purposes, lawful bases, data categories, recipients, transfers, retention, rights, cookies, marketing, children, security, complaint authority, and document date/version.

4. **Compare reality vs documents**

Classify findings:

- 🔴 **Critical** — undisclosed personal data collection/sharing, tracking before consent, missing lawful basis, missing transfer safeguards, no privacy notice for real processing, invalid bundled/pre-ticked consent, child/special-category risk without safeguards.
- 🟠 **Important** — vague or generic policy, weak retention, missing vendor names/categories, missing DSAR workflow, incomplete cookie table, incomplete ecommerce withdrawal/cancellation terms.
- 🟡 **Owner/legal task** — RoPA, DPA/SCC review, DPIA, DPO/EU representative decision, breach procedure, local counsel review.
- 🟢 **Best practice** — plain-language summary, document versioning, security.txt, accessibility statement clarity.

5. **Report with article/rule mapping**

Every finding should have:

- evidence;
- legal basis/risk area;
- concrete fix;
- owner of fix: code, document, or legal/operations.

## GDPR article map for audit use

Use this as the default mapping table. See `references/gdpr-article-map.md` for the expanded reference.

| Area | Primary GDPR basis | Audit question |
|---|---|---|
| Principles | Art. 5 | Are processing purposes lawful, fair, transparent, limited, minimized, accurate, storage-limited, secure, and accountable? |
| Lawful basis | Art. 6 | Is each purpose mapped to contract, consent, legitimate interest, legal obligation, vital interest, or public task? |
| Consent | Art. 7, Recital 32 | Is consent opt-in, specific, informed, unbundled, recorded, and as easy to withdraw as give? |
| Children | Art. 8 | If information-society services target children, is age/parental-consent logic addressed? |
| Special categories | Art. 9 | Are health/biometric/etc. data identified with explicit Art. 9 basis and safeguards? |
| Transparency | Arts. 12-14 | Does the privacy notice match real processing and provide required information? |
| Rights | Arts. 15-22 | Are access, rectification, erasure, restriction, portability, objection, profiling/ADM rights operationally supported? |
| Privacy by design | Art. 25 | Are defaults privacy-preserving and data minimized? |
| Processors | Art. 28 | Are processors/subprocessors identified and covered by DPAs? |
| RoPA | Art. 30 | Is an internal record of processing activities needed/maintained? |
| Security | Art. 32 | Are technical/organizational measures proportionate to risk? |
| Breach | Arts. 33-34 | Is there a 72-hour supervisory-authority breach process and data-subject notification logic where required? |
| DPIA | Art. 35 | Is a DPIA needed for high-risk processing, profiling, systematic monitoring, sensitive data, children, or AI? |
| DPO | Arts. 37-39 | Is DPO appointment required and contact disclosed if appointed? |
| EU representative | Art. 27 | If non-EU controller/processor targets EU people, is an EU representative required? |
| Transfers | Arts. 44-49 | Are third-country transfers disclosed with SCCs/adequacy/BCR/derogation and post-Schrems II safeguards? |

## Detailed checklist

### A. App reality vs legal documents

| Check | Status guidance |
|---|---|
| All personal data categories in code/forms are disclosed in privacy notice. | 🔴 if code collects data absent from policy. |
| All vendors/processors in code are disclosed by name or sufficiently specific category. | 🟠/🔴 depending on sensitivity and transfer. |
| All purposes in product flows have lawful bases in the notice. | 🔴 if no Art. 6 basis for key processing. |
| Cookie/tracker reality matches Cookie Policy/CMP. | 🔴 if trackers fire before consent or are undisclosed. |
| Retention stated per category/purpose or with concrete criteria. | 🟠 if vague only. |
| User rights channel exists and is practical. | 🔴/🟠 if absent or hidden. |

### B. Privacy notice — GDPR Arts. 12-14

Required or normally expected:

- controller identity and contact;
- DPO contact where applicable;
- EU/UK representative where applicable;
- processing purposes;
- lawful basis for each purpose;
- legitimate interests where used;
- categories of personal data;
- source of data if not direct;
- recipients/categories of recipients;
- international transfers and safeguards;
- retention periods or criteria;
- rights and how to exercise them;
- right to withdraw consent;
- right to lodge complaint with supervisory authority;
- whether data provision is contractual/legal and consequences of refusal;
- automated decision-making/profiling information where applicable;
- effective date/version.

### C. Consent and marketing — GDPR Art. 7 + ePrivacy/PECR

- No pre-ticked consent boxes.
- Separate consents for separate purposes: service, newsletter, profiling, third-party marketing.
- Withdrawal as easy as giving consent.
- Marketing email/SMS has opt-in or valid soft opt-in, clear unsubscribe, and suppression list handling.
- Consent records should include timestamp, version, purposes, source, and withdrawal.

### D. Cookies, pixels, and session replay — ePrivacy/PECR

- Strictly necessary cookies only before consent.
- Analytics/ads/pixels/session replay/social embeds blocked until consent unless a local regulator-specific exemption is clearly relied on.
- “Reject all” or equivalent is as easy as “Accept all”.
- Preferences are granular by purpose/vendor where feasible.
- User can reopen and withdraw preferences.
- Cookie table includes name, provider, purpose, category, duration, and third-party access.
- Consent Mode/TCF implementation does not silently send ad/analytics signals before valid consent.
- Session replay tools are disclosed and masked to avoid sensitive-field capture.

### E. International transfers — GDPR Ch. V / UK transfer rules

- Identify vendors outside EEA/UK, including US cloud, analytics, support, AI, email, CDN, payments.
- Identify transfer mechanism: adequacy decision, SCCs, BCRs, UK IDTA/Addendum, derogation.
- For US/other high-risk transfers, note transfer-impact/post-Schrems II assessment and supplementary safeguards as owner/legal task.
- Privacy notice should disclose transfer countries or categories and safeguards.

### F. Processors, RoPA, DPIA, DPO, representative

Separate public website fixes from owner/legal tasks:

- **Art. 28 DPA** — processor contracts for hosting, analytics, email, CRM, payments, AI APIs, support.
- **Art. 30 RoPA** — internal record of processing activities; especially controller/processor details, purposes, categories, recipients, transfers, retention, security.
- **Art. 35 DPIA** — likely needed for systematic monitoring, large-scale special categories, children, high-risk AI/profiling, location tracking, biometric or eligibility decisions.
- **Arts. 37-39 DPO** — decide whether required; disclose contact if appointed.
- **Art. 27 representative** — non-EU/UK organization targeting EU/UK users may need representative unless narrow exemption applies.
- **Arts. 33-34 breach** — 72-hour supervisory-authority workflow and data-subject notification logic.

### G. Ecommerce and consumer rules

Check if the site sells goods, services, subscriptions, digital content, courses, tickets, or memberships.

- trader/legal identity, address, contact, registration/VAT where applicable;
- product/service characteristics;
- total price including taxes and mandatory fees;
- delivery costs and timing;
- payment method and contract formation point;
- Terms of Sale before checkout;
- 14-day withdrawal right where applicable;
- exceptions for digital content/services started before withdrawal period ends;
- model withdrawal form/process where applicable;
- refund timing and return costs;
- subscription/autorenewal terms and easy cancellation;
- no misleading scarcity, hidden fees, or dark patterns.

### H. DSA platform triage

If the service hosts user content, seller listings, community posts, reviews, ads, or marketplace offers, check:

- clear terms for content moderation;
- notice-and-action mechanism;
- statement of reasons for restrictions/removals where applicable;
- internal complaint handling;
- trader traceability for marketplaces;
- ad transparency: who paid, why shown, targeting parameters;
- recommender-system transparency and user choice where applicable;
- protection of minors and ban/limits on sensitive-data ad targeting;
- dark-pattern restrictions for online platforms.

### I. AI Act / automated systems triage

If the product uses AI/ML or automated decision logic, classify before making legal conclusions.

- Is there a user-facing chatbot or synthetic content? If yes, check transparency/disclosure.
- Is there profiling or automated decision-making with significant effects? Map to GDPR Art. 22 and AI Act high-risk triage.
- Does it touch employment, education, credit, essential services, law enforcement, migration, biometric ID/categorisation, or medical/safety contexts? Mark high-risk legal review.
- Are inputs/outputs logged, used for model training, or shared with AI vendors? Check privacy notice, transfers, DPAs, retention.
- Is human review/appeal available for consequential decisions?

### J. Accessibility

- Accessibility statement exists where appropriate.
- Forms have labels, errors, keyboard access, focus state, contrast, alt text.
- Checkout/account/cookie controls are keyboard-accessible.
- Public-sector sites and covered private services/products may need stronger WCAG/EAA review.

### K. Security and disclosure hygiene

- HTTPS for all forms; no mixed-content sensitive resources.
- No secrets/tokens in client code, HTML, repo, or logs.
- No personal data in URL query strings where avoidable.
- Basic security headers considered: HSTS, CSP, X-Content-Type-Options, Referrer-Policy, Permissions-Policy.
- Cookies use Secure, HttpOnly where appropriate, SameSite.
- security.txt or contact path for vulnerability reports.

## Report template

```markdown
# EU/UK Legal Audit — <domain> — <YYYY-MM-DD>
> Legal-engineering audit, not legal advice. Final public wording and regulated-sector conclusions require qualified counsel review.

## Executive summary
<2-5 bullets: top risks, whether live site/code/docs were inspected, immediate blockers.>

## Evidence inspected
- Local repo / commit:
- Live URL:
- Legal documents:
- Scanner command:
- Pages/flows manually checked:

## App reality inventory
| Category | Evidence | Data/purpose/vendor | Notes |
|---|---|---|---|
| Forms | ... | ... | ... |
| Trackers | ... | ... | ... |
| Vendors/processors | ... | ... | ... |

## Legal-document claims
| Document | Claims | Gaps vs reality |
|---|---|---|
| Privacy Notice | ... | ... |
| Cookie Policy | ... | ... |
| Terms/Returns | ... | ... |

## Findings
| Severity | Area | Evidence | Rule/article | Required fix | Owner |
|---|---|---|---|---|---|
| 🔴 | Cookie consent | GA4 fires before consent | ePrivacy/PECR + GDPR Art. 7 | Block analytics until opt-in; update CMP and cookie table | Code + docs |
| 🟠 | Retention | Policy says “as long as necessary” only | GDPR Arts. 5(1)(e), 13(2)(a) | Add category-specific retention periods/criteria | Docs + legal |

## Code fixes available now
- ...

## Document fixes
- ...

## Owner/legal/operations tasks
- Art. 28 DPA/vendor review
- Art. 30 RoPA
- Art. 35 DPIA decision
- Art. 27 EU representative / UK representative decision
- DPO decision
- SCC/IDTA/transfer-impact review

## Residual lawyer-review points
- ...
```

## Common pitfalls

1. Do not treat a banner as compliant if trackers already fired before consent.
2. Do not audit only text. Compare policy to code, cookies, vendors, forms, logs, and live network behavior.
3. Do not rely on “legitimate interest” for tracking/ads/marketing without considering ePrivacy prior consent.
4. Do not merge EU and US logic. “Do Not Sell” is US-specific; EU needs lawful basis, transparency, rights, and prior cookie consent.
5. Do not decide DPO/DPIA/Art. 27 representative applicability from one keyword. Mark as owner/legal task when facts are incomplete.
6. Do not ignore UK differences: PECR/ICO, UK GDPR, IDTA/Addendum, UK representative where applicable.
7. Do not print secrets or personal data discovered during audit. Redact values and report file/location.
8. Do not claim compliance. Use “signals”, “gaps”, “likely risk”, and “lawyer review required”.

## Verification checklist

- [ ] Scanner run with correct jurisdiction mode (`eu`, `uk`, or `all`).
- [ ] Legal docs read, not just discovered by filename.
- [ ] Live cookie/tracker timing checked in browser/network or code.
- [ ] App reality inventory completed with named vendors and data categories.
- [ ] GDPR article map applied to findings.
- [ ] ePrivacy/PECR cookie consent assessed separately from GDPR notice.
- [ ] Ecommerce/consumer obligations assessed if money changes hands.
- [ ] DSA/AI Act/accessibility triage performed where relevant.
- [ ] Code/document/legal-owner tasks separated.
- [ ] Report includes evidence and does not expose secrets or personal data.
