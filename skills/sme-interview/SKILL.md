---
name: sme-interview
description: Runs the expert interview behind a report, white paper, eBook or thought-leadership piece — finds out what you already know, builds the question set, works from the recording or notes afterwards, extracts claims and quotes with their status, and takes them back to the expert to confirm before anything is written. Use when an asset needs real expertise, when a recorded interview already exists, or when someone asks "what should I ask the engineer?". Answers the voice-leader question; runs before write-copy, not instead of it.
---

<!-- Owner function: [Content]. -->

# Expert interview — the voice leader

The step that makes an asset worth reading. The substance comes from someone who actually
knows the thing. This runs that conversation properly and turns it into material.

---

## Ask this first

Not *"do you want to do an interview?"* — that invites a no. Ask:

> **"Who do you want to be the voice leader for what you're about to build?"**

| They say | Path |
|---|---|
| **A person I want to talk to** | Phase 1 below |
| **A meeting already happened** | The `meeting-source` skill extracts it; come back here at Phase 3 to confirm |
| **Nobody — condense what we have** | `find-assets`, then shape it into something new. A real answer, not a failure |

*"I had a meeting with my manager and I want to create from there"* is a legitimate starting
point. What you may take from it depends on what kind of meeting it was — a strategy call
gives you the angle, not verified facts.

---

## Phase 1 — Before the meeting

### Find out what you already know

The fastest way to waste an expert's hour is to ask what your content library already
answers. Search first (`find-assets`, or the sources in `house-rules` Part 2):

- What has already been published on this
- Which claims are already approved and citable
- **What is missing** — that is what the interview is for

Say so in the question set: *"We already have X and Y. This session is about Z."*

### Build the question set

Ten to fifteen questions with a spine:

| Section | Purpose | Roughly |
|---|---|---|
| Warm-up | What they actually work on, in their words | 1–2 |
| The problem | What customers get wrong; what surprises them | 3–4 |
| The mechanism | How it actually works — the part marketing usually gets slightly wrong | 3–4 |
| Evidence | Numbers, named examples, what they've seen | 2–3 |
| The emotion | What does the person doing this job actually feel? | 1–2 |
| **The contrarian one** | **What does everyone believe about this that is wrong?** | 1 |
| Close | What didn't we ask that we should have? | 1 |

**Never drop the contrarian question.** It is usually where the headline comes from.

**Ask about the emotion; never suggest one.** Get the honest answer and build hooks from it.

**Ask for the mechanism, not the benefit.** How something works is material no competitor can
copy. Agreement that it saves time is a sentence anyone could write.

Send the questions a day ahead.

### Set the meeting up to be usable

- **Record it with transcription on.** No transcript means doing this twice.
- 45 minutes. One interviewer.
- Tell them what it's for, and whether their name will be on it.

---

## Phase 2 — After the meeting

Get the transcript from the meeting tool listed in `house-rules`, or ask the requester to paste
it. **No recording?** Work from notes, and say clearly that nothing is a verbatim quote.

Pull out four things:

1. **Claims** — every factual statement. Mark each `verified` (traceable to a source),
   `needs checking`, or `expert opinion`.
2. **Quotable lines** — sentences that sound like a person. Their actual words; add
   `[context]` in brackets rather than rewriting.
3. **The unexpected thing** — usually the answer to the contrarian question. Often the whole
   asset.
4. **What's still missing** — numbers promised, questions unanswered, a second person to talk to.

**Don't:**
- turn opinion into fact — *"I think most teams underestimate this"* is a view, not a statistic
- turn a gesture into a number — *"we see big reductions"* is not a percentage. Put it on the
  missing list
- smooth their language into brand voice yet. Raw first.

---

## Phase 3 — Confirm with the expert

**Non-negotiable, and the step that gets skipped.** Before anything is written for
publication, send back:

```
WHAT WE TOOK FROM THE SESSION
  [3–5 claims, plainly stated]

QUOTES WE'D LIKE TO USE
  [each exactly as said, with its context]
  → Happy to be quoted by name? Yes / No / Reword

STILL NEED FROM YOU
  [the numbers, the second contact, the thing you said you'd send]

WHAT WE THINK THE ASSET SAYS
  [one paragraph — the argument]
```

The last section matters most. It's where an expert says *"that's not quite what I meant"* —
cheap now, expensive after design. Track it as a task with the expert as owner and a date.

---

## Phase 4 — Hand off

Pass to `write-copy`: confirmed claims with their status, approved quotes with agreed
attribution, the unexpected angle, and what the library already had.

**File the transcript where your content library lives** (house-rules Part 3), named so the
next person finds it. Expert transcripts are some of the richest material a team owns — only
if they can be found.

---

## Rules

- **Search before you write questions.**
- **Never publish a quote the speaker hasn't confirmed.**
- **Never convert a gesture into a number.**
- **Never skip confirmation**, however tight the deadline — and especially when the interview
  was months ago.
- **Keep the contrarian question.**
