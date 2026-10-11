"""Compile les CV en PDF avec latexmk.

Usage :
  python scripts/compiler.py                 # tous les CV
  python scripts/compiler.py kevin           # tous les CV d'une personne
  python scripts/compiler.py kevin/general   # un seul CV

Les PDF sont copiés dans dist/<personne>-<cible>.pdf, et ceux destinés au
portfolio (champ « portfolio » du brief) aussi dans dist/portfolio/<nom>.pdf.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys

from kcv import DIST, TEMPLATES, tous_les_cv


def compiler(cv) -> bool:
    template = TEMPLATES / cv.brief["template"]
    personne = cv.dossier.parent.parent
    env = dict(os.environ)
    # Le template, puis le dossier de la personne (photo), puis les chemins TeX par défaut.
    env["TEXINPUTS"] = os.pathsep.join([str(template) + "//", str(personne), ""])
    moteur = {"xelatex": "-xelatex", "lualatex": "-lualatex"}.get(cv.brief.get("moteur", ""), "-pdf")
    build = cv.dossier / "build"
    r = subprocess.run(
        ["latexmk", moteur, "-interaction=nonstopmode", "-halt-on-error",
         f"-outdir={build}", "cv.tex"],
        cwd=cv.dossier, env=env, capture_output=True, text=True,
    )
    if r.returncode != 0:
        print(r.stdout[-3000:])
        print(f"ÉCHEC  {cv.personne}/{cv.cible}")
        return False
    DIST.mkdir(exist_ok=True)
    shutil.copy(build / "cv.pdf", DIST / cv.nom_pdf)
    if cv.brief.get("portfolio"):
        (DIST / "portfolio").mkdir(exist_ok=True)
        shutil.copy(build / "cv.pdf", DIST / "portfolio" / cv.brief["portfolio"])
    print(f"OK     {cv.personne}/{cv.cible} -> dist/{cv.nom_pdf}")
    return True


def main(filtres: list[str]) -> int:
    cvs = [
        cv for cv in tous_les_cv()
        if not filtres or any(f in (cv.personne, f"{cv.personne}/{cv.cible}") for f in filtres)
    ]
    if not cvs:
        print("Aucun CV ne correspond.")
        return 1
    echecs = [cv for cv in cvs if not compiler(cv)]
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
