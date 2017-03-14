# coding: utf-8

print("TP4 - Ex15")

# Consigne :
print("\nComprendre et commenter le code suivant :\n\n")

# Exercice :
import os
os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")

import numpy as np
import matplotlib.pyplot as plt

etudiants = ['Boby', 'Pimousse', 'Arthur']
y_pos = np.arange(len(etudiants))
# Création d'un tableau contenant le nom d'étudiants, et un autre leur 
# attribuant une valeur en ordonnées à chaque élève.

notes = [12,15,14]
plt.axis([0,20,-1,3])
# On fixe des limites pour le graphique (des notes de 0 à 20, les élèves 0, 1
# et 2).

plt.barh(y_pos, notes,height=0.2,  align='center', alpha=0.4)
# Création d'un graphique de barres horizontales, avec différents paramètres.

plt.yticks(y_pos, etudiants)
# Etiquetage du nom des étudiants.

plt.xlabel('Note')
plt.title('Mathématiques')
# étiquetage des axes.

plt.show()
# affichage du graphique.

# Conclusion :
print("\nRésultat :\nmatplotlib.pyplot permet de créer des graphiques "+
    "horizontaux.")