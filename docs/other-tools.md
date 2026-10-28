# Using the studio outside Claude

Every skill in this kit is a folder with a `SKILL.md` — the open **Agent Skills** format:
a short header saying what the skill is for and when to use it, then plain Markdown
instructions. Nothing in the instructions depends on one vendor.

That gives you two ways in, depending on the tool.

| Tool reads skill folders? | Use |
|---|---|
| **Yes** | The `skills/` folder as it is |
| **No** | The single-file edition: `python tools/build_single_file.py` → `dist/marketing-studio.md` |

Support for skill folders is changing quickly. **Check your tool's current documentation**
before choosing — the notes below were written in October 2026 and describe how to try it,
not a guarantee.

---

## Claude

- **Claude Code / desktop app:** upload the plugin `.zip` (Plugins → Upload). Type `/start`.
- **Claude.ai:** upload each `skills/<name>` folder as a skill, starting with `house-rules`
  and `start`.

## OpenAI

- **Codex** (and other tools that support Agent Skills): copy the `skills/` folders into the
  skills directory your tool documents.
- **ChatGPT custom GPT or project:** build the single file, upload `dist/marketing-studio.md`
  as a knowledge file, and use this as the instructions:

  > You are a marketing content studio. Your full method is in marketing-studio.md. Begin
  > every conversation with the "start" skill. Read "house-rules" before writing or checking
  > anything. Never state a number unless it comes from a source the user provides or a
  > connected tool, quoted exactly and cited; otherwise write [PROOF POINT NEEDED].

## GitHub Copilot

- If your Copilot setup supports Agent Skills, place the `skills/` folders where its
  documentation says.
- Otherwise, use the single file as a repository or personal instructions file, or attach it
  to a chat.

## Anything else

Any assistant that accepts a document of instructions can run the single-file edition.

---

## How to compare tools fairly

Run the **five tests in the README** in each tool, with the same `house-rules`, and score them
✅ / ❌. They each have one right answer, so you are comparing behaviour, not taste.

Things that commonly differ between tools:

| Behaviour | Why it varies |
|---|---|
| Asks the two opening questions in one message | Some assistants answer immediately rather than asking |
| Declines to add an unsourced number | Depends on how strictly the tool follows long instructions |
| Leaves a customer quote alone | Same |
| Finds your content | Depends entirely on which connectors or files the tool can reach |

Keep a note of the results. It is the most honest way to answer "which tool should we use?"
