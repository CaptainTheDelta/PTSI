# Sur cette version, je me suis fait plaisir.
# Pour une version plus simple, regarder TP4-Ex10bisV2.py

#===============================================================================

# coding: utf-8

print("TP4 - Ex10bis")

# Consigne :
print("\nEcrire dans trois fichiers différents les nombres qui commencent "+
    "respectivement par le chiffre 1, 2 et 6 contenus dans le fichier "+
    "Pb_Euler_13.txt.\n\n")

# Exercice :
import os

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "Pb13.txt"

n = {}
# Création d'un dictionnaire
pb = open(nameFile, 'r')

for k in ['1','2','6']:
    n[k] = open("n"+k+".txt", 'a')
    # Création dynamique des différents fichiers de sortie.

lines = pb.readlines()

for l in lines:
    # Pour chaque ligne de pb

    a = l[0]
    # On récupère le premier chiffre.

    if(a in ['1','2','6']):
        n[a].write(l)
        # S'il s'agit de l'un des chiffres que l'on cherchait : on l'ajoute au
        # fichier correspondant, contenu dans le dictionnaire.

for k in n:
    n[k].close()
    # On ferme tous les fichiers de sortie.

pb.close()

# Conclusion :
print("\nRésultat :\nAvec un fichier d'entrée, on peut chercher plusieurs "+
    "informations différentes et les enregistrerr dans des fichiers séparés.")