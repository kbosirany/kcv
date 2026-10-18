# Template "banner"

Single column with a navy banner across the top (round photo, name, optional birth name and job
title, contacts in white), then a timeline body: dates in a left column, entries on the right,
skills aligned on the same grid. Source Sans font. Sober and modern, readable at a glance.
Applicant-tracking friendly (pdfLaTeX, real text).

- **Format**: A4, 10 pt, 1 page. The banner is drawn on the page where `\cvheader` is called.
- **Engine**: pdfLaTeX (default); two runs are needed for the banner (latexmk does it).
- **Style file**: `kcv-banner.sty`. A `cv.tex` contains ONLY content and these macros.

## `cv.tex` skeleton

```latex
\documentclass[10pt, a4paper]{article}
\usepackage[french]{babel}
\usepackage{kcv-banner}
\begin{document}
\cvsubname{née NAME}        % optional, before \cvheader
\cvheadline{Job title}      % optional, before \cvheader
\cvheader{photo.jpg}{First LAST}{%      % empty {} = no photo
  \cvlocation{City}\cvsep \cvphone{+33600000000}{06 00 00 00 00}\cvsep \cvmail{a@b.fr}\\[3pt]
  \cvlink{LinkedinIn}{https://...}{handle}\cvsep \cvinfo{Car}{Driving licence}}

\section{Summary}
\cvtext{Two or three sentences.}
\section{Experience}
\cventry{Title}{Subtitle or empty}{Organization}{City, Country}{Dates}
\begin{cvpoints}\item Achievement\end{cvpoints}
\section{Skills}
\cvskill{Category}{item, item}
\end{document}
```

Dates sit in a 3.3 cm column: "Mars 2025 -- Aujourd'hui" is about the longest that fits. Icons:
fontawesome5 names without the `\fa` prefix, star or options.
