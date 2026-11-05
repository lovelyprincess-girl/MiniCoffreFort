from cryptography.fernet import Fernet

cle = Fernet.generate_key()

with open("key.key", "wb") as fichier:
    fichier.write(cle)

print("Nouvelle clé créée.")