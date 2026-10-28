---
name: brand-system
description: Turns your brand guidelines (a PDF, a deck, a web page, or your designers' past work) into a brand system the AI can read and follow — voice rules, colours with their jobs, type, logo rules, imagery style, layout patterns and a do & don't list — plus a short design brief you can paste into any design or image tool. Use when someone says "make the AI follow our brand", "our designs come out off-brand", "turn our guidelines into something Claude can use", or when setting up the studio. It never invents a colour, font or rule that isn't in your guidelines.
---

<!-- Owner function: [Brand / Design]. -->

# Brand system

Brand guidelines are written for people. A long PDF with mood photos is hard for a model to
follow. This skill rewrites what is already in your guidelines into short, exact rules the AI
reads before it writes or lays anything out.

It adds nothing. Every rule it writes comes from your material, and it points to the page it
came from. Anything your guidelines don't say becomes a question, not a guess.

---

## Step 1 — Gather, in one message

```
┌─ YOUR BRAND ─────────────────────────────────────────────────────┐
 1  Attach or link your brand guidelines (PDF, deck, web page).
 2  Attach 3 to 5 pieces your design team is proud of: these show how
    the rules are actually used.
 3  Any templates people must use? (slides, documents, social tiles)
 4  Who signs off on brand questions? (a function)
└──────────────────────────────────────────────────────────────────┘
```

If they have only part of this, start with what they have and list what's missing at the end.

---

## Step 2 — Write the brand system

Produce one file, `brand-system.md`, in this order. Keep every line short and exact, and add
`(p. 12)` or the file name after each rule so people can check it.

**1. Voice, in rules.** Three to five traits as *we are / which means / we are not*, words we
never use with their replacements, headline case, the one call to action per piece. Paste this
part into `house-rules` Part 1 too.

**2. Colours, with their jobs.** A colour without a job gets used everywhere.

| Name | Hex | Job | Never |
|---|---|---|---|
| [Primary] | [#000000] | [Headlines, primary buttons] | [Body text on dark backgrounds] |

Only hex values that appear in the guidelines. If they give only a name or a print code, write
`[hex needed]`.

**3. Type.** Font families, weights and sizes for title, heading, body and caption. Name the
fallback font for tools that don't have the brand font.

**4. Logo.** Clear space, minimum size, which version on light and on dark, and what you must
never do to it.

**5. Imagery.** What the photos and illustrations look like, in words a model can follow
(subject, light, colour, crop, people or no people), plus what is off-brand. Use the example
pieces to describe what the design team actually does.

**6. Layout patterns.** The three or four layouts the team reuses (title slide, two-column,
quote, data), each described in a line: what goes where.

**7. Do and don't.** Ten lines at most, taken from the guidelines and the examples.

---

## Step 3 — A design brief to paste anywhere

From the brand system, write a short block (under 150 words) someone can paste at the top of a
request in any design or image tool:

```
Brand: [name]. Colours: [primary hex] for headlines, [accent hex] for one highlight only,
[neutral hex] backgrounds. Type: [font] headings, [font] body. Imagery: [one line].
Layout: [one line]. Never: [three things].
```

If the tool can take a file, offer `brand-system.md` itself instead. Where a tool can hold a
design system (colour tokens, fonts, components), suggest loading it there once rather than
pasting every time.

---

## Rules

- **Nothing invented.** No colour, font, rule or example that isn't in their material. A gap
  is written as `[needed: …]` and listed at the end.
- **Cite every rule** to its page or file.
- **A generated layout is a starting point, never final artwork.** Say so whenever the brand
  system is used for layout. Your designers finish it.
- **Flag conflicts.** If the guidelines and the example pieces disagree, show both and ask the
  brand owner which wins.
- **Give it an owner.** The brand function keeps `brand-system.md` true; it changes when the
  guidelines change, not when someone prefers a different blue.

---

## What you hand back

1. `brand-system.md`
2. The paste-anywhere design brief
3. The voice section, ready to paste into `house-rules` Part 1
4. A short list of gaps and conflicts for the brand owner
