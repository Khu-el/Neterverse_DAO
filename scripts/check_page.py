#!/usr/bin/env python3
"""Checks the static portal page. No dependencies, no package manager.

CLAUDE.md is deliberate that this repo has no framework, bundler, package
manager or test suite, and that a static page which loads everywhere is the
design. This script respects that: it is stdlib-only and introduces no build
step. It checks two things that are mechanical, and that reviewers have so far
been checking by reading:

  1. Tag nesting is balanced. PR #3 recorded "verified: page tag nesting is
     balanced" as a manual read. This is that read, automated.

  2. No external subresource. The page carries its CSS inline and pulls
     nothing from a third party, which is why it renders offline and behind a
     restrictive network. A <script src>, <link href>, <iframe>, remote @font-face
     or @import pointing off-site would end that quietly -- the page would still
     look fine wherever the author tested it.

An ordinary <a href> to another site is a link, not a subresource, and is
expected here: the Discord row is one.

What this does NOT check, because no script can: whether a jurisdictional claim
is sound, whether a cited authority is real, or whether a "#" placeholder is
still honest. Those are Executive OS §5, §6 and §7 obligations on the person
editing the page.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

failures = []


def check_balance(path: str, text: str) -> None:
    # Strip comments, then <style>/<script> bodies, so CSS braces and any
    # angle brackets inside them are not read as markup.
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<(style|script)\b[^>]*>.*?</\1\s*>", "", text, flags=re.S | re.I)

    stack = []
    for match in re.finditer(r"<\s*(/?)\s*([a-zA-Z][a-zA-Z0-9]*)([^>]*?)(/?)\s*>", text):
        closing, name, attrs, self_closing = match.groups()
        name = name.lower()
        if name in VOID or self_closing or name == "!doctype":
            continue
        line = text[: match.start()].count("\n") + 1
        if not closing:
            stack.append((name, line))
        else:
            if not stack:
                failures.append(f"{path}:{line}  </{name}> closes nothing")
            elif stack[-1][0] != name:
                open_name, open_line = stack[-1]
                failures.append(
                    f"{path}:{line}  </{name}> closes <{open_name}> opened at line {open_line}"
                )
                stack.pop()
            else:
                stack.pop()
    for name, line in stack:
        failures.append(f"{path}:{line}  <{name}> is never closed")


def check_no_external_subresource(path: str, text: str) -> None:
    rules = [
        ("script src", r"<\s*script\b[^>]*\bsrc\s*=\s*[\"'](?P<url>[^\"']+)"),
        ("stylesheet link", r"<\s*link\b[^>]*\bhref\s*=\s*[\"'](?P<url>[^\"']+)"),
        ("iframe", r"<\s*iframe\b[^>]*\bsrc\s*=\s*[\"'](?P<url>[^\"']+)"),
        ("object or embed", r"<\s*(?:object|embed)\b[^>]*\b(?:data|src)\s*=\s*[\"'](?P<url>[^\"']+)"),
        ("remote image", r"<\s*img\b[^>]*\bsrc\s*=\s*[\"'](?P<url>https?://[^\"']+)"),
        ("css @import", r"@import\s+(?:url\()?[\"']?(?P<url>[^\"')]+)"),
        ("remote @font-face", r"@font-face[^}]*url\(\s*[\"']?(?P<url>https?://[^\"')]+)"),
    ]
    for label, pattern in rules:
        for match in re.finditer(pattern, text, flags=re.I | re.S):
            url = match.group("url").strip()
            line = text[: match.start()].count("\n") + 1
            failures.append(
                f"{path}:{line}  external {label}: {url[:80]}\n"
                f"      The page renders offline because it pulls nothing from a third\n"
                f"      party. Inline it instead, or say why the dependency is worth it."
            )


pages = sorted(ROOT.glob("*.html")) + sorted(ROOT.glob("docs/**/*.html"))
if not pages:
    print("No HTML pages found.")
    sys.exit(0)

for page in pages:
    rel = str(page.relative_to(ROOT))
    body = page.read_text(encoding="utf-8")
    check_balance(rel, body)
    check_no_external_subresource(rel, body)

if failures:
    print(f"{len(failures)} finding(s):\n", file=sys.stderr)
    for f in failures:
        print(f"  {f}", file=sys.stderr)
    sys.exit(1)

print(f"{len(pages)} page(s) checked: tags balanced, no external subresource.")
for page in pages:
    print(f"  {page.relative_to(ROOT)}")
