
import getpass
import hashlib
import secrets
import hmac
import json
import os

from datetime import datetime

from modules.gestion_fichiers import (
    ajouter_fichier,
    lister_fichiers,
    lire_fichier,
    supprimer_fichier
)


# Configuration
FICHIER_MOT_DE_PASSE = "mot_de_passe.json"
MAX_TENTATIVES = 3
ITERATIONS = 600_000


# Enregistre les actions dans les logs
def log_action(message):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")


# Crée et enregistre le mot de passe
def creer_mot_de_passe():

    print("\n🔐 Première utilisation : crée ton mot de passe.")

    while True:
        mot_de_passe = getpass.getpass("Nouveau mot de passe : ")
        confirmation = getpass.getpass("Confirme ton mot de passe : ")

        if len(mot_de_passe) < 8:
            print("❌ Le mot de passe doit contenir au moins 8 caractères.")
            continue

        if mot_de_passe != confirmation:
            print("❌ Les deux mots de passe ne correspondent pas.")
            continue

        sel = secrets.token_bytes(16)

        empreinte = hashlib.pbkdf2_hmac(
            "sha256",
            mot_de_passe.encode("utf-8"),
            sel,
            ITERATIONS
        )

        donnees = {
            "sel": sel.hex(),
            "empreinte": empreinte.hex()
        }

        with open(FICHIER_MOT_DE_PASSE, "w", encoding="utf-8") as f:
            json.dump(donnees, f)

        print("✅ Mot de passe enregistré.")
        log_action("Mot de passe créé")
        return True


# Vérifie le mot de passe
def verifier_mot_de_passe(mot_de_passe):

    with open(FICHIER_MOT_DE_PASSE, "r", encoding="utf-8") as f:
        donnees = json.load(f)

    sel = bytes.fromhex(donnees["sel"])
    empreinte_enregistree = bytes.fromhex(donnees["empreinte"])

    nouvelle_empreinte = hashlib.pbkdf2_hmac(
        "sha256",
        mot_de_passe.encode("utf-8"),
        sel,
        ITERATIONS
    )

    return hmac.compare_digest(
        nouvelle_empreinte,
        empreinte_enregistree
    )


# Vérification de l'accès au coffre
def authentification():

    if not os.path.exists(FICHIER_MOT_DE_PASSE):
        creer_mot_de_passe()

    tentatives = 0

    while tentatives < MAX_TENTATIVES:

        password = getpass.getpass("\n🔒 Mot de passe : ")

        if verifier_mot_de_passe(password):
            print("✅ Accès autorisé")
            log_action("Accès réussi au coffre")
            return True

        tentatives += 1
        print("❌ Mauvais mot de passe")
        log_action(f"Tentative échouée ({tentatives})")

    print("🚫 Coffre verrouillé")
    log_action("Coffre verrouillé après 3 essais")
    return False


# Programme principal
def main():

    if not authentification():
        return

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


if __name__ == "__main__":
    main()
