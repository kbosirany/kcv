# Template "classic"

Kevin's original layout (RenderCV "classic" style): single column, underlined section titles,
dates and places right-aligned, optional round photo. Applicant-tracking friendly (readable PDF,
pdfLaTeX).

- **Format**: A4, 10 pt, aim for 1 page (2 acceptable if the brief says so).
- **Engine**: pdfLaTeX (default). Another engine: `engine: xelatex` in the brief.
- **Style file**: `kcv-classic.sty`. A `cv.tex` contains ONLY content and these macros, never
  layout settings.

## `cv.tex` skeleton

```latex
\documentclass[10pt, a4paper]{article}
\usepackage[french]{babel}                % language of the CV
\usepackage{kcv-classic}
\begin{document}
\cvheader{photo.jpg}{First LAST}{%        % empty {} = no photo
  \cvlocation{City}\cvsep \cvmail{a@b.fr}\cvsep \cvphone{+33600000000}{06 00 00 00 00}\cvsep
  \cvlink{LinkedinIn}{https://...}{handle}\cvsep \cvinfo{Car}{Driving licence}}

\section{Summary}
\cvtext{Two or three sentences.}

\section{Experience}
\cventry{Title}{Subtitle or empty}{Organization}{Location}{Dates}
\begin{cvpoints}
  \item Achievement
  \begin{itemize}\item Detail\end{itemize}
\end{cvpoints}

\section{Skills}
\cvskill{Category}{item, item}
\end{document}
```

Icons (`\cvlink`, `\cvinfo`): fontawesome5 names without the `\fa` prefix (LinkedinIn, Gitlab,
Github, Orcid, Car, Globe...).

## Adding another template (Overleaf, etc.)

1. Create `templates/<name>/` with the template files as they are (unzipped Overleaf project).
2. Add a `TEMPLATE.md` describing the sections and macros to use, the target length and the engine.
3. In a brief: `template: <name>`.

TeX finds the template files and the person's files (photo) through `TEXINPUTS`, see
`scripts/build.py`.
