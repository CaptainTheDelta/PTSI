# coding: utf-8

print("TP4 - Ex13")

# Consigne :
print("\nQue fait le code suivant ? Le recopier et le commenter. Puis le "+
    "lancer pour vérifier.\n\n")

# Exercice :
import os
os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")

import csv

lignes = []

with open('test.csv') as fichier:
    lignes = [ligne for ligne in csv.reader(fichier)]
# Création d'un tableau contenant chaque ligne du fichier test.csv

def moy(liste):
    """Renvoie la moyenne de liste.

    Args:
        liste (list): Liste d'éléments.

    Return:
        (str): Nombre représentant la moyenne à 0.1 près.
    """
    liste = [eval(x) for x in liste]
    # Transformation des données de la liste : de texte ils deviennent nombres.
    
    return str(round(sum(liste)/len(liste), 1))
    # Renvoie en texte l'arrondi à 10**-1 de la moyenne.


lignes[0].append('Moyennes')
# On ajoute à la première ligne Moyennes, comme on travaille avec des csv, cela
# signifie qu'on veut ajouter une colonne.

for ligne in lignes[1:]:
# Pour chaque ligne sauf la première (qui contient les noms des colonnes) :
    
    ligne.append(moy(ligne[1:]))
    # On ajoute à la fin (~ dans la dernière colonne) la moyenne des notes.
    # On commence à partir du second élément, car le premier est le nom.

with open('test.csv', 'w', newline='') as fichier:
    ecrire = csv.writer(fichier)
    for ligne in lignes:
        ecrire.writerow(ligne)
# On enregistre le fichier en format csv.

# Conclusion :
print("\nRésultat :\nOn a créé une nouvelle colonne contenant la moyenne dans "+
    "le tableau csv.")