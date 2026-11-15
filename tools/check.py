#!/usr/bin/env python3
"""Health and safety check for the Fab Rides site. GitHub runs it on every pull request.
Run locally with: python3 tools/check.py   (exit code 1 = errors, merge blocked)

Errors: things that must never ship. Warnings: decisions for Fabrizio, never auto-fixed.
Changing this file needs Fabrizio's approval (see CLAUDE.md)."""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

SITE = Path(__file__).resolve().parent.parent / "site"

# Outbound link domains Fabrizio has approved. Adding one needs his approval.
LINK_DOMAINS = {
    "fab-rides.co.uk", "fabrizio.deliberali.com", "fab-wines.co.uk",
    "signal.org", "parthianclimbing.com", "www.epic-series.com", "www.in-lombardia.it",
}
# Hosts allowed to serve images (old WordPress, until the images move into site/assets).
IMAGE_HOSTS = {"fab-rides.co.uk"}
FORBIDDEN_TAGS = {"script", "iframe", "form", "object", "embed", "frame", "frameset", "base"}
REQUIRED_HEADERS = ["default-src 'none'", "frame-ancestors 'none'", "form-action 'none'", "X-Content-Type-Options: nosniff"]
EXPECTED_REDIRECTS = {"/feed / 301", "/wp-admin / 301", "/wp-login.php / 301"}

errors, warnings = [], []


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.srcs, self.tags, self.title, self.h1 = [], [], [], "", 0
        self._title = False
        self.inline_style = self.handlers = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        for k in ("src", "srcset", "poster", "data"):
            if a.get(k):
                self.srcs.append(a[k])
        if tag == "link" and a.get("href"):
            self.srcs.append(a["href"])
        if "style" in a:
            self.inline_style += 1
        if any(k.startswith("on") for k in a):
            self.handlers += 1
        if tag == "title":
            self._title = True
        if tag == "h1":
            self.h1 += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._title = False

    def handle_data(self, data):
        if self._title:
            self.title += data


def host(url):
    return urlparse(url).hostname or ""


pages = sorted(SITE.glob("*.html"))
texts = {}
for page in pages:
    html = page.read_text(encoding="utf-8")
    texts[page.name] = html
    p = Page()
    p.feed(html)
    n = page.name

    if not p.title.strip():
        errors.append(f"{n}: missing <title>")
    if p.h1 != 1:
        errors.append(f"{n}: expected exactly one <h1>, found {p.h1}")
    for t in sorted(set(p.tags) & FORBIDDEN_TAGS):
        errors.append(f"{n}: <{t}> is not allowed (no scripts, embeds or forms without Fabrizio's approval)")
    if p.inline_style:
        errors.append(f"{n}: {p.inline_style} inline style attribute(s); the CSP blocks them, use site.css")
    if p.handlers:
        errors.append(f"{n}: inline event handler(s) (onclick etc.) are not allowed")
    if re.search(r"javascript:", html, re.I):
        errors.append(f"{n}: javascript: URL")

    for href in p.links:
        if href.startswith(("#", "mailto:")):
            continue
        if href.startswith(("http://", "https://")):
            if href.startswith("http://"):
                errors.append(f"{n}: insecure http link -> {href}")
            if host(href) not in LINK_DOMAINS:
                errors.append(f"{n}: link to unapproved domain {host(href)} (add to LINK_DOMAINS only with Fabrizio's approval)")
            continue
        target = href.split("#")[0]
        if target and not (SITE / target).exists():
            errors.append(f"{n}: broken internal link -> {href}")
        if href.startswith("//") or ":" in target:
            errors.append(f"{n}: unexpected link form -> {href}")

    for src in p.srcs:
        if src.startswith(("http://", "https://", "//")):
            if host(src if not src.startswith("//") else "https:" + src) not in IMAGE_HOSTS:
                errors.append(f"{n}: external resource from unapproved host -> {src}")
            else:
                warnings.append(f"{n}: images still load from the old WordPress site")
        elif not (SITE / src.split("?")[0]).exists():
            errors.append(f"{n}: missing local file -> {src}")

    if "contact-form-7" in html or "[contact" in html:
        errors.append(f"{n}: leftover WordPress shortcode")
    if re.search(r"whatsapp", re.sub(r'<a [^>]*idea1[^>]*>.*?</a>', "", html), re.I):
        errors.append(f"{n}: mentions WhatsApp (Fab Rides uses Signal)")
    if re.search(r"Deliberali", html):
        errors.append(f"{n}: name must be written 'de Liberali'")
    visible = re.sub(r"<[^>]+>", " ", html)
    if re.search(r"(\+44|\+39|\b0)\s?\d{2,4}[\s-]?\d{3}[\s-]?\d{3,4}\b", visible):
        errors.append(f"{n}: looks like a phone number; never publish phone numbers")
    if 'class="draft-note"' in html:
        errors.append(f"{n}: draft questions still on the page; answer them in tools/places.py before merging")
    if 'name="robots" content="noindex, nofollow"' not in html:
        errors.append(f"{n}: noindex removed; allowed only at the domain switch, with Fabrizio's approval")

headers = (SITE / "_headers").read_text(encoding="utf-8") if (SITE / "_headers").exists() else ""
for h in REQUIRED_HEADERS:
    if h not in headers:
        errors.append(f"_headers: missing or weakened security rule: {h}")
if "script-src" in headers or "unsafe-" in headers:
    errors.append("_headers: scripts or unsafe CSP keywords are not allowed")

redirects = (SITE / "_redirects").read_text(encoding="utf-8") if (SITE / "_redirects").exists() else ""
actual = {" ".join(l.split()) for l in redirects.splitlines() if l.strip() and not l.startswith("#")}
if actual != EXPECTED_REDIRECTS:
    errors.append(f"_redirects changed: {sorted(actual ^ EXPECTED_REDIRECTS)} (needs Fabrizio's approval and an update here)")

for w in sorted(set(warnings)):
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"{len(pages)} pages checked, {len(errors)} errors, {len(set(warnings))} warnings")
sys.exit(1 if errors else 0)
