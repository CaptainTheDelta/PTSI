# coding: utf-8

print("TP4 - Ex06")

# Consigne :
print("\nOuvrez le fichier et afficher le contenu de Pb13.txt.\n\n")

# Exercice :
import os
os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
# Ces deux lignes changent le lieu où Python travaille : on se place dans le 
# dossier Ressources.

nameFile = "Pb13.txt"

fichier = open(nameFile, 'r')
# Ouvre le fichier en mode lecture.

chaine = fichier.read()
print(chaine)
# read() renvoie l'ensemble du fichier

# On aurait pu :

#   lignes = fichier.readlines()
#   for l in lignes: print(l)


fichier.close()
# Ferme le fichier.

# Conclusion :
print("\nRésultat :\nOn peut lire exploiter des fichiers avec python !!!")

# read : renvoie l'ensemble du fichier sous forme d'un string.
# readline : renvoie une ligne du fichier sous forme d'un string.
# readlines : renvoie un tableau contenant chaque ligne du tableau.