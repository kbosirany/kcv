"""Compile CVs to PDF with latexmk.

Usage:
  python scripts/build.py                 # all CVs
  python scripts/build.py kevin           # all CVs of one person
  python scripts/build.py kevin/general   # a single CV

PDFs are copied to dist/<person>-<target>.pdf, and those meant for the portfolio
("portfolio" field of the brief) also to dist/portfolio/<name>.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys

from kcv import DIST, TEMPLATES, all_cvs


def build(cv) -> bool:
    template = TEMPLATES / cv.brief["template"]
    person_dir = cv.folder.parent.parent
    env = dict(os.environ)
    # TeX looks in the template, then the person's folder (photo), then defaults.
    env["TEXINPUTS"] = os.pathsep.join([str(template) + "//", str(person_dir), ""])
    engine = {"xelatex": "-xelatex", "lualatex": "-lualatex"}.get(cv.brief.get("engine", ""), "-pdf")
    out = cv.folder / "build"
    r = subprocess.run(
        ["latexmk", engine, "-interaction=nonstopmode", "-halt-on-error",
         f"-outdir={out}", "cv.tex"],
        cwd=cv.folder, env=env, capture_output=True, text=True,
    )
    if r.returncode != 0:
        print(r.stdout[-3000:])
        print(f"FAILED  {cv.person}/{cv.target}")
        return False
    DIST.mkdir(exist_ok=True)
    shutil.copy(out / "cv.pdf", DIST / cv.pdf_name)
    if cv.brief.get("portfolio"):
        (DIST / "portfolio").mkdir(exist_ok=True)
        shutil.copy(out / "cv.pdf", DIST / "portfolio" / cv.brief["portfolio"])
    print(f"OK      {cv.person}/{cv.target} -> dist/{cv.pdf_name}")
    return True


def main(filters: list[str]) -> int:
    cvs = [
        cv for cv in all_cvs()
        if not filters or any(f in (cv.person, f"{cv.person}/{cv.target}") for f in filters)
    ]
    if not cvs:
        print("No CV matches.")
        return 1
    failures = [cv for cv in cvs if not build(cv)]
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
