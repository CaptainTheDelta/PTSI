# coding: utf-8

print("TP4 - Ex14")

# Consigne :
print("\nAjouter à notre fichier notes.csv une ligne sur laquelle figure la "+
    "moyenne par matière.\n\n")

# Exercice :
import os
os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "notes.csv"

import csv

lignes = []
with open(nameFile) as fichier:
    lignes = [ligne for ligne in csv.reader(fichier)]

def moy(liste):
    """Renvoie la moyenne de liste.

    Args:
        liste (list): Liste d'éléments.

    Return:
        (str): Nombre représentant la moyenne à 0.1 près.
    """
    liste = [eval(x) for x in liste]
    return str(round(sum(liste)/len(liste), 1))


moyennes = ["Moyenne des matières"]

c = len(lignes[0])
# c pour colonne, l pour lignes

for n in range(1,c):
    notes = [note[n] for note in lignes[1:]]
    # Pour chaque ligne, on récupère la note de la c-ième colonne.
    moyennes.append(moy(notes))

with open('test.csv', 'w', newline='') as fichier:
    ecrire = csv.writer(fichier)

    for ligne in lignes:
        ecrire.writerow(ligne)

    ecrire.writerow(moyennes)

# Conclusion :
print("\nRésultat :\nOn peut ajouter des colonnes, mais on peut aussi ajouter "+
    "des lignes.")