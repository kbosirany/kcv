# kcv.mum

CV LaTeX organisé par contenu, modèle de mise en page et orientation.

## Construire un CV

Installez une distribution LaTeX incluant `latexmk`, puis lancez :

```powershell
python scripts/build.py --template minimalist --variant academic
```

Le PDF est créé dans `releases/`. Pour ajouter une version, complétez les fichiers de `data/` et le fichier `variants/<orientation>/content.tex`.

## Structure

- `data/` : informations et rubriques partagées
- `templates/` : mises en page indépendantes du contenu
- `variants/` : sélection et adaptation du contenu par cible
- `metadata/` : catalogue des combinaisons disponibles
- `releases/` : PDF générés (ignorés par Git, sauf `.gitkeep`)
