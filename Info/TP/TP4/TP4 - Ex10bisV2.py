# Sur cette version, je me suis fait plaisir.
# Pour une version plus simple, regarder TP4-Ex10bisV2.py

#===============================================================================

# coding: utf-8

print("TP4 - Ex10bisV2")

# Consigne :
print("\nEcrire dans trois fichiers différents les nombres qui commencent "+
    "respectivement par le chiffre 1, 2 et 6 contenus dans le fichier "+
    "Pb_Euler_13.txt.\n\n")

# Exercice :
import os

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "Pb13.txt"

pb = open(nameFile, 'r')
# Ouverture de l'entrée.
n1 = open("n1.txt", 'a')
n2 = open("n2.txt", 'a')
n6 = open("n6.txt", 'a')
# Création/ouverture de la sortie.

lines = pb.readlines()

for l in lines:
    # Pour chaque ligne de pb

    a = l[0]
    # On récupère le premier chiffre.

    if(a == '1'):
        n1.write(l)
    elif(a == '2'):
        n2.write(l)
    elif(a == '6'):
        n6.write(l)
    # On fait du cas par cas pour déterminer si a = 1 ou 2 ou 6, et on 
    # enregistre le nombre dans le fichier correspondant si une des égalités est
    # vérifiée. 

n1.close()
n2.close()
n6.close()

pb.close()

# Conclusion :
print("\nRésultat :\nAvec un fichier d'entrée, on peut chercher plusieurs "+
    "informations différentes et les enregistrerr dans des fichiers séparés.")