#!/usr/bin/env python3
from __future__ import annotations
import pathlib, re, sys
try:
    import yaml
except Exception as exc:
    print(f"PyYAML missing: {exc}", file=sys.stderr)
    sys.exit(1)

root = pathlib.Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
content = skill.read_text(encoding="utf-8")
assert content.startswith("---"), "SKILL.md must start with YAML frontmatter"
end = content.find("\n---\n", 3)
assert end != -1, "SKILL.md frontmatter must close with ---"
frontmatter = yaml.safe_load(content[3:end])
assert frontmatter["name"] == "legal-audit-eu"
assert frontmatter["description"] and len(frontmatter["description"]) <= 1024
assert content[end + 5 :].strip(), "SKILL.md body is empty"
required_files = [
    "README.md",
    "llms.txt",
    "llms-full.txt",
    "LICENSE",
    "scripts/scan.py",
    "references/gdpr-article-map.md",
    "references/eprivacy-cookie-consent.md",
    "references/uk-gdpr-pecr-note.md",
    "references/dsa-ai-act-triage.md",
    "examples/sample-report.md",
    "tests/fixtures/sample-site/index.html",
]
missing = [p for p in required_files if not (root / p).exists()]
assert not missing, f"Missing required files: {missing}"
print("skill validation ok")
