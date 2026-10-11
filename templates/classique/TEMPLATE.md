# Template « classique »

Mise en page historique de Kevin (style RenderCV « classic ») : une colonne, titres
de section soulignés, dates et lieux alignés à droite, photo ronde optionnelle.
Compatible logiciels de recrutement (PDF lisible, pdfLaTeX).

- **Format** : A4, 10 pt, 1 page visée (2 acceptables si le brief le dit).
- **Moteur** : pdfLaTeX (défaut). Autre moteur : `moteur: xelatex` dans le brief.
- **Fichier de style** : `kcv-classique.sty`. Un `cv.tex` ne contient QUE du contenu et
  ces macros, jamais de réglages de mise en page.

## Squelette d'un `cv.tex`

```latex
\documentclass[10pt, a4paper]{article}
\usepackage[french]{babel}
\usepackage{kcv-classique}
\begin{document}
\cvheader{photo.jpg}{Prénom NOM}{%       % photo vide {} = pas de photo
  \cvlieu{Ville}\cvsep \cvmail{a@b.fr}\cvsep \cvtel{+33600000000}{06 00 00 00 00}\cvsep
  \cvlien{LinkedinIn}{https://…}{pseudo}\cvsep \cvinfo{Car}{Permis B}}

\section{Profil}
\cvtexte{Deux ou trois phrases.}

\section{Expériences professionnelles}
\cventree{Intitulé}{Sous-titre ou vide}{Organisation}{Lieu}{Dates}
\begin{cvpoints}
  \item Réalisation
  \begin{itemize}\item Détail\end{itemize}
\end{cvpoints}

\section{Compétences}
\cvcompetence{Catégorie}{élément, élément}
\end{document}
```

Icônes (`\cvlien`, `\cvinfo`) : noms du paquet fontawesome5 sans `\fa` (LinkedinIn, Gitlab,
Github, Orcid, Car, Globe…).

## Ajouter un autre template (Overleaf, etc.)

1. Dossier `templates/<nom>/` avec les fichiers du template tels quels (zip Overleaf décompressé).
2. Un `TEMPLATE.md` qui décrit les sections et macros à utiliser, la longueur visée, le moteur.
3. Dans un brief : `template: <nom>`.

Les fichiers du template et ceux de la personne (photo) sont trouvés par TeX via `TEXINPUTS`,
voir `scripts/compiler.py`.
