# 🧬 Control plane — how this repository participates

> **Status:** 🔄 ACTIVE · **As of:** 2026-09-10
> **Canonical bus:** `Khu-el/Khu-el` → `.neterverse/`
> **Lane:** `LANE_A` · **Visibility:** PUBLIC
> **This is a pointer, not a copy.**

The Neterverse control plane — the shared state two AI runtimes use to coordinate
without losing context or crossing a boundary — lives in **one place**:
`.neterverse/` in `Khu-el/Khu-el`, with its kernel in
`packages/neterverse-kernel`.

---

## 🚫 Do not create a second bus here

If a future agent or contributor needs shared state, registries, an event log,
task leases or a handoff, **they belong in the canonical bus, not in this
repository.** Duplicate masters are the specific failure this document exists to
prevent: two buses disagreeing is worse than one bus nobody reads.

Read `Khu-el/Khu-el` → `.neterverse/README.md` before writing any coordination
state anywhere in this account.

---

## 📍 What this repository is, in control-plane terms

| | |
|---|---|
| **Lane** | `LANE_A` — enterprise and ministry, public-facing |
| **Role** | Public portal for the Neterverse Administration Trust DAO |
| **System of record for** | Its own page content and notice templates. Nothing else |
| **Not the system of record for** | Governance registries, tasks, evidence, or entity records — those sit in Notion, ClickUp and Drive |
| **Deployment** | Static. There is no build step and no backend |

---

## 🛑 The boundary that matters most here

This repository's *purpose* is public-facing material, which means **publication
is one merge away**. The control plane's risk tiers apply directly:

| Tier | Here that means |
|---|---|
| **R0** | Reading, researching, reviewing page content |
| **R1** | Editing a draft, a template, or this documentation |
| **R2** | Preparing public copy that has not been released |
| **R3** | 🛑 Publishing, serving, or sending a notice — **human gate** |
| **R4** | 🛑 Filing, recording, signing, or anything with legal effect — **human gate** |

**Committing a draft is not authorization to publish it.** Preparing a notice
template is R2 and fine. Sending, serving or recording one is R3 or R4 and stops.

---

## ⚖️ The content rule lives elsewhere

The rule that everything here states what the trust *asserts* — a document claim,
never settled external law binding an unrelated party — is already written in
[`CLAUDE.md`](../CLAUDE.md) and Executive OS §6. This file does not restate it,
because a pointer that copies its sources becomes a second source.

One thing to add rather than repeat: the control plane **records** an assertion
status. It never upgrades one.
