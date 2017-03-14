# coding: utf-8

print("TP4 - Ex08")

# Consigne :
print("\nEcrire un programme qui compte le nombre d’occurrence du chiffre 2 "+
    "dans le même fichier.\n\n")

# Exercice :
import os

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "Pb13.txt"
compteur = 0

fichier = open(nameFile, 'r')

lignes = fichier.readlines()

for l in lignes:
# pour chaque ligne :
    for c in l:
    # pour chaque caractère de la ligne :
        f(c == '2'):
            compteur += 1

# On peut aussi faire :

#   data = fichier.read()
#   for c in data:
#       if(c == '2'):
#           compteur += 1

fichier.close()

print("Il y a {} fois le chiffre 2 dans {}.".format(compteur,nameFile))

# Conclusion :
print("\nRésultat :\nOn fait une boucle sur les caractères de chaque ligne, "+
    "et on compte le nombre de 2.")