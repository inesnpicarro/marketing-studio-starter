# Marketing Studio — starter kit

A marketing content studio for Claude. One front door, a handful of skills that each do one
job well, and a single file where your company's rules live.

You type **`/start`**. It asks which team you're on and what you want to do, then takes you
from idea to approved copy and into design — and never invents a fact on the way.

> This kit contains no company data. It's a working pattern. It becomes yours when you fill in
> one file: `skills/house-rules/SKILL.md`.

---

## The idea in eight lines

1. **One door.** Nobody should need to know which skill to use. `/start` routes.
2. **Two questions first:** which team, and what do you want to do — a campaign, an asset,
   an update, or everyday work.
3. **Everyday work gets an answer, not a form.** *"What do we have on banking?"* is a search,
   not a project.
4. **Skills hold the method. Your sources hold the facts.** Nothing about your products,
   customers or numbers is written into a skill. Every figure is fetched at the moment of
   writing, quoted exactly, cited — or shown as a visible gap.
5. **The voice leader.** Every asset has a source of substance: an expert interview, a
   meeting that already happened, or what you already have. Starting from nothing is allowed,
   but the studio will tell you the result will be generic.
6. **Voice is an input, not a correction.** House rules are read before the first word; the
   brand check confirms rather than repairs.
7. **The checker reports; it never rewrites.** And it never touches a customer's quote.
8. **Copy first, design second.** An AI-made layout is a statement of intent for your
   designers. You own the direction; design owns the execution.

---

## What's inside

Fifteen skills. Each is a folder with a `SKILL.md` — plain Markdown in the open Agent Skills
format, so the same files work in Claude and in other tools that read skills (see
[docs/other-tools.md](docs/other-tools.md)).

| Stage | Skill | What it does |
|---|---|---|
| Set up | **`house-rules`** | **Your rules — the file you edit.** Voice, banned words, conventions, where facts live, who reviews, where files go |
| Set up | `build-knowledge-base` | Where your content lives, one naming pattern, an index and a proof-points file the AI reads first |
| Set up | `brand-system` | Your brand guidelines rewritten as rules the AI follows, plus a design brief to paste anywhere |
| Door | **`start`** | Two questions, the brief, routing |
| Find | `find-assets` | What do we already have on this? Organised for the occasion |
| Concept | `campaign-concept` | Four territories, naming shortlist, named visual motifs, image prompts, do & don't |
| Material | `sme-interview` | The expert interview: questions before, extraction after, confirmation with the expert |
| Material | `meeting-source` | Turns a past meeting into material — and says what you may use |
| Audience | `personas` | Buyers, ICP cards, targeting lists, objections — retrieved from your sources every time |
| Write | `write-copy` | The copy for any common asset, in your voice, on real material |
| Check | `brand-check` | Is this on brand? Findings with the rule and the fix. Never rewrites |
| Plan | `timeline` | Can this go live that week? When must work start? |
| Personalise | **`tailor`** (Cherry, the Red Tailor) | Versions per segment, an opening line per target account, building blocks for whole lists. Same claims, new numbers flagged |
| Approve | `review-and-handoff` | Approvals named as decisions, copy freeze, the design request |
| Track | `project-setup` | Puts the work into your project tool with owners and dates |

Four skills touch other systems — `find-assets`, `meeting-source`, `timeline`,
`project-setup`. They are **patterns**: they use whatever you connect, and when nothing is
connected they say so and ask you to paste the material instead.

Where a tool can run a skill as a separate subagent, `find-assets` and `brand-check` benefit
most — the searching and checking stay out of your conversation and only the answer comes back.

---

## Install

**Claude Code or the Claude desktop app**
Plugins → Upload a plugin → choose the `.zip`. Start a new session. Type `/start`.

**Claude.ai (web)**
Upload each folder in `skills/` as a skill, starting with `house-rules` and `start`.

**Other AI tools (OpenAI, GitHub Copilot, others)**
See [docs/other-tools.md](docs/other-tools.md). Tools that read skill folders use `skills/` as
it is. For the rest, `python tools/build_single_file.py` bundles everything into one file you
can upload as instructions or knowledge.

---

## Make it yours — about thirty minutes

0. **Or let the studio interview you.** Type `/start` the first time and say yes to the set-up: it walks you through your knowledge base (`build-knowledge-base`), your brand (`brand-system`) and your house rules, asking questions as it goes.
1. **Open `skills/house-rules/SKILL.md`.** Replace everything in `[square brackets]`.
   - Part 1 — how you sound: voice, banned words with replacements, CTAs, boilerplate
   - Part 2 — where your facts live: your knowledge base, CRM, competitive tool, drives
   - Part 3 — who and where: teams, reviewers, extra approvals, tools, file naming
2. **Connect what you can** in your AI tool's connector settings — a document library, a
   meeting tool, a project tool. None are required to start.
3. **Give every skill an owner.** Each file opens with a line naming the owning function. One
   function keeps each skill true. Put the names in your own register — people move,
   functions don't.
4. **Run the five tests below.** Then let one team use it for a week and listen.

You don't need to finish house-rules before using the studio. It works with the brackets in
place and tells you every time it meets a rule you haven't written — that's how the file
gets filled in.

---

## Five tests — each has a right answer

| Paste | Right answer |
|---|---|
| *"I need something for the banking event next month."* | Asks team and intent in **one** message, guesses field marketing and asks you to confirm, and treats it as **finding what exists** before making anything |
| *"Fix the typo in the second paragraph of our pricing page."* | Just fixes it. No form, no project |
| *"Write a white paper on supplier onboarding."* (and answer *"not sure"* to the voice leader question) | Tells you plainly it will come out generic and offers an expert interview. Doesn't produce a confident draft from nothing |
| *"Add that customers see an average 300% ROI."* | Checks your sources, can't find it, **declines**, and shows `[PROOF POINT NEEDED]` |
| Paste copy containing a banned word inside a customer quote, and the same word in your own sentence | `brand-check` flags **your** sentence as FIX with the replacement, and the **quote** only as CONSIDER — *choose a different quote or leave it* |

If the last two fail, fix them before anyone else uses the studio. They're the ones that
protect trust.

---

## What this kit is not

- **Not a design tool.** It produces approved copy and a design brief. Your designers build.
- **Not a source of facts.** It is exactly as good as the sources you connect — and honest
  when they're thin.
- **Not finished.** It's a starting shape. Add specialist builders (email, events, paid) as
  your team needs them, and list them in `start`.

---

## Repository layout

```
.claude-plugin/plugin.json   Claude plugin manifest
skills/<name>/SKILL.md       the fifteen skills
docs/other-tools.md          using it with OpenAI, Copilot and others
tools/build_single_file.py   bundles every skill into dist/marketing-studio.md
```

*Shared as a starter pattern. Use it, change it, make it yours.*
