---
name: new-person
description: Create the people/<slug>/ skeleton for a new person (empty narrative, empty fact sheet, brief). Use when asked to add someone (e.g. kelly, vivi).
---

# New person

1. Ask for the folder name (lowercase, no accents) if not given, plus the display name and the
   contact details needed for the CV header.
2. Copy the structure of `people/mum/`: `person.yml`, `background/` (README, `education.md`,
   `experience.md`, `other.md` with `> À compléter :` questions, in French), an empty `facts.yml`,
   `cvs/general/brief.md`.
3. Empty any content specific to mum; carry nothing over from her.
4. Do not put `portfolio:` in the brief. Add the photo if provided.
5. Run `python scripts/validate.py`.
6. Tell the person which `background/` files to fill in first.
