# coding: utf-8

print("TP4 - Problème Euler n13")

# Consigne :
print("\nWork out the first ten digits of the sum of the following "+
    "one-hundred 50-digit numbers\n\n")

# Exercice :
import os

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "Pb13.txt"
s = 0


fichier = open(nameFile, 'r')

lignes = fichier.readlines()

for l in lignes:
    s += int(l)
    # Ajout à la somme du nombre contenu sur la ligne.

fichier.close()

s = str(s)[:10]
print("First ten digits :",s)

# Conclusion :
print("\nRésultat :\nComme on peut stocker des nombres dans un fichier, on "+
    "les récupérer et les utiliser dans notre programme.")