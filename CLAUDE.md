# Règles pour Claude dans kcv

Langue de travail : français (Kevin est francophone). CV en français sauf demande contraire,
indiquée dans `brief.md` (`langue:`).

## Chaîne de vérité

`parcours/*.md` (récit) → `faits.yml` (fiche) → `cvs/<cible>/cv.tex` (CV).

- Ne jamais écrire dans un CV une information absente de `faits.yml`.
- Ne jamais écrire dans `faits.yml` une information absente du récit. Si une date, un chiffre ou
  un outil manque, ne pas deviner : l'ajouter à `a_completer` et poser la question.
- Ne pas copier un contenu d'une personne à l'autre. Si un ancien CV contient une donnée douteuse
  (par exemple des dates qui ressemblent à celles d'une autre personne), la signaler et ne pas
  la reprendre.
- Ne jamais modifier le récit à la place de la personne, sauf pour y ajouter ce qu'elle vient de
  dire ; le récit est écrit à la première personne, dans ses mots.

## Faire un CV

1. Lire `personne.yml`, `faits.yml`, le brief et `templates/<template>/TEMPLATE.md`.
2. Choisir et reformuler ce qui compte pour la cible : verbes d'action, résultats chiffrés quand
   ils sont dans les faits, 1 page par défaut. Ne rien ajouter de nouveau.
3. Écrire `cv.tex` avec les seules macros du template, puis `python scripts/valider.py` et
   `python scripts/compiler.py <personne>/<cible>`, et regarder le PDF.

## Fichiers

- `people/<personne>/parcours/` : récit libre. `faits.yml` : validé par `schemas/faits.schema.json`.
- Un template ne contient aucune donnée personnelle ; une personne ne contient aucune mise en page.
- Ne pas commiter de PDF ni de fichiers de compilation (`.gitignore`).
- Seuls les briefs contenant `portfolio:` sont publiés sur le portfolio ; ne jamais ajouter cette
  ligne pour une autre personne que Kevin sans son accord.
- Le dossier `archive/` est en lecture seule : on s'en inspire, on ne le modifie pas.
