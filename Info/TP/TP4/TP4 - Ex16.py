# coding: utf-8

print("TP4 - Ex16")

# Consigne :
print("\nTracer un diagramme des notes de physique de nos étudiants contenues "+
    "dans le fichier test.csv (en lisant le fichier bien sûr).\n\n")

# Exercice :
import os
import csv
import numpy as np
import matplotlib.pyplot as plt

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "test.csv"

names = []
notes = []

# N'ayant pas test.csv sous la main, je suppose qu'il est de la forme :
# [['Nom','Note'],['bob',150],...]

with open(nameFile) as fichier:
    csv = csv.reader(fichier)

    for line in csv:
        names += [line[0]]
        notes += [line[1]]
        # On prends les noms et les notes.

names = names[1:]
notes = notes = [eval(note) for note in notes[1:]]
# On élimine la première ligne, et pour les notes, on traduit le texte en
# nombres.

y_pos = np.arange(len(names))

plt.barh(y_pos, notes,height=0.2,  align='center', alpha=0.4)

plt.yticks(y_pos, names)
plt.axis([0,20,-1,len(names)])
plt.xlabel('Note')
plt.title('Physique')

plt.show()

# Conclusion :
print("\nRésultat :\n")