---
name: review-and-handoff
description: Takes finished copy through approval and into design. Runs the brand check, works out which approvals the asset actually needs, writes approval tasks named as decisions with an approver and a date, freezes the copy once approved, and writes the design request with an imagery brief. Use when someone says "this is ready for review", "who needs to approve this", "send it to design", or when an asset has stalled in approval and nobody knows why.
---

<!-- Owner function: [Marketing operations / Project lead]. -->

# Review and handoff

Two jobs: **get the asset approved**, then **get it built.** Design lays out approved words.
It never fetches facts or rewrites claims.

---

## Part 1 — Approval

### Step 0 — Brand check first

Before any human reads it, hand the copy to the **`brand-check` skill**. Fix everything
blocking and everything marked FIX **before** a reviewer sees it. A reviewer who spends their
pass catching banned words never gets to the question only they can answer: *is this right,
and is it any good?*

Attach the report so the reviewer sees what was already checked.

### Step 1 — Self-check

- [ ] Every number traces to a named source, fetched in this work — none from memory
- [ ] Every quote is confirmed by the person who said it
- [ ] No banned words; conventions from `house-rules` followed
- [ ] **Every open decision written down with an owner and a date**

The last one is what gets skipped. An open question in a document is a note. An open question
with an owner and a date is a decision that will happen.

### Step 2 — Which approvals apply

Not every asset needs every gate. Use `house-rules` Part 3.2 for who; this table for when.

| The asset… | Needs |
|---|---|
| Names a customer, quotes a person, or mentions a competitor | Consent / legal **+** accuracy **+** brand **+** campaign owner |
| Makes a product or technical claim | Accuracy **+** brand **+** campaign owner |
| External, no names, no new claims | Brand **+** campaign owner |
| Internal only | Brand only |
| Reuses already-approved copy unchanged | **None** — cite the earlier approval |

**Paid media always needs consent checked again**, even if the customer is already named on
the website. Consent for one channel isn't consent for another.

### Step 3 — Write the approval tasks

One task per approval. Hand the list to the **`project-setup` skill**, which creates them in the
project tool from `house-rules` — or returns them as a list to paste in, if it isn't connected.

| Field | Rule |
|---|---|
| **Owner** | The **approver**. Never the person who wrote it |
| **Due date** | Always. Default three working days; longer for legal or customer consent — say so up front |
| **Name** | A **decision**, not an activity |

- ❌ *"Present the copy to the brand lead"*
- ✅ *"Approve brand treatment — [asset name]"*

If the writer must present before the approver can decide, that's a **separate task** owned by
the writer, blocking the approval. Two tasks, two owners, one dependency.

```
DECISION NEEDED    [one question, answerable yes or no]
ASSET              [link to the one document]
EVIDENCE           [sources, consent records, earlier approvals]
IF APPROVED        moves to [next approval / frozen]
IF REJECTED        name the specific fix — "not on brand" can't be actioned
DUE                [date]. Silence is not approval.
```

### Step 4 — Track and freeze

Report state per approval, never as a percentage:

```
Consent    ⏳ with legal, due [date]
Accuracy   ✅ approved [date]
Brand      ⛔ waiting on consent
```

**The document is made once, when copy is settled** — in the folder from `house-rules`.
Reviewers comment **in that document**. Never send a reviewer pasted text: it forks the copy,
and the fork is what gets approved.

When every applicable approval is in, **the copy is frozen.** Say so plainly.

### Diagnosing a stalled asset

Check in order — the first is usually the answer:

1. Is the approval owned by the writer? Then no approver is blocked. Reassign it.
2. Does it have a due date? No date, no queue position.
3. Is it named as a decision or an activity? Activities never complete.
4. Are the open questions tracked, or sitting in a document?
5. Is an easy approval waiting on a hard one nobody started? Start the hard one.

---

## Part 2 — Handoff to design

**Only after freeze.**

### Lay it out as intent, not artwork

The marketer can lay out the approved copy with an AI design tool to show how they want it to
look. **That layout is a statement of intent for the design team, who build the real asset.**
We own the direction; design owns the execution. Never ship an AI-made layout as finished
artwork, and never present it as one.

### What the design request carries

```
APPROVED COPY      [link to the frozen document]
APPROVALS          [each one, ✅ and date] · copy frozen [date]
LAYOUT INTENT      [link to the layout, if one was made]
TEMPLATE           [the brand template it should use, if any]

IMAGERY            for each image:
   shows           the subject — not a mood word
   sits            cover · section break · inline
   must not be     e.g. generic office stock
   reference       an existing asset that gets it right
   existing        link any image you already own that would do

DATES              needed by · go-live
LANGUAGES          [if translations follow]
```

**The imagery brief is where rework comes from.** Say what the image shows, not how it should
feel. If usable imagery already exists, link it — most requests don't need new art.

Use the team's existing request form or queue if they have one. Don't create free-form tasks
that bypass it.

---

## Close the loop

Two things happen after the asset ships, and both get forgotten:

1. **The asset goes back into the content library**, named per `house-rules` Part 3.4, with
   its approval record. That is what makes the next brief faster.
2. **Open decisions carried forward** get their own tasks with owners and dates.

---

## Rules

- **Never mark an approval on someone's behalf.**
- **Never send unfrozen copy to design.**
- **Never raise a design request without the approval record.**
- **Never let an open decision live only in a document.**
