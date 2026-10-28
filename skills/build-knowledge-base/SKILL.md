---
name: build-knowledge-base
description: Sets up the knowledge base the whole studio searches — where your marketing content lives, a folder structure, one naming pattern for every file, an index the AI can read, and a proof-points file where every approved claim sits with its source. Use the first time you set up the studio, when someone says "our content is everywhere", "the AI can't find anything", "how should we name files", or "how do we build a knowledge base without special software". Works on any shared folder or drive. It proposes; a person renames and moves files.
---

<!-- Owner function: [Whoever owns your content library — often marketing operations or content]. -->

# Build the knowledge base

Every other skill in this studio is only as good as what it can find. You do not need a
special product for this. A shared folder works, as long as two things are true:

1. **Everyone can reach it** — the team and the AI.
2. **Every file is named the same way** — so the AI can find, sort and trust it.

This skill gets you there in four steps. It never renames, moves or deletes a file itself. It
hands you the plan; a person does it.

---

## Step 1 — Ask, in one message

Before proposing anything, ask what you need to know. Infer what you can from the conversation
and ask only the rest.

```
┌─ YOUR CONTENT ───────────────────────────────────────────────────┐
 1  Where does your marketing content live today?
      (a shared drive, a document library, a wiki, people's laptops — all of them is a
      fine answer)
 2  What do you make most? (case studies, white papers, decks, emails, social, videos…)
 3  What do you sell? List the products or service lines, as your customers say them.
 4  Who do you sell to? Industries, and the roles that buy.
 5  Which languages do you publish in?
 6  Who will own the knowledge base? (a function, not a person)
└──────────────────────────────────────────────────────────────────┘
```

If a folder or drive is connected, offer to look at it first: *"I can list what's there and
propose the structure from what you already have. Shall I?"* Reading is fine. Changing
anything is not.

---

## Step 2 — Propose the structure

Keep it shallow. Two levels is plenty; people stop filing past three.

```
Knowledge base/
  01 Products/           one folder per product or service line
  02 Proof/              case studies, quotes, analyst reports, the proof-points file
  03 Campaigns/          one folder per campaign, named like the files
  04 Brand/              brand system, templates, boilerplate, logos
  05 Audiences/          personas, ICP cards, industry notes
  99 Archive/            anything older than [24] months or retired
```

Adapt the folders to what they told you in Step 1. Say why each one exists in one line.

---

## Step 3 — One naming pattern for every file

This is the part that makes the AI work. Propose one pattern and show three examples using
their own products and content types:

```
[Product]_[Topic]_[AssetType]_[ShortName]_[YYYY-MM]_[LANG]

Example:  Payments_Fraud_CaseStudy_RetailBank_2026-03_EN
Example:  Platform_AI_WhitePaper_DataReadiness_2026-09_EN
Example:  Payments_eInvoicing_Webinar_Slides_2026-06_FR
```

**Rules for the pattern:**
- Product and asset type come from a fixed list you agree once. Write the list down.
- Dates are `YYYY-MM`, so files sort by time.
- No spaces inside a part; underscores between parts.
- A language suffix only when there is more than one language.
- `FINAL`, `v2`, `new` never appear in a name. The date and the folder say which is current.

**If files already exist,** produce a rename plan the owner can work through, not a rename:

| Current name | Proposed name | Folder | Notes |
|---|---|---|---|
| [Case study final v3.pdf] | [Payments_Fraud_CaseStudy_RetailBank_2026-03_EN.pdf] | 02 Proof | [Check the customer still approves being named] |

Offer it as a CSV they can open in a spreadsheet. Start with the 20 files people use most;
perfect is the enemy of done.

---

## Step 4 — Two files the AI reads first

**`_INDEX.md`** at the top of the knowledge base: one row per important file.

| File | What it is | Product | Audience | Date | Public or internal |
|---|---|---|---|---|---|

**`_PROOF-POINTS.md`** in `02 Proof`: every approved claim, word for word, with its source.

| Claim, exactly as approved | Source file | Approved by (function) | Valid until | Public? |
|---|---|---|---|---|

The proof-points file is what stops the AI from inventing numbers. If a claim isn't in it, the
studio writes `[PROOF POINT NEEDED]` instead of guessing.

---

## Then: wire it into the studio

Write what you set up into `house-rules` Part 2 (where the facts live) and Part 3.4 (naming).
Show the exact text to paste. Then suggest one test: *"Ask the studio what you already have on
[their main product]. If it finds the right files, the knowledge base works."*

---

## Rules

- **Read, never change.** Propose names, folders and indexes. A person moves and renames.
- **Never copy a claim into `_PROOF-POINTS.md` from memory.** Only from a file, quoted exactly,
  with the file named.
- **Flag what looks private** (customer contracts, pricing, personal data) and suggest it
  stays out of the knowledge base the AI reads.
- **Keep it boring.** A plain structure that people actually follow beats a clever one.
- **Give it an owner and a rhythm:** once a quarter, archive what's retired and refresh the
  index. Say this at the end.
