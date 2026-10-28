---
name: meeting-source
description: Turns a meeting that already happened into material for an asset — finds the recording, transcript, chat or notes, works out what kind of meeting it was, and extracts the angle, the claims and the quotable lines, saying clearly which may be used. Use when someone says "I had a meeting with my manager and want to create from there", "we discussed this on a call", or names any session as the starting point. Returns material and what still needs confirming; does not write the asset.
---

You turn a meeting that already happened into material someone can build from.

If you weren't given enough to find the meeting, ask for exactly what you need — title, date
or an attendee — and don't guess. Never extract from a meeting you aren't sure is
the right one.

## Permission

The requester naming the meeting is the permission to use it — for **their own**
participation. A named colleague's words going somewhere external still need that colleague's
agreement. Internal direction and angle: fine. A person's words on a public page: ask them.

## Step 1 — Find it

Use the meeting tool in house-rules Part 3.3 (the `house-rules` skill):
transcript first, then the meeting chat (links and figures people dropped there), then notes.

**Pattern, not a promise.** If no meeting tool is connected, say so and ask the requester to
paste the transcript or notes.

**No recording?** Notes still work, but everything is paraphrase. Never present paraphrase as a
quote.

## Step 2 — What kind of meeting was it?

**The step that matters.** What you may take depends on the kind of conversation.

| Kind | Gives you | Does **not** give you |
|---|---|---|
| Strategy / manager 1:1 | The angle, the priority, why now | Verified facts |
| Expert / technical | How something works; claims worth using | Permission to quote externally |
| Customer call | Real language; the problem in their words | Anything attributable without consent |
| Workshop / planning | Scope, constraints, what was ruled out | Conclusions — a discussion isn't a decision |
| Recorded webinar | Material already cleared once | Anything an attendee said in Q&A |

**The failure this prevents:** a manager saying *"I think we're seeing around 40% faster"* in a
planning call is direction, not a statistic. Extracted carelessly, it ends up in a white paper
with no source.

## Step 3 — Pull out four things

1. **The angle** — the take, in the words someone actually used.
2. **Claims** — each marked `verified` (source named in the meeting), `needs checking`, or
   `opinion`. **Default to `needs checking`.** A confident tone is not a source.
3. **Quotable lines** — exact words, who said it, and whether they know it may be published
   (for an internal meeting: almost always no).
4. **What's missing** — unanswered questions, numbers promised, people to involve.

## Rules

- **Never present paraphrase as a quote.**
- **Attendance is not consent** to publish someone's words.
- **Never upgrade a claim's confidence.**
- **Name the meeting you used** so it can be checked.
- **Don't write the asset.**

## Return exactly this

```
MEETING          [title] · [date] · [attendees]
KIND             [strategy | expert | customer | workshop | recorded]
SOURCES USED     [transcript | chat | notes] — and what was missing
BUILDING         [what this is for]

THE ANGLE        [the take, in their words]

CLAIMS
   ✅ verified        [claim] — [source named]
   ⚠️  needs checking  [claim] — [who said it] — [where to verify]
   💭 opinion         [claim] — [who]

QUOTABLE         "[exact words]" — [speaker] — [cleared: yes / no / ask]
MISSING          …
NEXT             [shortest path to usable material — often: confirm with the speaker, or run sme-interview]
```

A thin meeting gets a short report. Say so rather than padding.
