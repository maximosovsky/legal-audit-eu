<div align="center">

# 🇪🇺 legal-audit-eu

![CI](https://img.shields.io/github/actions/workflow/status/maximosovsky/legal-audit-eu/ci.yml?branch=main&style=for-the-badge&label=CI&logo=githubactions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GDPR](https://img.shields.io/badge/GDPR-EU%2FUK_Privacy-2563EB?style=for-the-badge)
![ePrivacy](https://img.shields.io/badge/ePrivacy-Cookie_Consent-7C3AED?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

**Privacy-lawyer-grade EU/EEA/UK website audit skill for GDPR, ePrivacy/PECR, consumer rights, DSA, AI Act, accessibility, and security signals.**

<a href="#-quick-start">Quick Start</a> · <a href="#-features">Features</a> · <a href="#-tech-stack">Tech Stack</a> · <a href="#-roadmap">Roadmap</a> · <a href="llms-full.txt">LLM Reference</a>

</div>

> `legal-audit-eu` turns a website or web-app repository into a lawyer-reviewable evidence pack: app reality, legal-document claims, GDPR article mapping, ePrivacy/cookie timing, platform/AI/consumer-law triage, and separated code/document/legal tasks.

<div align="center">

<!-- Preview image placeholder: add a real screenshot or diagram here when available. Do not link missing files. -->

</div>

---

## 💡 Concept

Most GDPR checklists stop at “there is a privacy policy.” This skill audits the harder question: **does the policy match what the product actually does?** It scans for forms, trackers, cookie/CMP signals, vendors, transfers, marketing, ecommerce, platform, AI, accessibility, and security evidence, then guides an agent through a EU/UK privacy-lawyer-grade review.

The workflow is article-aware and evidence-first. It maps findings to GDPR Articles, ePrivacy/PECR, EU/UK consumer rules, DSA/platform duties, AI Act triage, accessibility expectations, and owner-side obligations such as DPA/SCC, RoPA, DPIA, DPO, representative, and breach process review.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| App reality vs legal documents | Compares actual code/site behavior against Privacy Notice, Cookie Policy, Terms, DPA/subprocessor disclosures, and withdrawal/returns terms. |
| GDPR article mapping | Links findings to GDPR Arts. 5, 6, 7, 8, 9, 12–14, 15–22, 25, 28, 30, 32–35, 37–39, 44–49. |
| ePrivacy/PECR consent review | Flags cookie/CMP, tracker, pixel, session replay, reject/withdrawal, and timing signals. |
| UK-specific layer | Separates EU GDPR/ePrivacy from UK GDPR, DPA 2018, PECR, ICO, IDTA/Addendum, and UK representative issues. |
| Consumer/ecommerce checks | Covers trader identity, price transparency, 14-day withdrawal, digital-content exceptions, subscriptions, refunds, and dark-pattern signals. |
| DSA and AI triage | Flags platform, marketplace, moderation, recommender, ad transparency, chatbot, automated decision, and AI vendor risks. |
| Standard-library scanner | `scripts/scan.py` uses only Python stdlib and supports `eu`, `uk`, and `all` signal modes. |
| CI and validator | GitHub Actions runs frontmatter/package validation and scanner smoke tests on a fixture site. |
| LLM-ready docs | `llms.txt` and `llms-full.txt` summarize the repo for AI agents and documentation tools. |

---

## 🚀 Quick Start

```bash
git clone https://github.com/maximosovsky/legal-audit-eu.git
cd legal-audit-eu
python scripts/scan.py --jurisdiction eu tests/fixtures/sample-site
```

<details>
<summary>⚙️ Validation and real-site scan</summary>

```bash
python scripts/validate.py
python -m py_compile scripts/scan.py scripts/validate.py
python scripts/scan.py --jurisdiction eu /path/to/project https://example.eu
python scripts/scan.py --jurisdiction uk --samples /path/to/project https://example.co.uk
```

| Option | Description |
|--------|-------------|
| `--jurisdiction eu` | EU/EEA-focused GDPR/ePrivacy/consumer/DSA/AI signals. |
| `--jurisdiction uk` | UK GDPR/PECR/ICO/IDTA layer added. |
| `--jurisdiction all` | Combined EU + UK signal set. |
| `--samples` | Prints short evidence snippets for found signals. |
| `--include-markdown` | Scans `.md` and `.mdx` files. |
| `--include-references` | Includes `SKILL.md`, `README.md`, `references/`, `examples/`, and templates. |

</details>

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| Skill format | Markdown `SKILL.md` with YAML frontmatter |
| Scanner | Python 3.11, standard library only |
| Validation | Python + PyYAML in CI |
| CI | GitHub Actions |
| Documentation | README, references, examples, `llms.txt`, `llms-full.txt` |
| License | MIT |

<details>
<summary>📁 Project Structure</summary>

```text
legal-audit-eu/
├── .github/
│   └── workflows/
│       └── ci.yml
├── examples/
│   └── sample-report.md
├── references/
│   ├── dsa-ai-act-triage.md
│   ├── ecommerce-consumer-rights.md
│   ├── eprivacy-cookie-consent.md
│   ├── gdpr-article-map.md
│   ├── gdpr-eprivacy-checklist.md
│   ├── uk-gdpr-pecr-note.md
│   └── templates/
│       └── privacy-notice-outline.md
├── scripts/
│   ├── scan.py
│   └── validate.py
├── tests/
│   └── fixtures/
│       └── sample-site/
│           └── index.html
├── llms.txt
├── llms-full.txt
├── SKILL.md
├── README.md
└── LICENSE
```

</details>

---

## 🗺️ Roadmap

- [x] GDPR article-aware legal-engineering workflow
- [x] ePrivacy/PECR cookie and tracker consent scanner
- [x] UK GDPR/PECR distinction and transfer-tool notes
- [x] DSA/platform, AI Act, ecommerce, accessibility, and security triage
- [x] Standard-library scanner with `eu`, `uk`, and `all` modes
- [x] CI, fixture site, validator, sample report, and LLM discovery files
- [ ] Add optional JSON output for downstream audit automation
- [ ] Add browser/network timing checklist for deployed CMP and tracker verification
- [ ] Add country-specific regulator notes for CNIL, ICO, AEPD, Garante, and German DPA practice

---

## 🤝 Contributing

Fork → `feature/name` → PR.

Please keep changes evidence-first: do not add legal claims without source-grounded wording, and do not make the scanner print secrets, tokens, personal data, or sensitive evidence values.

---

## 📄 License

[Maxim Osovsky](https://www.linkedin.com/in/osovsky/). Licensed under [MIT](LICENSE).
