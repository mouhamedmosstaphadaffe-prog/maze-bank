
import typer
from datetime import datetime
import time
import getpass

from rich.progress import track
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.table import Table

from save_and_show_users_connect import *
from categories_d_achats import *
from sauvegarde import *
from verification_d_utilisateur import *

etoile = Text()
table = Table()
etoile.append("*"*21, style="green")
etoile.append("*"*10, style="yellow")
etoile.append("*", style="green")
etoile.append("*"*10, style="yellow")
etoile.append("*"*21, style="red")
console = Console()
mot_de_passe = typer.style("mot de passe", fg="green", bold=True)
chiffre = typer.style("chiffres", fg="red", bold=True)
lettre = typer.style("lettres", fg="red", bold=True)
_3 = typer.style("3", fg="blue", bold=True)
_16 = typer.style("16", fg="blue", bold=True)
_moins = typer.style("-", fg="green", bold=True)
_ = typer.style("_", fg="blue", bold=True)
_8 = typer.style("8", fg="blue")
_majuscule = typer.style("majuscule", fg="red")
_minuscule = typer.style("minuscule", fg="red")
caractère_special = typer.style("caractère spécial", fg="red")


class Utilisateur:
    def __init__(self, name_use):
        self.name_use = name_use

    @property
    def montant(self):
        return read_file()[self.name_use]["amount"]

    def solde(self):
        solde = self.montant
        text = Text(justify="center")
        text.append(f"💳  V O T R E  S O L D E", style="bold italic gray93")
        text.append(f"\n{solde:.2f} $", style="bold yellow")
        console.print(Panel(text,border_style="purple", box=box.ROUNDED, expand=False))

    def depot(self):
        while True:
            solde = self.montant
            console.print("--" * 50, style="bold gray93")
            amount = console.input("[bold italic blue]Combien vous voulez deposer: [/bold italic blue]")
            try:
                if float(amount) <= 0:
                    console.print("[red]Erreur: Entrer un montant valide[/red]")
                    continue
                if float(amount) >= 100000:
                    console.print("[red]On se connaît, vous n'avez pas cette somme dans le monde reel 🤣🤣[/red]")
                    continue
                soldee = solde + float(amount)
                if soldee > 1000000000:
                    console.print("[red]limite depassée: votre solde ne peut pas depasser 1.000.000.000 $[/red]")
                    continue


                if soldee <= 1000000000:

                    update_solde(self.name_use, soldee)
                    today = datetime.now()
                    today_nice = today.strftime("%d-%m-%Y %H:%M:%S")

                    add_story(self.name_use, today_nice, "Depôt", amount)
                    console.print("✅Dépôt effectué", style="bold green")
                    console.print("--" * 50, style="bold gray93")

                    break
            except ValueError:
                console.print("[red]Erreur: Entrer un montant valide[/red]")

    def buy(self):
        # Afficher les catégories
        options = Text("""
1. Nourriture
2. Vêtements
3. Sport
4. Électronique
5. Fournitures scolaires
6. Transport
7. Maison
8. Retour
""", style="bold green",justify="left")
        choice = ["1", "2", "3", "4", "5", "6", "7", "8"]
        while True:
            console.clear()
            console.print(Panel(options, title="[bold italic gold1]🛒 M E N U  A C H A T S 🛒[bold italic gold1]", box=box.ROUNDED, border_style="purple"), justify="left")
            reponse = console.input("[bold yellow]Veuillez choisir une option (1-8): [/bold yellow]")
            if reponse not in choice:
                console.print("⛔ Entrer un Chiffre Valide")
                time.sleep(1)

            if reponse == "1":
                nourriture(self.name_use)

            if reponse == "2":
                vetements(self.name_use)
            if reponse == "3":
                sport(self.name_use)
            if reponse == "4":
                electronique(self.name_use)
            if reponse == "5":
                fournitures(self.name_use)
            if reponse == "6":
                transport(self.name_use)
            if reponse == "7":
                maison(self.name_use)
            if reponse == "8":
                console.print("[bold green]Retour au menu principal[/bold green]")
                console.print("--" * 50, style="bold gray93")
                time.sleep(0.5)
                console.clear()
                break

    def story(self):
        console.clear()
        text = Text("historique".upper(), style="bold blue", justify="center")
        console.print(Panel(text, border_style="bold blue1", expand=True))
        while True:

            inpute = Text("1. Consulter l'historique\n2. Quitter\n", style="bold italic red")
            reponse = console.input(inpute)

            if reponse == "1":
                list_of_all_histories = read_file()[self.name_use]["story"]
                table = Table(title="[underline]📜 Historique des actions[/underline]", box=box.ROUNDED,
                              border_style="blue",
                              title_style="bold gold1 italic", expand=True, title_justify="center")
                table.add_column("Date", style="bold cyan1 italic", justify="left")
                table.add_column("Action", style="bold red1 italic", justify="left")
                table.add_column("Montant", style="bold green3 italic", justify="left")
                for history in list_of_all_histories:
                    date, action, montant = history
                    table.add_row(date, action, "- " + montant + " $" if action.startswith(
                        "À") or action.startswith("Achat") else "+ " + montant + " $")
                console.print(table)

            elif reponse == "2":
                console.clear()
                return

            else:
                console.print("[red]Erreur: Entrer un choix valide[/red]")
                continue




    def transfert(self):
        while True:
            user_to_transfert = console.input("[bold gray93]Entrer le nom du destinataire :[/bold gray93] ")
            if user_to_transfert in read_file():
                if user_to_transfert == self.name_use:
                    console.print("--" * 50, style="bold gray93")
                    console.print("\nVous ne pouvez pas effectuer de transfert à vous-même", style="bold blue")
                    console.print("--"*50, style="bold gray93")
                    continue
                solde_destinataire = read_file()[user_to_transfert]["amount"]
                montant_a_envoye = console.input("[bold gray93]Entrer le montant à transferer : [/bold gray93]")

                try:
                    amount = self.montant
                    solde = amount - float(montant_a_envoye)
                    soldee = solde_destinataire + float(montant_a_envoye)
                    if soldee > 1000000000:
                        console.print("--" * 50, style="bold gray93")
                        console.print(f"[red]limite depassée: le solde de [/red][green]{user_to_transfert}[green][red] ne peut pas depasser 1000000000 $[/red]")
                        console.print("--" * 50, style="bold gray93")
                        continue

                    if float(montant_a_envoye) > amount:
                        console.print("[red]Vos n'avez pas assez d'argent [/red]")
                        continue
                    if float(montant_a_envoye) > 0 :
                        solde_user = read_file()[user_to_transfert]["amount"]

                        update_solde(user_to_transfert, soldee)
                        update_solde(self.name_use, solde)
                        for i in track(range(100), description="🔄Transfert..."):
                            time.sleep(0.01)
                        console.clear()
                        console.print(f"[bold orange3]Votre transfert a bien été envoyé à [/bold orange3][bold blue]{user_to_transfert}[/bold blue]")

                        today = datetime.now()
                        today_nice = today.strftime("%d-%m-%Y %H:%M:%S")
                        add_story(self.name_use, today_nice, f"À {user_to_transfert}", montant_a_envoye)
                        add_story(user_to_transfert, today_nice, f"De {self.name_use}", montant_a_envoye)
                        break

                    else:
                        console.print("--" * 50, style="bold gray93")
                        console.print("🫸Entrez en nombre > 0🫷", style="bold italic red")
                        console.print("--" * 50, style="bold gray93")

                        continue
                except ValueError:
                    console.print("Erreur: Ce n'est pas un nombre valide\nRéessayer",style="bold red")
                    continue
            else:
                console.print("--" * 50, style="bold gray93")
                console.print("[bold red]Ce compte n'existe pas\nRéessayer[bold red]")
                console.print("--" * 50, style="bold gray93")
                continue











