"""Check fact sheets, briefs and template presence.

Usage: python scripts/validate.py
"""

from __future__ import annotations

import json
import sys

import yaml
from jsonschema import Draft202012Validator

from kcv import ROOT, TEMPLATES, all_cvs, people


def main() -> int:
    errors: list[str] = []
    schema = json.loads((ROOT / "schemas" / "facts.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    for person in people():
        for required in ("person.yml", "facts.yml", "background"):
            if not (person / required).exists():
                errors.append(f"{person.name}: {required} missing")
        facts = person / "facts.yml"
        if facts.exists():
            data = yaml.safe_load(facts.read_text(encoding="utf-8"))
            for e in validator.iter_errors(data):
                where = "/".join(str(p) for p in e.absolute_path) or "(root)"
                errors.append(f"{facts.relative_to(ROOT)}: {where}: {e.message}")

    try:
        cvs = all_cvs()
    except ValueError as e:
        errors.append(str(e))
        cvs = []
    portfolio_names: dict[str, str] = {}
    for cv in cvs:
        name = f"{cv.person}/{cv.target}"
        template = cv.brief.get("template")
        if not template or not (TEMPLATES / template).is_dir():
            errors.append(f"{name}: template '{template}' not found in templates/")
        if not cv.tex.exists():
            errors.append(f"{name}: cv.tex missing")
        portfolio = cv.brief.get("portfolio")
        if portfolio:
            if portfolio in portfolio_names:
                errors.append(f"{name}: portfolio '{portfolio}' already used by {portfolio_names[portfolio]}")
            portfolio_names[portfolio] = name

    for e in errors:
        print(f"ERROR  {e}")
    print(f"{len(people())} person(s), {len(cvs)} CV(s), {len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
