# coding: utf-8

print("TP4 - Ex12")

# Consigne :
print("\nUtiliser le code ci-dessus, puis vérifier le résultat en lisant dans "+
    "le fichier.\n\n")

# Exercice :
import os

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "notes.csv"

table = [['Noms', 'Math', 'Physique', 'Info'],['Boby', '12', '14', '15'],['Pimousse', '15', '15', '16']]

import csv

with open('test.csv', 'w', newline='') as fichier:
# si test.csv existait, tout ce qui était dedans sera écrasé, sinon test.csv est
# créé.

# /!\ Ne pas oublier newline='', sans ça, on a le droit à des retours à la ligne
# entre chaque ligne.

    ecrire = csv.writer(fichier)

    for ligne in table:
        ecrire.writerow(ligne) 
        # La méthode writerow écrit ligne par ligne.

    ecrire.writerow(['Arthur', '14', '17', '17'])

# Conclusion :
print("\nRésultat :\nEn fonction du mode d'ouverture, on effectue des actions "+
    "différentes en utilisant la même fonction, writerow. Il faut donc y être "+
    "attentif.\nDe plus, on peut observer que via csv, on peut enregistrer "+
    "facilement des tableaux de données.")