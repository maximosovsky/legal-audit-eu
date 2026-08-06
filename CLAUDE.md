# legal-audit-eu

Privacy-lawyer-grade EU/EEA/UK website audit skill. This repository is a Hermes Agent skill that also works as a Claude Code project.

## What this skill does

Compares a website or web-app's actual behavior (forms, trackers, cookies, payments, AI features, user flows) against its legal documents (Privacy Notice, Cookie Policy, Terms, DPA, refund/withdrawal terms), and produces a lawyer-reviewable gap analysis mapped to:

- GDPR (EU and UK) — transparency, lawful basis, consent, data-subject rights, processors, transfers, DPIA, DPO, RoPA
- ePrivacy Directive / PECR — cookies, pixels, analytics, session replay, consent timing
- UK GDPR / DPA 2018 / PECR — separate from EU layer
- Consumer/ecommerce law — trader identity, 14-day withdrawal, refunds, subscriptions, dark patterns
- Digital Services Act (DSA) — platforms, marketplaces, moderation, ads, recommenders
- AI Act — chatbots, scoring, profiling, generated content, AI transparency
- Accessibility — WCAG / European Accessibility Act signals
- Security disclosure — HTTPS, secrets, breach contact

## Quick start

```bash
python scripts/scan.py --jurisdiction eu tests/fixtures/sample-site
python scripts/scan.py --jurisdiction uk --include-markdown --samples .
```

## Principle

This is legal-engineering triage, not legal advice. Output is an evidence pack for qualified counsel review.