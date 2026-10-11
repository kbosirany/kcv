"""Shared helpers: discover people and CVs, read briefs."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PEOPLE = ROOT / "people"
TEMPLATES = ROOT / "templates"
DIST = ROOT / "dist"

_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


@dataclass
class Cv:
    person: str
    target: str
    folder: Path
    brief: dict

    @property
    def tex(self) -> Path:
        return self.folder / "cv.tex"

    @property
    def pdf_name(self) -> str:
        return f"{self.person}-{self.target}.pdf"


def read_brief(path: Path) -> dict:
    """Read the YAML front matter (between two --- lines) of a brief.md."""
    text = path.read_text(encoding="utf-8")
    m = _FRONT_MATTER.match(text)
    if not m:
        raise ValueError(f"{path}: missing YAML front matter (--- ... --- block)")
    return yaml.safe_load(m.group(1)) or {}


def people() -> list[Path]:
    return sorted(p for p in PEOPLE.iterdir() if p.is_dir() and not p.name.startswith("_"))


def all_cvs() -> list[Cv]:
    cvs = []
    for person in people():
        for folder in sorted((person / "cvs").glob("*/")):
            brief = folder / "brief.md"
            if not brief.exists():
                raise ValueError(f"{folder}: brief.md missing")
            cvs.append(Cv(person.name, folder.name, folder, read_brief(brief)))
    return cvs
