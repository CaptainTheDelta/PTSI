# coding: utf-8

print("TP4 - Ex11")

# Consigne :
print("\nCopier le fichier notes.csv dans votre répertoire de travail. "+
    "Modifier le chemin du fichier dans le code précédent et essayer de le "+
    "lire.\n\n")

# Exercice :
import os
import csv

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "notes.csv"

with open(nameFile) as fichier:
# Le mot clef with est très pratique : il permet d'ouvrir le fichier, et dès 
# lors que l'on sort du bloc, il le ferme automatiquement !
# Comme ça, plus besoin de penser au close() !!!
    
    lire = csv.reader(fichier, delimiter=';')
    # Ne pas oublier de préciser le délimiteur du csv : avec excel en français,
    # on a le droit au ';', pour éviter toute confusion avec la ',' des nombres.
    
    for ligne in lire:
        print(ligne)
    input()

# Conclusion :
print("\nRésultat :\nOn peut donc récupérer des tableaux sous format csv, pour"+
    " les exploiter plus tard.")