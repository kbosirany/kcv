"""Vérifie les fiches de faits, les briefs et la présence des templates.

Usage : python scripts/valider.py
"""

from __future__ import annotations

import json
import sys

import yaml
from jsonschema import Draft202012Validator

from kcv import PEOPLE, RACINE, TEMPLATES, personnes, tous_les_cv


def main() -> int:
    erreurs: list[str] = []
    schema = json.loads((RACINE / "schemas" / "faits.schema.json").read_text(encoding="utf-8"))
    validateur = Draft202012Validator(schema)

    for personne in personnes():
        for requis in ("personne.yml", "faits.yml", "parcours"):
            if not (personne / requis).exists():
                erreurs.append(f"{personne.name} : {requis} manquant")
        faits = personne / "faits.yml"
        if faits.exists():
            donnees = yaml.safe_load(faits.read_text(encoding="utf-8"))
            for e in validateur.iter_errors(donnees):
                chemin = "/".join(str(p) for p in e.absolute_path) or "(racine)"
                erreurs.append(f"{faits.relative_to(RACINE)} : {chemin} : {e.message}")

    try:
        cvs = tous_les_cv()
    except ValueError as e:
        erreurs.append(str(e))
        cvs = []
    noms_portfolio: dict[str, str] = {}
    for cv in cvs:
        nom = f"{cv.personne}/{cv.cible}"
        template = cv.brief.get("template")
        if not template or not (TEMPLATES / template).is_dir():
            erreurs.append(f"{nom} : template « {template} » introuvable dans templates/")
        if not cv.tex.exists():
            erreurs.append(f"{nom} : cv.tex manquant")
        portfolio = cv.brief.get("portfolio")
        if portfolio:
            if portfolio in noms_portfolio:
                erreurs.append(f"{nom} : portfolio « {portfolio} » déjà utilisé par {noms_portfolio[portfolio]}")
            noms_portfolio[portfolio] = nom

    for e in erreurs:
        print(f"ERREUR  {e}")
    print(f"{len(personnes())} personne(s), {len(cvs)} CV, {len(erreurs)} erreur(s).")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
