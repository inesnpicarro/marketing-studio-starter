---
name: write-copy
description: Writes the copy for a marketing asset once the brief is settled — blog posts, landing pages, emails and nurture sequences, social posts, ads, one-pagers, datasheets, case studies, reports and eBooks, slide-by-slide deck copy. Reads the house rules for voice, the personas skill for the audience, and the material from the voice leader, and fetches every number from your sources at the time of writing. Use after `start` has run the brief, or when someone asks directly for copy for a named asset. Produces copy in the conversation, not a designed file.
---

<!-- Owner function: [Content / Copy lead]. -->

# Write copy

You write the words. Not the layout, not the file — the words, in the company's voice, built
on real material.

---

## Before writing a word

You need four things. If any is missing, get it — from the brief if `start` ran one, from the
requester if not.

| Need | From | If missing |
|---|---|---|
| **The brief** — what, why, angle, channel, date, reviewer | `start` | Ask the four that matter most: what it is, who it's for, the angle, the call to action |
| **The voice** | `house-rules` Part 1 | Write plainly and say which rules you could not apply |
| **The audience** | `personas`, if the reader is a named role | Ask who reads it and what they care about |
| **The material** — the substance | The voice leader: interview, meeting, document, or existing content | **Stop.** Say the asset has no substance yet and offer the options from `start` question 4 |

**Never write substance from nothing.** A competent draft with no real material is the most
expensive output this studio can produce — it looks finished and says nothing.

---

## While writing

**Voice from the first word.** Write in the house voice, avoid the banned words, follow the
conventions. The brand check at the end should confirm, not repair.

**Every number is fetched now.** Statistics, customer results, analyst positions, company
figures — retrieve each one from the sources in `house-rules` Part 2 while writing, use the
exact wording the source uses, and note the source beside it. If nothing returns it, write
`[PROOF POINT NEEDED: what kind of proof would go here]` and keep going.

**Quotes stay as spoken.** Never tidy a person's words into brand voice. If it needs context,
add `[brackets]`. Mark every quote with whether the speaker has agreed to its use.

**The competitor test.** For every headline and key sentence: could a competitor say this,
word for word? If yes, it needs a number, a mechanism or a proof point only you have.

**Lead with the reader's problem, not the product.**

---

## Shapes for common assets

Use the matching shape. Ask the format-specific questions in the right-hand column only if
the brief didn't answer them.

| Asset | Shape | Ask if unknown |
|---|---|---|
| **Blog post** | Headline · one-line standfirst · the problem · what most people get wrong · what works, with proof · what to do next · one CTA | Target search phrase? Length? |
| **Landing page** | Headline · subhead · the problem in the reader's words · 3 outcomes with proof · how it works · social proof · CTA · FAQ | What is the offer? Is it gated? |
| **Email** | Subject line (3 options) · preview text · opening line that earns the next · one idea · one CTA | Which send in a sequence? Plain or designed? |
| **Nurture sequence** | One arc across 3–5 emails, each with a single job: problem · reframe · proof · objection · ask. Timing between sends | Trigger, exit condition, list |
| **Social post** | Hook line · 2–4 short lines · the proof · CTA in the text · 2–3 hashtags. Offer **three variants**: tension · proof · reframe | Company or personal voice? Where does it link? |
| **Ad set** | Per format: headline · body · CTA, within each platform's limits. 2–3 angles to test | Platform, formats, audience |
| **One-pager / datasheet** | Headline outcome · the problem · what it does (3–5 capabilities, each with what it means for the reader) · proof · how to start | Product or solution? Who hands it out? |
| **Case study** | Customer and context · the challenge in their words · why they chose · what changed, with figures **from the customer's approved story** · quote · what's next | Is the customer's consent on file? |
| **Report / eBook / white paper** | Title · executive summary · 4–6 sections, each one argument with evidence · what to do · about us (approved boilerplate) | Gated? Expert named? |
| **Deck** | Slide by slide: headline (the point, as a sentence) · body · speaker notes | How long is the slot? Who presents? |

If the asset isn't listed, say which shape you are borrowing and why.

---

## Deliver

**Copy in the conversation.** Iterate there until the requester is happy. Write nothing to a
file while words are still moving.

Show it with:

```
ASSET          [type] · [channel] · [audience]
SOURCES USED   [each source a figure or claim came from]
GAPS           [every [PROOF POINT NEEDED] and every unconfirmed quote]

[the copy]
```

**When they're happy:** run the `brand-check` skill on it, then hand to `review-and-handoff`.
Say what happens next in one line:

> *"That's the copy. Next: brand check, then review with [reviewer], then a layout for the
> design team to build from."*

---

## Rules

- **No substance, no draft.** Say so and offer the voice-leader options.
- **No number from memory.** Fetched now, exact wording, cited — or a visible gap.
- **No rewritten quotes.**
- **No banned words**, including any inherited from a source document.
- **One call to action.**
- **Copy, not artwork.** Only produce a file when the copy is settled and someone asks for it.
