# Importe la bibliothèque qui permet de chiffrer et déchiffrer les données
from cryptography.fernet import Fernet

# Permet de vérifier si un fichier existe
import os


# Nom du fichier qui contient la clé de chiffrement
KEY_FILE = "key.key"


# Charge la clé si elle existe, sinon en crée une nouvelle
def charger_ou_creer_cle():

    # Vérifie si la clé est déjà enregistrée
    if os.path.exists(KEY_FILE):

        # Ouvre le fichier contenant la clé
        with open(KEY_FILE, "rb") as f:
            key = f.read()

    else:

        # Crée une nouvelle clé
        key = Fernet.generate_key()

        # Enregistre la clé dans un fichier
        with open(KEY_FILE, "wb") as f:
            f.write(key)

    # Prépare le système de chiffrement avec cette clé
    return Fernet(key)


# Charge la clé une seule fois au démarrage du programme
cipher = charger_ou_creer_cle()


# Chiffre un texte
def chiffrer_texte(texte):

    return cipher.encrypt(texte.encode())


# Déchiffre un texte
def dechiffrer_texte(texte_chiffre):

    return cipher.decrypt(texte_chiffre).decode()