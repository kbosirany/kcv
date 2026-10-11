---
name: generer-cv
description: Produit un CV ciblé (brief.md + cv.tex) pour une personne à partir de sa fiche de faits et d'un template, puis le compile. À utiliser quand on demande un CV pour un poste ou une cible.
---

# Générer un CV

1. Identifier la personne, la cible (poste, secteur), la langue, la longueur, le template
   (défaut : `template_defaut` de `personne.yml`). Poser la question s'il manque l'essentiel.
2. Créer `people/<slug>/cvs/<cible>/brief.md` : en-tête YAML (`template`, `langue`) puis cible,
   longueur, sections, notes.
3. Lire `faits.yml` et `templates/<template>/TEMPLATE.md`. Sélectionner et reformuler les points qui
   comptent pour la cible, sans rien ajouter qui ne soit dans les faits.
4. Écrire `cv.tex` avec les macros du template uniquement.
5. `python scripts/valider.py` puis `python scripts/compiler.py <slug>/<cible>`. Ouvrir le PDF
   (`pdftoppm -png`) et vérifier la longueur et la mise en page.
6. Résumer en quelques lignes ce qui a été mis en avant ou écarté. Mentionner les lignes
   `a_completer` qui auraient renforcé le CV.
