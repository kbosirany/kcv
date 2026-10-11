---
name: mettre-a-jour-faits
description: Met à jour people/<slug>/faits.yml à partir du récit parcours/*.md et montre le diff. À utiliser quand le récit a changé ou quand on demande de mettre à jour la fiche.
---

# Mettre à jour la fiche de faits

1. Lire tous les fichiers de `people/<slug>/parcours/` et le `faits.yml` actuel.
2. Mettre à jour `faits.yml` : formations, expériences (réalisations découpées en points courts avec
   `mots_cles`), projets, compétences, langues. Dates au format AAAA-MM, `fin: null` si en cours.
3. Rien d'inventé : chaque champ vient du récit. Ce qui manque va dans `a_completer`.
4. Mettre à jour `mis_a_jour`, puis `python scripts/valider.py`.
5. Montrer le diff en français (ajouts, modifications, ce qui reste à compléter) pour relecture.
