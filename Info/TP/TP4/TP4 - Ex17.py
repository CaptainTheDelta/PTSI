# coding: utf-8

print("TP4 - Ex17")

# Consigne :
print("\nEcrire une fonction ajout() qui demande à l'utilisateur le nom et les "+
    "notes en mathématiques, physique et informatique d'un nouvel étudiant et "+
    "qui l'ajoute à notre fichiers notes.csv.\n\n")

# Exercice :
import os
import csv
import re

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")

nameFile = "notes.csv"

def ajout():
    """Demande à l’utilisateur le nom et les notes en mathématiques, physique et
    informatique d’un nouvel étudiant, puis l'ajoute à notes.csv.
    """
    entree = input("Nouvelle entrée : <Nom> <Note de math> <Note de physique> "+
        "<Note d'info>\n>>> ")

    while(not re.match("^[A-Z][a-z]+(-[A-Z][a-z])*(( )([01]?[0-9](\.\d{,2})?|20)){3}$",entree)):
        # [A-Z][a-z]+(-[A-Z][a-z])*             Validité du nom. Aaa(-Aaa)
        # (( )([01]?[0-9](\.\d{,2})?|20)){3}    Validité des 3 notes. 0 <= x <= 20, 
        # à 0.01 près au max.
        
        print("Erreur ! Format incorrect !")
        entree = input("Nouvelle entrée : <Nom> <Note de math> <Note de "+
            "physique> <Note d'info>\n>>> ")

    entree = entree.split()
    # Divise le texte en liste, en séparant chaque mot.

    with open(nameFile, 'a', newline='') as fichier:
    # On ouvre en mode 'a', pour ne pas écraser, seulement écrire à la fin.
        
        ecrire = csv.writer(fichier)
        
        ecrire.writerow(entree)
        # On ajoute notre entree aux notes.csv.

ajout()

# Conclusion :
print("\nRésultat :\nOn peut ajouter des données à un fichier sans le lire "+
    "entièrement.")