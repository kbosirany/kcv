# Template "sidebar"

Two columns: a tinted sidebar on the left (round photo, contact, short skill lists, interests) and
the main column on the right (name, job title, summary, experience, education). Deep teal accent,
Lato font. Sober and warm, suited to care and social sectors. Applicant-tracking friendly
(pdfLaTeX, real text).

- **Format**: A4, 10 pt, 1 page. The two columns do not balance: the main column sets the length.
- **Engine**: pdfLaTeX (default).
- **Style file**: `kcv-sidebar.sty`. A `cv.tex` contains ONLY content and these macros.

## `cv.tex` skeleton

```latex
\documentclass[10pt, a4paper]{article}
\usepackage[french]{babel}
\usepackage{kcv-sidebar}
\begin{document}
\begin{cvpage}
% sidebar
\cvphoto{photo.jpg}
\sidesection{Contact}
\cvcontact{MapMarker}{City}
\cvcontact{Phone}{06 00 00 00 00}
\cvcontactlink{Envelope}{mailto:a@b.fr}{a@b.fr}
\cvcontactlink{LinkedinIn}{https://...}{handle}
\cvcontact{Car}{Driving licence}
\sidesection{Skills}
\begin{sidelist}\item Skill \item Skill\end{sidelist}

% main column
\cvmain
\cvname{First LAST}
\cvsubname{née NAME}            % optional
\cvheadline{Job title}          % optional
\section{Summary}
\cvtext{Two or three sentences.}
\section{Experience}
\cventry{Title}{Subtitle or empty}{Organization}{City, Country}{Dates}
\begin{cvpoints}\item Achievement\end{cvpoints}
\section{Skills}                % optional, if not in the sidebar
\cvskill{Category}{item, item}
\end{cvpage}
\end{document}
```

Icons (`\cvcontact`): fontawesome5 names without the `\fa` prefix and without star or options
(MapMarker, Phone, Envelope, LinkedinIn, Car, Globe...). Keep sidebar items short: the column is
5.5 cm wide.
