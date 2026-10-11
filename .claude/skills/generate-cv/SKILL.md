---
name: generate-cv
description: Produce a targeted CV (brief.md + cv.tex) for a person from their fact sheet and a template, then build it. Use when asked for a CV for a job or a target.
---

# Generate a CV

1. Identify the person, the target (job, sector), the language, the length and the template
   (default: `default_template` in `person.yml`). Ask if the essentials are missing.
2. Create `people/<slug>/cvs/<target>/brief.md`: YAML header (`template`, `language`) then target,
   length, sections, notes.
3. Read `facts.yml` and `templates/<template>/TEMPLATE.md`. Select and rephrase the points that
   matter for the target, adding nothing that is not in the facts.
4. Write `cv.tex` with the template's macros only.
5. Run `python scripts/validate.py` then `python scripts/build.py <slug>/<target>`. Open the PDF
   (`pdftoppm -png`) and check length and layout.
6. Summarize in a few lines (in French) what was emphasized or left out. Mention the
   `open_questions` entries that would have strengthened the CV.
