# Rules for Claude in kcv

Kevin is French-speaking: talk to him in French. Everything else in the repository (file and
folder names, YAML keys, scripts, documentation, comments, skills) is in English. Only the content
of `people/*/background/*.md` (the narrative) is in French, and the CV text derived from it.
CVs are in French unless the brief says otherwise (`language:`).

## Chain of truth

`background/*.md` (narrative) → `facts.yml` (fact sheet) → `cvs/<target>/cv.tex` (CV).

- Never write in a CV information that is absent from `facts.yml`.
- Never write in `facts.yml` information that is absent from the narrative. If a date, figure or
  tool is missing, do not guess: add it to `open_questions` and ask.
- Do not copy content from one person to another. If an old CV contains doubtful data (for example
  dates that look like another person's), flag it and do not carry it over.
- Never edit the narrative in place of the person, except to add what they just said; the
  narrative is written in the first person, in their words.

## Making a CV

1. Read `person.yml`, `facts.yml`, the brief and `templates/<template>/TEMPLATE.md`.
2. Choose and rephrase what matters for the target: action verbs, quantified results when they are
   in the facts, 1 page by default. Add nothing new.
3. Write `cv.tex` with the template's macros only, then run `python scripts/validate.py` and
   `python scripts/build.py <person>/<target>`, and look at the PDF.

## Files

- `people/<person>/background/`: free narrative. `facts.yml`: validated by
  `schemas/facts.schema.json`.
- A template contains no personal data; a person folder contains no layout.
- Do not commit PDFs or LaTeX build files (`.gitignore`).
- Only briefs containing `portfolio:` are published to the portfolio; never add that line for
  anyone but Kevin without his consent.
- `archive/` is read-only: take inspiration from it, do not modify it.
