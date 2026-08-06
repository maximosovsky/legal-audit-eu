#!/usr/bin/env python3
"""EU/UK legal-audit signal scanner.

Usage:
  python scripts/scan.py [--jurisdiction eu|uk|all] [--include-markdown] [--include-references] [path] [https://site]

The scanner gathers engineering signals only. It does not determine legal compliance.
It intentionally defaults to EU mode and avoids scanning this skill's own reference
material unless requested, so self-tests do not produce misleading US/reference hits.
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import ssl
import sys
import urllib.request
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

TRACKERS: Dict[str, str] = {
    "Google Analytics / Tag Manager": r"gtag\(|googletagmanager\.com|google-analytics\.com|G-[A-Z0-9]{6,}|UA-\d+",
    "Meta/Facebook Pixel": r"connect\.facebook\.net|fbq\(|facebook\.com/tr",
    "TikTok Pixel": r"analytics\.tiktok\.com|ttq\(",
    "LinkedIn Insight": r"snap\.licdn\.com|linkedin\.com/px",
    "Hotjar / session replay": r"static\.hotjar\.com|hotjar\(|hj\(",
    "Microsoft Clarity": r"clarity\.ms|clarity\(",
    "Segment / RudderStack / Amplitude": r"cdn\.segment\.com|rudderstack|amplitude\.com|amplitude\(",
    "Sentry / error monitoring": r"sentry\.io|@sentry|Sentry\.init",
}

CONSENT: Dict[str, str] = {
    "Cookie/CMP text": r"cookie|cookies|consent|privacy preferences|manage preferences|accept all|reject all|essential only",
    "CMP vendor": r"onetrust|cookiebot|usercentrics|osano|iubenda|termly|didomi|quantcast|trustarc|complianz",
    "Consent Mode / TCF": r"gtag\(['\"]consent|__tcfapi|IABTCF|euconsent|TCFv2|google consent mode",
    "Reject/decline wording": r"reject all|decline|deny|essential only|necessary only|refuse|отклонить",
    "Manage preferences wording": r"manage preferences|cookie settings|privacy settings|change consent|withdraw consent",
}

FORMS: Dict[str, str] = {
    "Email field": r'type=["\']email|name=["\'][^"\']*email|id=["\'][^"\']*email',
    "Phone field": r'type=["\']tel|name=["\'][^"\']*phone|inputmode=["\']tel',
    "Name field": r'name=["\'][^"\']*(name|firstName|lastName|full_name|fullname)',
    "Address field": r'name=["\'][^"\']*(address|street|city|zip|postal|postcode)',
    "Payment/billing field": r"stripe|paypal|adyen|checkout|billing|cardholder|payment",
    "Consent checkbox": r'type=["\']checkbox[^>]*(consent|agree|privacy|terms|marketing)|(?:consent|agree|privacy|terms|marketing)[^>]*type=["\']checkbox',
    "Prechecked checkbox": r'type=["\']checkbox[^>]*(checked|defaultChecked)|(?:checked|defaultChecked)[^>]*type=["\']checkbox',
    "Newsletter / marketing signup": r"newsletter|subscribe|marketing emails|email marketing|mailchimp|sendgrid|klaviyo|brevo|customer.io",
}

LEGAL_PAGES: Dict[str, str] = {
    "Privacy Notice / Privacy Policy": r"privacy policy|privacy notice|data protection notice|privacy statement",
    "Terms / Terms of Service": r"terms of service|terms and conditions|terms of use|terms of sale",
    "Cookie Policy": r"cookie policy|cookies notice|cookie notice",
    "Refund / returns / withdrawal": r"refund policy|return policy|returns|right of withdrawal|withdrawal period|cancel(?:lation)? policy",
    "Contact / trader identity": r"contact us|legal notice|imprint|company number|registered office|business address|VAT|trader",
    "Unsubscribe": r"unsubscribe|opt out|email preferences",
    "Accessibility": r"accessibility statement|wcag|european accessibility act|keyboard navigation",
}

GDPR: Dict[str, str] = {
    "GDPR / UK GDPR mention": r"gdpr|uk gdpr|data protection act 2018",
    "Lawful basis language": r"legal basis|lawful basis|legitimate interest|contract necessity|consent|vital interests|public task|legal obligation",
    "Data-subject rights": r"right of access|right to erasure|right to rectification|right to restriction|data portability|right to object|data subject rights|DSAR",
    "DPO / representative": r"data protection officer|\bDPO\b|EU representative|UK representative|Article 27",
    "Retention language": r"retention period|data retention|how long we keep|storage limitation|delete.*data",
    "International transfers": r"standard contractual clauses|SCCs|adequacy decision|international transfer|third countr|IDTA|UK Addendum",
    "Processor / DPA language": r"processor|subprocessor|sub-processor|data processing agreement|\bDPA\b|Art\. 28|Article 28",
    "Breach language": r"data breach|personal data breach|72 hours|supervisory authority|incident notification",
    "DPIA / high risk": r"DPIA|data protection impact assessment|high risk processing|systematic monitoring",
}

EU_CONSUMER_DSA_AI: Dict[str, str] = {
    "14-day withdrawal": r"14 days|fourteen days|right of withdrawal|withdrawal form",
    "Subscription / renewal": r"subscription|auto-renew|automatic renewal|recurring|cancel subscription",
    "Marketplace / trader traceability": r"marketplace|seller|trader|merchant|third-party listing|vendor listing",
    "Notice-and-action / moderation": r"notice and action|content moderation|report illegal content|statement of reasons|internal complaint",
    "Ads / recommender transparency": r"advertisement transparency|why am I seeing this|recommender system|recommendation algorithm|targeting parameters",
    "AI / automated decisions": r"artificial intelligence|\bAI\b|chatbot|automated decision|profiling|machine learning|LLM|OpenAI|Anthropic",
    "Children/minors": r"children|minors|under 16|parental consent|age gate|age verification",
    "Special-category data": r"health data|biometric|religion|political opinion|sexual orientation|ethnic origin|genetic data",
}

UK_SPECIFIC: Dict[str, str] = {
    "PECR / ICO": r"PECR|Privacy and Electronic Communications Regulations|Information Commissioner's Office|\bICO\b",
    "UK transfer tools": r"IDTA|international data transfer agreement|UK Addendum|UK GDPR",
    "UK representative": r"UK representative|representative in the UK",
}

SECURITY: Dict[str, str] = {
    "Potential client-side secret": r"(api[_-]?key|secret|token|private[_-]?key)\s*[:=]\s*[\"'][A-Za-z0-9_\-]{20,}",
    "HTTP asset / mixed content": r"http://[^\s'\")<]+",
    "Env/credential reference": r"\.env|AWS_SECRET|DATABASE_URL|PRIVATE_KEY|SECRET_KEY",
    "security.txt / disclosure": r"security\.txt|vulnerability disclosure|responsible disclosure|security contact",
}

SCAN_EXTS_BASE = ("*.html", "*.htm", "*.js", "*.jsx", "*.ts", "*.tsx", "*.vue", "*.svelte", "*.php")
MARKDOWN_EXTS = ("*.md", "*.mdx")
SKIP_PARTS_BASE = {".git", "node_modules", "dist", "build", ".next", "vendor", "__pycache__", ".pytest_cache"}
REFERENCE_PARTS = {"references", "examples", "templates"}
REFERENCE_FILES = {"SKILL.md", "README.md", "LICENSE"}

@dataclass
class ScanResult:
    label: str
    found: bool
    count: int
    sample: str = ""


def compile_groups(jurisdiction: str) -> List[Tuple[str, Dict[str, str]]]:
    groups: List[Tuple[str, Dict[str, str]]] = [
        ("Trackers / analytics / SDKs", TRACKERS),
        ("Cookie / consent signals", CONSENT),
        ("Personal-data collection forms", FORMS),
        ("Legal pages / notices", LEGAL_PAGES),
        ("GDPR / data-protection signals", GDPR),
        ("EU consumer / DSA / AI triage", EU_CONSUMER_DSA_AI),
    ]
    if jurisdiction in {"uk", "all"}:
        groups.append(("UK-specific signals", UK_SPECIFIC))
    groups.append(("Security / exposure signals", SECURITY))
    return groups


def should_skip(path: str, include_references: bool) -> bool:
    parts = set(os.path.normpath(path).split(os.sep))
    if parts & SKIP_PARTS_BASE:
        return True
    if not include_references:
        if parts & REFERENCE_PARTS:
            return True
        if os.path.basename(path) in REFERENCE_FILES:
            return True
    return False


def collect_text(root: str, include_markdown: bool, include_references: bool) -> Tuple[str, int, List[str]]:
    exts = list(SCAN_EXTS_BASE)
    if include_markdown:
        exts.extend(MARKDOWN_EXTS)
    files: List[str] = []
    for ext in exts:
        files.extend(glob.glob(os.path.join(root, "**", ext), recursive=True))
    kept_files: List[str] = []
    chunks: List[str] = []
    for f in sorted(set(files)):
        if should_skip(f, include_references):
            continue
        try:
            data = open(f, encoding="utf-8", errors="ignore").read()
        except Exception:
            continue
        kept_files.append(f)
        chunks.append(f"\n\n/* FILE: {f} */\n" + data)
    return "\n".join(chunks), len(kept_files), kept_files


def scan_group(text: str, patterns: Dict[str, str]) -> List[ScanResult]:
    out: List[ScanResult] = []
    for label, pattern in patterns.items():
        matches = list(re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE))
        sample = ""
        if matches:
            m = matches[0]
            start = max(0, m.start() - 50)
            end = min(len(text), m.end() + 80)
            sample = re.sub(r"\s+", " ", text[start:end]).strip()
        out.append(ScanResult(label, bool(matches), len(matches), sample))
    return out


def print_group(title: str, results: Iterable[ScanResult], show_samples: bool) -> None:
    print(f"\n## {title}")
    for result in results:
        marker = "FOUND" if result.found else "  no "
        line = f"  [{marker}] {result.label}"
        if result.found:
            line += f" ({result.count})"
        print(line)
        if show_samples and result.sample:
            print(f"      sample: {result.sample[:220]}")


def fetch_url(url: str) -> Tuple[str, str]:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "legal-audit-eu-signal-scanner/1.1"})
    body = urllib.request.urlopen(req, timeout=20, context=ctx).read().decode("utf-8", "ignore")
    scheme = "HTTPS" if url.lower().startswith("https://") else "HTTP (risk for personal-data forms)"
    return body, scheme


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="EU/UK legal-audit signal scanner")
    parser.add_argument("path", nargs="?", default=".", help="Project/site folder to scan")
    parser.add_argument("url", nargs="?", help="Optional live URL to fetch and scan")
    parser.add_argument("--jurisdiction", choices=["eu", "uk", "all"], default="eu", help="Signal set to print")
    parser.add_argument("--include-markdown", action="store_true", help="Scan .md/.mdx files too")
    parser.add_argument("--include-references", action="store_true", help="Scan reference/example/SKILL/README files too")
    parser.add_argument("--samples", action="store_true", help="Print short evidence snippets for found signals")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    abs_root = os.path.abspath(args.path)
    print(f"# EU/UK legal-audit signals — {abs_root}")
    print(f"Jurisdiction mode: {args.jurisdiction}")
    text, count, files = collect_text(args.path, args.include_markdown, args.include_references)
    print(f"Scanned files: {count}")
    if count == 0:
        print("Note: no scannable source files found. Use --include-markdown or --include-references if you are intentionally scanning docs.")
    for title, patterns in compile_groups(args.jurisdiction):
        print_group(title, scan_group(text, patterns), args.samples)
    if args.url:
        try:
            body, scheme = fetch_url(args.url)
            print(f"\n## Live URL: {args.url}\n  Protocol: {scheme}")
            for title, patterns in compile_groups(args.jurisdiction):
                print_group("Live: " + title, scan_group(body, patterns), args.samples)
        except Exception as exc:
            print(f"\n## Live URL error: {repr(exc)[:180]}")
    print("\n— Interpret signals with SKILL.md. A FOUND/NO result is evidence triage, not a legal conclusion. —")


if __name__ == "__main__":
    main()
