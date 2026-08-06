# GDPR article map for EU website audits

Not legal advice. Use this file to map findings to GDPR obligations in reports.

| Area | GDPR basis | Practical audit evidence |
|---|---|---|
| Principles | Art. 5 | Purpose limitation, minimisation, accuracy, storage limitation, integrity/confidentiality, accountability. |
| Lawful basis | Art. 6 | Every purpose in the notice and code has a basis: contract, consent, legitimate interests, legal obligation, vital interests, public task. |
| Consent | Art. 7 + Recital 32 | Opt-in, specific, informed, unbundled, recorded, withdrawable as easily as given. |
| Children | Art. 8 | Age/parental-consent logic for information-society services offered to children. |
| Special categories | Art. 9 | Health, biometric, genetic, ethnicity, religion, politics, sexual orientation etc. require explicit Art. 9 basis. |
| Criminal offence data | Art. 10 | Only under official authority or authorized law with safeguards. |
| Transparency | Arts. 12-14 | Controller identity, purposes, lawful bases, recipients, transfers, retention, rights, complaint authority, automated decisions, date/version. |
| Rights | Arts. 15-22 | Access, rectification, erasure, restriction, portability, objection, automated-decision safeguards. |
| Privacy by design/default | Art. 25 | Defaults minimize data; optional tracking/marketing off until valid consent. |
| Joint controllers | Art. 26 | Joint-controller arrangements disclosed where parties jointly determine purposes/means. |
| Processors | Art. 28 | DPAs with hosting, analytics, email, CRM, payment, support, AI, storage processors. |
| RoPA | Art. 30 | Internal record of processing activities, especially for repeated/commercial processing. |
| Security | Art. 32 | Appropriate technical and organizational measures; encryption/pseudonymisation where relevant. |
| Breach | Arts. 33-34 | 72-hour supervisory-authority notification and data-subject communication where required. |
| DPIA | Art. 35 | Required for likely high-risk processing: systematic monitoring, sensitive data at scale, profiling with significant effects, children, AI/automated eligibility decisions. |
| Prior consultation | Art. 36 | If residual high risk remains after DPIA safeguards. |
| DPO | Arts. 37-39 | Public authority, large-scale systematic monitoring, or large-scale special-category/criminal-data processing. |
| EU representative | Art. 27 | Non-EU establishment targeting EU persons, unless narrow occasional/low-risk exemption applies. |
| Transfers | Arts. 44-49 | Adequacy, SCCs, BCRs, derogations; transfer-impact/supplementary-safeguard review for risky third countries. |

## Report wording pattern

Use precise but cautious language:

> Evidence: `<script src="https://www.googletagmanager.com/...">` loads on the landing page before a consent choice. Risk: non-essential analytics/ad tracking before consent under ePrivacy/PECR and invalid GDPR consent under Art. 7. Fix: block GTM/GA until opt-in, add reject/preferences controls, and update the cookie table with provider/purpose/duration.
