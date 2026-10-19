import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).parent / "data" / "users.json"
def read_file():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def write_file(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        return json.dump(users, f, indent=4, ensure_ascii=False)
def add_account(name_user: str, mot_de_pass: str, solde: float, story: list):
    get_all_users = read_file()
    get_all_users[name_user] = {"password": mot_de_pass,"amount" : solde,"story": story}
    write_file(get_all_users)
def update_solde(name_user : str, solde: float):
    get_all_users = read_file()
    get_all_users[name_user]["amount"] = solde
    write_file(get_all_users)
def add_story(name_user : str, date,action, montant :float):
    get_all_users = read_file()
    story_to_save = (date, action, montant)
    get_all_users[name_user]["story"].append(story_to_save)
    write_file(get_all_users)








