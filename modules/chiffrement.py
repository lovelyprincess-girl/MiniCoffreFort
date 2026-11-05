from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"


def charger_cle():
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError(
            "Clé de chiffrement introuvable. "
            "Génère une nouvelle clé."
        )

    with open(KEY_FILE, "rb") as f:
        key = f.read()

    return Fernet(key)


cipher = charger_cle()


def chiffrer_texte(texte):
    return cipher.encrypt(texte.encode())


def dechiffrer_texte(texte_chiffre):
    return cipher.decrypt(texte_chiffre).decode()