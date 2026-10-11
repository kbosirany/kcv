# kcv

Dépôt unique pour écrire et produire les CV de Kevin et de ses proches.
On décrit son parcours **avec ses mots**, Claude en tire une fiche structurée puis
un CV ciblé, compilé en PDF.

```
récit libre  ──►  fiche de faits  ──►  CV ciblé (PDF)  ──►  portfolio (optionnel)
parcours/*.md      faits.yml           cvs/<cible>/cv.tex    kbosirany/kportfolio
```

## Organisation

```
people/<personne>/
  personne.yml        nom affiché, coordonnées, photo, template par défaut
  parcours/*.md       LE RÉCIT (source de vérité), en texte libre
  faits.yml           fiche structurée, générée par Claude et relue
  photo.jpg
  cvs/<cible>/
    brief.md          poste visé, langue, longueur ; l'en-tête YAML choisit le template
    cv.tex            le CV, écrit par Claude à partir de faits.yml + brief.md
templates/<nom>/      mise en page seule, sans aucune donnée (voir TEMPLATE.md)
schemas/              schéma de faits.yml
scripts/              valider.py, compiler.py
archive/              anciens dépôts (kcv v1, kcv2, kcv.mum), pour référence
.claude/skills/       nouvelle-personne, mettre-a-jour-faits, generer-cv
```

Personnes actuelles : `kevin`, `mum`. À venir : `kelly` (sœur), `vivi` (fiancée).

## Au quotidien

1. **Écrire ou compléter le récit** dans `people/<personne>/parcours/`. Aucun format, aucune
   limite. Les lignes `> À compléter :` indiquent ce qu'il manque.
2. **Demander à Claude** « mets à jour la fiche de <personne> » : il relit le récit, met à jour
   `faits.yml` et montre ce qui a changé. On relit.
3. **Demander un CV** : « CV de <personne> pour <poste>, 1 page ». Claude crée
   `cvs/<cible>/brief.md` et `cv.tex` ; la CI compile et fournit le PDF.

Règle d'or : un CV ne contient que ce qui est dans `faits.yml`, et `faits.yml` ne contient que
ce qui est dans le récit. Rien n'est inventé.

## Ajouter une personne

Demander « crée <prénom> », ou copier `people/mum/` en vidant `parcours/` et `faits.yml`.

## Compiler en local

```sh
pip install -r requirements.txt
python scripts/valider.py                 # fiches de faits, briefs, templates
python scripts/compiler.py                # tous les CV -> dist/
python scripts/compiler.py kevin/general  # un seul
```

Il faut `latexmk`, `texlive-latex-extra`, `texlive-fonts-extra` et `texlive-lang-french`. La CI
(`.github/workflows/build.yml`) fait la même chose à chaque push et pull request ; les PDF sont
dans les artefacts du run. Les PDF ne sont pas commités.

## Lien avec le portfolio

Le portfolio ([kportfolio](https://github.com/kbosirany/kportfolio), site Astro sur GitHub
Pages) affiche une liste de CV décrite dans son `data/cv.yml` et lit les PDF dans `public/cv/`.
kcv est la seule source de ces PDF :

- Un brief qui contient `portfolio: cv-fr.pdf` (en-tête YAML) désigne un CV à publier, sous ce
  nom de fichier ; ce nom doit correspondre à `fichier:` dans `data/cv.yml` du portfolio
  (`cv-fr.pdf`, `cv-en.pdf`). Sans cette ligne, le CV reste privé : c'est le cas de tout ce qui
  n'est pas à Kevin.
- `.github/workflows/portfolio.yml` compile, puis ouvre une pull request sur kportfolio avec les
  PDF dans `public/cv/`. Le déploiement du portfolio reste le sien, et toi tu valides la PR.
- Réglage unique : créer un jeton GitHub limité au dépôt kportfolio (Contents et Pull requests en
  lecture/écriture) et l'enregistrer comme secret `PORTFOLIO_TOKEN` dans kcv. Sans secret, le
  workflow ne fait rien.

Même si kcv devient privé, le portfolio ne dépend pas de kcv à la construction : il reçoit des
PDF dans son propre dépôt. La fiche `faits.yml` de Kevin pourra plus tard alimenter aussi
`data/competences.yml` et `data/projets.yml` du portfolio (même source, plusieurs sorties) ;
non fait pour l'instant, le portfolio étant en construction.

## Confidentialité

Les récits contiennent des données personnelles de proches (adresse, téléphone, parcours).
Recommandation : passer ce dépôt en **privé** (Settings > General > Danger Zone). Les artefacts
de la CI restent alors accessibles aux seuls collaborateurs, et seuls les CV marqués `portfolio`
sortent du dépôt.
