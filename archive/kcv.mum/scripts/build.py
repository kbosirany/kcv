#!/usr/bin/env python3
"""Prépare et compile une combinaison de modèle et variante."""
import argparse, shutil, subprocess
from pathlib import Path
root = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(); p.add_argument('--template', default='minimalist'); p.add_argument('--variant', default='academic'); p.add_argument('--prepare-only', action='store_true'); a = p.parse_args()
source, content = root/'templates'/a.template/'cv.tex', root/'variants'/a.variant/'content.tex'
if not source.is_file() or not content.is_file(): raise SystemExit('Modèle ou variante introuvable.')
build = root/'.build'/f'{a.template}-{a.variant}'; build.mkdir(parents=True, exist_ok=True)
shutil.copytree(root/'data', build/'data', dirs_exist_ok=True)
shutil.copytree(root/'variants', build/'variants', dirs_exist_ok=True)
(build/'cv.tex').write_text(source.read_text(encoding='utf-8').replace('VARIANT_CONTENT', content.relative_to(root).as_posix()), encoding='utf-8')
if not a.prepare_only:
    subprocess.run(['latexmk', '-pdf', 'cv.tex'], cwd=build, check=True)
    (root/'releases').mkdir(exist_ok=True)
    shutil.copy2(build/'cv.pdf', root/'releases'/f'cv-{a.variant}-{a.template}.pdf')
