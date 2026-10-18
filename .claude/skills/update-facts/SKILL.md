---
name: update-facts
description: Update people/<slug>/facts.yml from the narrative background/*.md and show the diff. Use when the narrative changed or when asked to update the fact sheet.
---

# Update the fact sheet

1. Read every file in `people/<slug>/background/` and the current `facts.yml`.
2. Update `facts.yml`: education, experience (achievements split into short points with
   `keywords`), projects, skills, languages. Dates are YYYY-MM, `end: null` if ongoing. Values are
   French (CV content); keys are English.
3. Invent nothing: every field comes from the narrative. What is missing goes in `open_questions`.
4. Update `updated`, then run `python scripts/validate.py`.
5. Show the diff to the user in French (additions, changes, what is still to complete) for review.