class Bank:
    def __init__(self):
        self.users = read_file()
        self.user_connecte = read_file_connect()

    def create_account(self):
        while True:
            name_use = console.input("Creer un [bold italic green]nom d'utilisateur : [bold italic green]")
            match_user_name = name_user(name_use)

            if not match_user_name:
                console.print("--" * 50, style="bold gray93")
                print(f"Le nom doit faire {_3} à {_16} caractères : {lettre}, {chiffre}, {_} ou {_moins}, avec au moins 3 {lettre}")
                console.print("--" * 50, style="bold gray93")
                continue

            if name_use in self.users:
                console.print("--" * 50, style="bold gray93")
                console.print("[red]prohibited:Nom utilisé\nRéessayer[/red]")
                console.print("--" * 50, style="bold gray93")

                continue
            break
        while True:
            password = getpass.getpass(f"Créer un {mot_de_passe}: ")
            if not password_user(password):
                console.print("--" * 50, style="bold gray93")
                print(f"le password doit avoir au moins {_8} caracteres,\n une {_majuscule}, une {_minuscule}, un {chiffre} et un {caractère_special}.")
                console.print("--" * 50, style="bold gray93")
                continue

            break
        while True:

            confirme = getpass.getpass(f"Confirmer votre {mot_de_passe}: ")

            if confirme == password:
                for i in track(range(100), description="Création de votre compte..."):
                    time.sleep(0.02)
                console.clear()
                console.print("🎉🎉Création de compte avec succès🎉🎉\n\n", style="bold italic chartreuse3")
                append_user(name_use)
                add_account(name_use, hash_pwd(password),0.0, [])
                self.users = read_file()
                return name_use
                break
            else:
                console.print("--" * 50, style="bold gray93")
                console.print("Entrer le bon mot de passe", style="bold red")
                console.print("--" * 50, style="bold gray93")

    def se_connecter(self):

        while True:
            console.print("--" * 50, style="bold gray93")
            name_use = console.input("Entrer votre [bold italic green]nom[/bold italic green]: ")
            if name_use in self.users:
                password = getpass.getpass(f"Entrer votre {mot_de_passe}: ")
                if verification(password, self.users[name_use]["password"]):

                    for i in track(range(100), description="Récupération de vos informations bancaires...", style="green"):
                        time.sleep(0.02)

                    console.print("[bold chartreuse3]🎉Connection réussie🎉[/bold chartreuse3]")
                    carte_bienvenue = Panel(
                        f"[bold italic gray93]Bonjour [bold italic blue]{name_use}[/bold italic blue] ![/bold italic gray93]\n[bold italic gray93]Heureux de vous retrouver chez MAZE BANK.[/bold italic gray93]",
                        border_style="dark_orange", box=box.ROUNDED
                    )

                    time.sleep(0.5)
                    console.clear()

                    console.print(carte_bienvenue,justify="center")
                    append_user(name_use)
                    return name_use
                    break
                console.print("--" * 50, style="bold gray93")
                console.print(":prohibited:echec du mot de passe", style= "bold red")
                continue
            else:
                console.print(f"[red1 bold]{name_use}[/red1 bold][red] n'existe pas[red]")




