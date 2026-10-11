"""Outils communs : découverte des personnes, des CV et lecture des briefs."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
PEOPLE = RACINE / "people"
TEMPLATES = RACINE / "templates"
DIST = RACINE / "dist"

_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


@dataclass
class Cv:
    personne: str
    cible: str
    dossier: Path
    brief: dict

    @property
    def tex(self) -> Path:
        return self.dossier / "cv.tex"

    @property
    def nom_pdf(self) -> str:
        return f"{self.personne}-{self.cible}.pdf"


def lire_brief(chemin: Path) -> dict:
    """Lit l'en-tête YAML (entre deux lignes ---) d'un brief.md."""
    texte = chemin.read_text(encoding="utf-8")
    m = _FRONT_MATTER.match(texte)
    if not m:
        raise ValueError(f"{chemin} : en-tête YAML manquant (bloc --- ... ---)")
    return yaml.safe_load(m.group(1)) or {}


def personnes() -> list[Path]:
    return sorted(p for p in PEOPLE.iterdir() if p.is_dir() and not p.name.startswith("_"))


def tous_les_cv() -> list[Cv]:
    cvs = []
    for personne in personnes():
        for dossier in sorted((personne / "cvs").glob("*/")):
            brief = dossier / "brief.md"
            if not brief.exists():
                raise ValueError(f"{dossier} : brief.md manquant")
            cvs.append(Cv(personne.name, dossier.name, dossier, lire_brief(brief)))
    return cvs
