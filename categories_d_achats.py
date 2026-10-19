import time

import typer
from datetime import datetime

from sauvegarde import *
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.table import Table
from rich import box

from rich.panel import Panel
table = Table()

console = Console()
def nourriture(name_user: str):
    saisi = Text("""
1. Café ........ 300 $            
2. Pain ......... 200 $     
3. Lait ......... 500 $     
4. Riz ......... 1000 $     
5. Viande ...... 2500 $     
6. Retour      
    """, style="bold purple", justify="left")
    
    while True:
        solde = read_file()[name_user]["amount"]
        console.print(Panel(saisi, border_style="gold1", expand=False,title="[bold underline purple]NOURRITURE[/bold underline purple]"))
        reponse = console.input("[bold gold1]Quel produit voulez-vous acheter ? [/bold gold1]")
        produits = {
            "1": ("Café", 300),
            "2": ("Pain", 200),
            "3": ("Lait", 500),
            "4": ("Riz", 1000),
            "5": ("Viande", 2500)
        }
        if reponse in ["1", "2", "3", "4", "5"]:
            nom, prix =produits[reponse]
            if solde < prix:
                console.print("[bold red]Solde insuffisant[/bold red]")
                continue

            soldee = solde - prix
            prixx = str(prix)
            today = datetime.now()
            today_nice = today.strftime("%d-%m-%Y %H:%M:%S")
            add_story(name_user, today_nice, f"Achat: {nom}", prixx)
            update_solde(name_user, soldee)
            console.print(f"[green1]Achat effectué avec succès [/green1]")
            time.sleep(0.5)
            console.clear()
            continue

        elif reponse == "6":
            break
        else:
            console.print("[red]Choix invalide[/red]")




def vetements(name_user: str):
        saisi = Text("""
1. T-shirt ............... 3000 $       
2. Pantalon .............. 7000 $       
3. Chaussures ........... 15000 $       
4. Veste ................ 12000 $       
5. Casquette ............. 2500 $       
6. Chaussettes ........... 1000 $       
7. Retour       
        """, style="bold purple", justify="left")
        while True:
            solde = read_file()[name_user]["amount"]
            console.print(Panel(saisi, border_style="gold1", expand=False,title="[bold underline purple]VÊTEMENTS[/bold underline purple]"))
            reponse = console.input("[bold gold1]Quel produit voulez-vous acheter ? [/bold gold1] ")

            if reponse in ["1", "2", "3", "4", "5", "6"]:
                produits = {
                    "1": ("T-shirt", 3000),
                    "2": ("Pantalon", 7000),
                    "3": ("Chaussures", 15000),
                    "4": ("Veste", 12000),
                    "5": ("Casquette", 2500),
                    "6": ("Chaussettes", 1000)
                }
                nom, prix = produits[reponse]

                if solde < prix:
                    console.print("[bold red]Solde insuffisant[/bold red]")
                    continue

                soldee = solde - prix
                prixx = str(prix)
                today = datetime.now()
                today_nice = today.strftime("%d-%m-%Y %H:%M:%S")
                add_story(name_user, today_nice, f"Achat: {nom}", prixx)

                update_solde(name_user, soldee)
                console.print(f"[green1]Achat effectué avec succès [/green1]")
                time.sleep(0.5)
                console.clear()
                continue

            elif reponse == "7":
                break
            else:
                console.print("[red]Choix invalide[/red]")


def sport(name_user: str):
        saisi = Text("""
1. Ballon ................ 8000 $       
2. Maillot ............... 5000 $       
3. Crampons ............. 20000 $       
4. Protège-tibias ........ 3000 $       
5. Gants de gardien ....... 7000 $      
6. Sac de sport .......... 10000 $      
7. Retour       
        """, style="bold purple", justify="left")
        produits = {
            "1": ("Ballon", 8000),
            "2": ("Maillot", 5000),
            "3": ("Crampons", 20000),
            "4": ("Protège-tibias", 3000),
            "5": ("Gants de gardien", 7000),
            "6": ("Sac de sport", 10000)
        }

        while True:
            solde = read_file()[name_user]["amount"]
            console.print(Panel(saisi, border_style="gold1", expand=False,title="[bold underline purple]SPORT[/bold underline purple]"))
            reponse = console.input("[bold gold1]Quel produit voulez-vous acheter ? [/bold gold1] ")

            if reponse in produits:
                nom, prix = produits[reponse]

                if solde < prix:
                    console.print("[bold red]Solde insuffisant[/bold red]")
                    continue

                soldee = solde - prix
                prixx = str(prix)
                today = datetime.now()
                today_nice = today.strftime("%d-%m-%Y %H:%M:%S")
                add_story(name_user, today_nice, f"Achat: {nom}", prixx)

                update_solde(name_user, soldee)
                console.print(f"[green1]Achat effectué avec succès [/green1]")
                time.sleep(0.5)
                console.clear()
                continue

            elif reponse == "7":
                break
            else:
                console.print("[red]Choix invalide[/red]")

