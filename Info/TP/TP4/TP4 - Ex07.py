# coding: utf-8

print("TP4 - Ex07")

# Consigne :
print("\nEcrire un programme qui compte le nombre de ligne du fichier "+
    "Pb13.txt.\n\n")

# Exercice :
import os

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "Pb13.txt"

fichier = open(nameFile, 'r')

lignes = fichier.readlines()

fichier.close()

print("Il y a {} lignes dans {}.".format(len(lignes),nameFile))

# Conclusion :
print("\nRésultat :\nEn combinant les bonnes fonctions, on peut obtenir "
    +"facilement le nombre de lignes du fichier Pb13.txt.")