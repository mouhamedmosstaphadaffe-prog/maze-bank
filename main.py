import time

from Class import *
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
console = Console()
from rich.text import Text

def main():
    name = None
    try:

        maze_banke = Text("\n🏦🪙 M A Z E  B A N K 🪙🏦\n\n", style="bold italic gold1", justify="center")
        maze_banke.append("Votre confiance, notre priorité")
        console.print(Panel(maze_banke, expand=True, box=box.DOUBLE, border_style="purple"), justify="center")
        time.sleep(0.2)
        while True:

            TABLE = Table(box=box.ROUNDED,border_style="bright_cyan")
            TABLE.add_column("N°",style="bold italic bright_yellow", justify="left")
            TABLE.add_column("Que souhaitez vous faire ?",style="bold italic bright_white",justify="left")
            TABLE.add_row("1","Créer un compte")
            TABLE.add_row("2","Se connecter")
            TABLE.add_row("3","Quitter")
            console.print(TABLE)
            choice = console.input("[bold italic bright_magenta]Votre choix -> [/bold italic bright_magenta]")
            _1_ou_2 = ["1", "2"]
            ma_bank = Bank()
            if choice in _1_ou_2:
                name = ma_bank.create_account() if choice == "1" else ma_bank.se_connecter()
                utilisateur = Utilisateur(name_use=name)

                while True:
                    text = Text("M E N U   P R I N C I P A L", style="bold gold1")
                    table = Table(title=text, title_justify="center", box=box.ROUNDED, border_style="purple")
                    table.add_column("N°", style="bold italic bright_yellow", justify="left")
                    table.add_column("C H O I X ", style="bold italic bright_white", justify="left")
                    table.add_row("1", "💰 Consulter mon solde")
                    table.add_row("2", "📥 Déposer de l'argent")
                    table.add_row("3", "🛒 Découvrir la boutique de Maze Bank")
                    table.add_row("4", "🔄 Transférer de l'argent")
                    table.add_row("5", "📜 Consulter mon historique")
                    table.add_row("6", "🚪 Se déconnecter")
                    console.print(table)
                    reponse = console.input("[bold italic blue]Votre choix -> [/bold italic blue]")

                    if reponse == "1":
                        utilisateur.solde()
                        time.sleep(0.5)
                    elif reponse == "2":
                        utilisateur.depot()
                        time.sleep(0.2)
                    elif reponse == "3":
                        utilisateur.buy()
                    elif reponse == "4":
                        utilisateur.transfert()
                        time.sleep(0.5)
                    elif reponse == "5":
                        utilisateur.story()

                    elif reponse == "6":
                        console.print("Merci de votre confience\nÀ la prochaine 👋👋",style="bold italic chartreuse3")
                        remove_user(name)
                        name = None
                        break
                    else:
                        console.print("Entrer un choix valide",style="bold italic red")
                        time.sleep(1)
                        console.clear()


            elif choice == "3":
                console.print("Au revoir 👋👋", style="bold italic red")
                break
            else:
                console.print("--" * 50, style="bold gray93")
                console.print("Veuillez choisir 1, 2 ou 3.")
                continue
    except KeyboardInterrupt:
        console.print("Au revoir 👋👋", style="bold italic red")
        if name:
            remove_user(name)
if __name__ == "__main__":
    main()
