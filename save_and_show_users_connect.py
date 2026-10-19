import json
from pathlib import Path
from rich.console import Console

console = Console()
DATA_FILE = Path(__file__).parent / "data" / "users_connect.json"
def read_file_connect():
    with open(DATA_FILE, "r") as f:
        return json.load(f)
def write_file(users):
    with open(DATA_FILE, "w") as f:
        return json.dump(users, f, indent=4)
def append_user(name_user):
    get_all_users = read_file_connect()
    get_all_users.append(name_user)
    write_file(get_all_users)
def remove_user(name_user):
    get_all_users = read_file_connect()
    get_all_users.remove(name_user)
    write_file(get_all_users)
def get_all_users_online():
    get_all_users = read_file_connect()
    for i, user in enumerate(get_all_users):
        i += 1
        console.print(f"[bold blue]{i}[/bold blue] {user}")
if __name__ == "__main__":
    get_all_users_online()