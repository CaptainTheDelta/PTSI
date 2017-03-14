# coding: utf-8

print("TP4 - Ex18")

# Consigne :
print("\nEcrire une fonction kill_bob() qui demande à l'utilisateur le Nom "+
    "d'un étudiant à retirer de notre fichier notes.csv. (Attention il faut "+
    "que le fichier reste lisible par ligne…)\n\n")

# Exercice :
import os
import csv
import re

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")

nameFile = "notes.csv"

def kill_bob():
    """Demande à l'utilisateur le Nom d'un étudiant à retirer du fichier 
    notes.csv.
    """
    entree = input("Entrez le nom de l'étudiant à retirer : <Nom>\n>>> ")

    while(not re.match("^[A-Z][a-z]+(-[A-Z][a-z])*$",entree)):
        # [A-Z][a-z]+(-[A-Z][a-z])* Vérifie la validité du nom.
        print("Erreur ! Format incorrect !")
        entree = input("Entrez le nom de l'étudiant à retirer : <Nom>\n>>> ")

    lignes = []
    with open(nameFile) as fichier:
        lignes = [ligne for ligne in csv.reader(fichier)]

    n = -1

    for i,name in enumerate([ligne[0] for ligne in lignes]):
        # enumerate renvoie le couple i,liste[i]
        # [ligne[0] for ligne in lignes] permet d'obtenir le premier élément de 
        # chaque ligne, à savoir le nom.
        if(name == entree):
            n = i
            break
    # On détermine si le nom fait partie des noms du fichier.

    l = len(lignes)

    if(n == -1 or n == 0):
    # Si n est égal à -1, c'est qu'il n'y a pas de nom correspondants.
    # Si n est égal à 0, c'est qu'on a séléctionné la ligne d'en tête
        print("La personne demandée n'existe pas dans le fichier.")
    else:
        with open(nameFile, 'w', newline='') as fichier:
            notes = csv.writer(fichier)

            for i in range(l):
                # pour chaque ligne
                if(i == n):
                    continue
                    # si la ligne correspond à celle du nom, on passe.
                
                notes.writerow(lignes[i])

kill_bob()

# Conclusion :
print("\nRésultat :\nOn peut retirer des élément précis du fichier, mais il "+
    "faut pour cela réécrire le fichier entier.")