def electronique(name_user: str):
        saisi = Text("""
1. Écouteurs ............. 5000 $       
2. Clavier ............... 8000 $       
3. Souris ................ 4000 $       
4. Téléphone ........... 100000 $
5. Ordinateur .......... 250000 $       
6. Chargeur .............. 3000 $       
7. Retour       
        """, style="bold purple", justify="left")
        produits = {
            "1": ("Écouteurs", 5000),
            "2": ("Clavier", 8000),
            "3": ("Souris", 4000),
            "4": ("Téléphone", 100000),
            "5": ("Ordinateur", 250000),
            "6": ("Chargeur", 3000)
        }

        while True:
            solde = read_file()[name_user]["amount"]
            console.print(Panel(saisi, border_style="gold1", expand=False,title="[bold underline purple]OBJETS ÉLECTRONIQUES[/bold underline purple]"))
            reponse = console.input("[bold gold1]Quel produit voulez-vous acheter ? [/bold gold1] ")

            if reponse in produits:
                nom, prix = produits[reponse]

                if solde < prix:
                    console.print("[bold red]Solde insuffisant[/bold red]")
                    continue

                soldee = solde - prix
                prixx = str(prix)
                today = datetime.now()
                today_nice = today.strftime("%d-%m-%Y %H:%M:%S")
                add_story(name_user, today_nice, f"Achat: {nom}", prixx)

                update_solde(name_user, soldee)
                console.print(f"[green1]Achat effectué avec succès [/green1]")
                time.sleep(0.5)
                console.clear()
                continue

            elif reponse == "7":
                break
            else:
                console.print("[red]Choix invalide[/red]")



def fournitures(name_user: str):
        saisi = Text("""
1. Stylo ................. 200 $        
2. Cahier ................ 500 $        
3. Sac scolaire .......... 8000 $       
4. Livre ................. 4000 $       
5. Règle ................. 300 $        
6. Calculatrice .......... 5000 $       
7. Retour       
        """, style="bold purple", justify="left")
        produits = {
            "1": ("Stylo", 200),
            "2": ("Cahier", 500),
            "3": ("Sac scolaire", 8000),
            "4": ("Livre", 4000),
            "5": ("Règle", 300),
            "6": ("Calculatrice", 5000)
        }

        while True:
            solde = read_file()[name_user]["amount"]
            console.print(Panel(saisi, border_style="gold1", expand=False,title="[bold underline purple]FOURNITURES SCOLAIRES[/bold underline purple]"))
            reponse = console.input("[bold gold1]Quel produit voulez-vous acheter ? [/bold gold1] ")

            if reponse in produits:
                nom, prix = produits[reponse]

                if solde < prix:
                    console.print("[bold red]Solde insuffisant[/bold red]")
                    continue

                soldee = solde - prix
                prixx = str(prix)
                today = datetime.now()
                today_nice = today.strftime("%d-%m-%Y %H:%M:%S")
                add_story(name_user, today_nice, f"Achat: {nom}", prixx)

                update_solde(name_user, soldee)
                console.print(f"[green1]Achat effectué avec succès [/green1]")
                time.sleep(0.5)
                console.clear()
                continue

            elif reponse == "7":
                break
            else:
                console.print("[red]Choix invalide[/red]")



def transport(name_user: str):
        saisi = Text("""
1. Ticket de bus ......... 500 $        
2. Course en taxi ........ 2000 $       
3. Carburant ............. 5000 $       
4. Abonnement de bus .... 15000 $       
5. Location de vélo ...... 1000 $       
6. Retour       
        """, style="bold purple", justify="left")
        produits = {
            "1": ("Ticket de bus", 500),
            "2": ("Course en taxi", 2000),
            "3": ("Carburant", 5000),
            "4": ("Abonnement de bus", 15000),
            "5": ("Location de vélo", 1000)
        }

        while True:
            solde = read_file()[name_user]["amount"]
            console.print(Panel(saisi, border_style="gold1", expand=False,title="[bold underline purple]TRANSPORT[/bold underline purple]"))
            reponse = console.input("[bold gold1]Quel service voulez-vous choisir ? [/bold gold1] ")

            if reponse in produits:
                nom, prix = produits[reponse]

                if solde < prix:
                    console.print("[bold red]Solde insuffisant[/bold red]")
                    continue

                soldee = solde - prix
                prixx = str(prix)
                today = datetime.now()
                today_nice = today.strftime("%d-%m-%Y %H:%M:%S")
                add_story(name_user, today_nice, f"Achat: {nom}", prixx)
                update_solde(name_user, soldee)
                console.print(f"[green1]Achat effectué avec succès [/green1]")
                time.sleep(0.5)
                console.clear()
                continue

            elif reponse == "6":
                break
            else:
                console.print("[red]Choix invalide[/red]")



def maison(name_user: str):
        saisi = Text("""
1. Savon ................. 500 $        
2. Lampe ................. 3000 $       
3. Chaise ................ 10000 $      
4. Ventilateur ........... 20000 $      
5. Seau .................. 1500 $       
6. Balai ................. 1000 $       
7. Matelas ............... 40000 $      
8. Retour       
        """, style="bold purple", justify="left")
        produits = {
            "1": ("Savon", 500),
            "2": ("Lampe", 3000),
            "3": ("Chaise", 10000),
            "4": ("Ventilateur", 20000),
            "5": ("Seau", 1500),
            "6": ("Balai", 1000),
            "7": ("Matelas", 40000)
        }

        while True:
            solde = read_file()[name_user]["amount"]
            console.print(Panel(saisi, border_style="bold gold1", expand=False,title="[bold underline purple]MAISON[/bold underline purple]"))
            reponse = console.input("[bold gold1]Quel produit voulez-vous acheter ?[/bold gold1] ")

            if reponse in produits:
                nom, prix = produits[reponse]

                if solde < prix:
                    console.print("[bold red]Solde insuffisant[/bold red]")
                    continue

                soldee = solde - prix
                prixx = str(prix)
                today = datetime.now()
                today_nice = today.strftime("%d-%m-%Y %H:%M:%S")
                add_story(name_user, today_nice, f"Achat: {nom}", prixx)
                update_solde(name_user, soldee)
                console.print(f"[green1]Achat effectué avec succès [/green1]")
                time.sleep(0.5)
                console.clear()
                continue

            elif reponse == "8":

                break
            else:
                console.print("[red]Choix invalide[/red]")