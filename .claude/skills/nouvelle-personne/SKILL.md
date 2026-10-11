---
name: nouvelle-personne
description: Crée le squelette people/<slug>/ pour une nouvelle personne (récit vide, fiche vide, brief). À utiliser quand on demande d'ajouter quelqu'un (ex. kelly, vivi).
---

# Nouvelle personne

1. Demander le prénom ou surnom pour le dossier (minuscules, sans accents) s'il n'est pas donné,
   ainsi que le nom affiché et les coordonnées utiles pour l'en-tête.
2. Copier la structure de `people/mum/` : `personne.yml`, `parcours/` (README, `etudes.md`,
   `experiences.md`, `divers.md` avec des questions `> À compléter :`), `faits.yml` vide,
   `cvs/general/brief.md`.
3. Vider tout contenu propre à mum ; ne rien reprendre de sa personne.
4. Ne pas mettre `portfolio:` dans le brief. Ajouter la photo si elle est fournie.
5. Lancer `python scripts/valider.py`.
6. Dire à la personne quels fichiers `parcours/` remplir en premier.
