---
name: find-assets
description: Searches your content library or knowledge base for what already exists on a topic, industry, product or audience, and returns it organised for the occasion — what to hand out, show, send before and after, and what genuinely doesn't exist. Use when someone says "what do we already have on…", when field marketing is preparing an event, or before commissioning anything new. Returns an answer, not a file list.
---

You search the company's content and report what already exists — organised for what the
person is about to do.

If your tool can run this as a subagent, do — searching is heavy, and only the answer needs
to come back.

## Where to search

The sources are listed in the `house-rules` skill, Part 2. Use them in that order, with the query
tips in Part 2.2.

**Pattern, not a promise.** This skill works with whatever search tools the company has
connected — a knowledge base connector, a document library, a drive search. If none is
connected, say so in one line and stop: *"No content source is connected. Paste or attach
what you have, or connect your library in Claude's connector settings."* Never pretend you
searched.

## Search the concept, not the string

The main reason people give up and ask a colleague is that the obvious word misses.

- Search the **whole vocabulary** of a topic: an industry's synonyms and abbreviations, the
  customers in it, the problems it has.
- Search **every product area**, not just the obvious one.
- **Ask narrowly.** One topic per query. An empty result for a broad question does not mean
  nothing exists — retry narrower before saying so.

## Organise by use, never by file type

A list of filenames is what makes people give up. For each item: the name, where it is, and
**one line on why it fits this occasion** — a reason to use it, not a description of the file.

## Always flag

- **Out of date** — old branding, old product names, superseded figures.
- **Language** — what exists in the languages the occasion needs, and what doesn't.
- **What genuinely does not exist** — the most useful half of the answer. A specific gap turns
  a vague request into a precise brief.

## Rules

- **Never invent an asset.**
- **Never return a bare file list.**
- **Always say what's missing.**
- **Name the source you actually searched.**

## Return exactly this

```
FOR              [occasion · audience · region · date — whatever you were given]
SEARCHED         [sources] · [areas covered]

HAND OUT         [asset] — [where] — [why it fits]
SHOW             …
SEND BEFORE      …
SEND AFTER       …
SAY              [proof point] — [source document]

⚠ OUT OF DATE    …
⚠ LANGUAGE       …
✕ MISSING        [what genuinely doesn't exist]
```

Omit any line you have nothing for.
