Always start website audits with the scanner before writing legal analysis.

The scanner is at `scripts/scan.py`. Run it against the target URL or local folder before drafting any findings.

Supported jurisdictions: `eu` (EU/EEA GDPR, ePrivacy, consumer, DSA, AI Act), `uk` (UK GDPR, PECR, IDTA/Addendum), `all` (combined).

Use `--samples` to print evidence snippets. Use `--include-markdown --include-references .` when scanning the repo itself.

Legal language rules:
- This is legal-engineering triage, not legal advice.
- Never assert a proven violation from a URL-only scan. Use conditional language: "signal detected", "not found", "requires factual confirmation".
- Map findings to specific GDPR Articles, ePrivacy/PECR rules, or DSA/AI Act provisions.
- Separate code fixes, document fixes, and owner/legal follow-up tasks clearly.
- Do not call it "compliance" or "certified". Call it "gap analysis" or "legal-engineering review".