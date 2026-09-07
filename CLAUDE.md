# 🧭 CLAUDE.md — Khu-el/Neterverse_DAO

**📌 Read `docs/EXECUTIVE_OS.md` first.** It is the controlling operating standard for
research, evidence, visuals, artifacts, and the approval boundary in this account. This
file is the repo-specific layer on top of it.

---

## 🧬 What this repo is

The public-facing hub for the **Neterverse Administration Trust DAO**. Currently three
plain files, no build step, no dependencies:

```
index.html                    Static portal page (inline CSS, dark/gold/emerald palette)
README.md                     Repo + DAO overview, links
Public_Notice_Template.txt    Template for a public notice of ecclesiastical standing
```

**Stack:** hand-written static HTML. There is no framework, bundler, package manager,
test suite, or CI. Do not introduce one without being asked — a static page that loads
everywhere is the current design. If a build step ever becomes necessary, say why first.

To preview: open `index.html` in a browser, or `python3 -m http.server` from the repo root.

## ⚖️ The single most important rule for this repo

This repository contains **legal-theory and jurisdictional claims** — ecclesiastical
standing, private trust capacity, natural/canon law, "no presumed statutory authority
unless by consent." Executive OS §6 governs everything written here:

> **🛡️ Do not treat internal governance, private agreement, ecclesiastical principle,
> maxim, declaration, or private record as automatically binding on an unrelated external
> party or public authority.**

Practically, when drafting, editing, or reviewing content in this repo:

- **✍️ Draft what the trust asserts** — that is legitimate and is what these documents are
  for. Assertion is a `DOCUMENT_CLAIM`, not an `EXTERNALLY_VERIFIED` fact (§14).
- **🚫 Do not upgrade an assertion into a statement of settled external law.** Whether an
  agency, court, or counterparty is bound is a **separate question with separate
  evidence** — usually 🟠 TENTATIVE or ⚪ UNKNOWN absent controlling authority.
- **🔎 Cite real authority or cite nothing.** Never invent a statute, code section, case,
  treaty, or filing reference. §5's source hierarchy applies: enacted law and controlling
  decisions outrank commentary, and forum/social material may *identify* an issue but
  never *establishes* it.
- **🥊 Red-team before publishing (§7).** What would a regulator, court, bank, county
  recorder, or opposing attorney say about this sentence? If the honest answer is "they
  would not accept it," the text should say what the trust asserts — not what everyone
  must accept.
- **⚠️ Nothing here is legal advice**, and content that could function as legal advice to
  a third party should say so.

## 🛑 Approval boundary (§10)

Drafts, templates, page content, and analysis may be prepared freely. **Human-controlled
unless expressly authorized for that exact action:** publishing, filing, recording,
serving or sending any notice, signing, contracting, issuing public statements, or making
representations on the principal's behalf. Preparing a notice template is fine.
**Sending, serving, or recording one is not.**

This matters here more than in most repos: this repo's *purpose* is public-facing
material, so "publish" is one merge away. Committing a draft ≠ authorization to publish it.

## 🔗 Cross-repo consistency (§4)

Trust / estate / lane concepts are also modeled in `Khu-el/Khu-el`
(`packages/governance-core`) and surfaced in its `legacy-estate` app (CCRLT, House of
Ransom, Lane B). **Keep terminology consistent across the three repos, and surface
conflicts rather than silently reconciling them.** The lane distinction matters: this repo
is public-facing, while the estate app is deliberately private Lane B — do not move
content from there to here.

## 🎨 Editing the portal page

`index.html` keeps its inline styles and existing palette (`#1C1C1C` ground, `#D4AF37`
headings, `#50C878` links). Emoji-led section headings (🔗 Links, 📜 Notice) are the
established navigation pattern and match §1 — keep them. Several links are `#` placeholders
marked "coming soon"; **leave them as honest placeholders until a real destination exists**
rather than pointing them somewhere plausible-looking (§1: ❓ UNKNOWN never becomes ✅).
