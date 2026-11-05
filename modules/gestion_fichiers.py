# Permet de travailler avec les fichiers et les dossiers
import os

# Importe les fonctions qui servent à chiffrer et déchiffrer le texte
from modules.chiffrement import chiffrer_texte, dechiffrer_texte

# Nom du dossier où seront enregistrés les fichiers
DOSSIER = "fichiers"


# Ajoute un nouveau fichier dans le coffre-fort
def ajouter_fichier():

    # Demande le nom du fichier
    nom = input("Nom du fichier : ")

    # Demande le contenu du fichier
    contenu = input("Contenu du fichier : ")

    # Crée le chemin complet du fichier
    chemin = os.path.join(DOSSIER, nom)

    # Chiffre le contenu avant de l'enregistrer
    contenu_chiffre = chiffrer_texte(contenu)

    # Enregistre le contenu chiffré dans le fichier
    with open(chemin, "wb") as fichier:
        fichier.write(contenu_chiffre)

    print("✅ Fichier créé et chiffré avec succès !")


# Affiche tous les fichiers présents dans le coffre
def lister_fichiers():

    fichiers = os.listdir(DOSSIER)

    if len(fichiers) == 0:
        print("📂 Aucun fichier trouvé.")

    else:
        print("\n📂 Liste des fichiers :")

        for fichier in fichiers:
            print("-", fichier)


# Lit un fichier puis le déchiffre
def lire_fichier():

    # Demande le nom du fichier à ouvrir
    nom = input("Nom du fichier à lire : ")

    chemin = os.path.join(DOSSIER, nom)

    # Vérifie que le fichier existe
    if not os.path.exists(chemin):
        print("❌ Fichier introuvable")
        return

    # Ouvre le fichier en mode lecture binaire
    with open(chemin, "rb") as fichier:
        contenu_chiffre = fichier.read()

    # Déchiffre le contenu
    contenu = dechiffrer_texte(contenu_chiffre)

    print("\n📄 Contenu du fichier :")
    print(contenu)


# Supprime un fichier du coffre
def supprimer_fichier():

    # Demande le nom du fichier
    nom = input("Nom du fichier à supprimer : ")

    chemin = os.path.join(DOSSIER, nom)

    # Vérifie que le fichier existe
    if os.path.exists(chemin):

        os.remove(chemin)

        print("🗑️ Fichier supprimé avec succès")

    else:
        print("❌ Fichier introuvable")