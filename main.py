# Importe les fonctions de gestion des fichiers
from modules.gestion_fichiers import (
    ajouter_fichier,
    lister_fichiers,
    lire_fichier,
    supprimer_fichier
)

# Permet de cacher le mot de passe lorsqu'on le tape
import getpass

# Permet d'enregistrer la date et l'heure dans les logs
from datetime import datetime


# Mot de passe du coffre-fort
MOT_DE_PASSE = "1234"

# Nombre maximum d'essais autorisés
MAX_TENTATIVES = 3


# Enregistre les actions dans le fichier logs.txt
def log_action(message):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")


# Variables de contrôle
tentatives = 0
acces = False


# Vérification du mot de passe
while tentatives < MAX_TENTATIVES:

    password = getpass.getpass("🔒 Mot de passe : ")

    if password == MOT_DE_PASSE:
        print("✅ Accès autorisé")
        log_action("Accès réussi au coffre")
        acces = True
        break

    else:
        tentatives += 1
        print("❌ Mauvais mot de passe")
        log_action(f"Tentative échouée ({tentatives})")


# Si les 3 essais sont utilisés, le programme s'arrête
if not acces:
    print("🚫 Coffre verrouillé")
    log_action("Coffre verrouillé après 3 essais")
    exit()


# Menu principal du coffre-fort
while True:

    print("\n🔒 Mini Coffre-Fort")
    print("1 - Ajouter un fichier")
    print("2 - Lister les fichiers")
    print("3 - Lire un fichier")
    print("4 - Supprimer un fichier")
    print("5 - Quitter")

    choix = input("Choix : ")

    if choix == "1":
        ajouter_fichier()

    elif choix == "2":
        lister_fichiers()

    elif choix == "3":
        lire_fichier()

    elif choix == "4":
        supprimer_fichier()

    elif choix == "5":
        print("👋 Fin du programme")
        break

    else:
        print("❌ Choix invalide")