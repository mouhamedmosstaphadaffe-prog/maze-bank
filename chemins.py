from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def fichier_data(nom, contenu_initial):
    chemin = DATA_DIR / nom
    if not chemin.exists():
        chemin.write_text(contenu_initial, encoding="utf-8")
    return chemin