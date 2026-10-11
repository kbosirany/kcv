from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
site = root/'site'; site.mkdir(exist_ok=True)
releases_out = site/'releases'; releases_out.mkdir(exist_ok=True)
pdfs = sorted((root/'releases').glob('*.pdf'))
for p in pdfs:
    shutil.copy2(p, releases_out/p.name)
links = ''.join(f'<li><a href="releases/{p.name}">{p.stem}</a></li>' for p in pdfs) or '<li>Aucun CV disponible.</li>'
(site/'index.html').write_text(f'<!doctype html><meta charset="utf-8"><title>CV</title><h1>CV</h1><ul>{links}</ul>', encoding='utf-8')
