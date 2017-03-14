# coding: utf-8

print("TP4 - Ex")

# Consigne :
print("\nDans le code suivant insérer plt.grid() avant plt.show() et "+
    "relancer. Ajouter ensuite plt.axhline(color='red') et relancer. Enfin "+
    "insérer plt.legend(['sinus'],loc='upper left')\n\n")

# Exercice :
import matplotlib.pyplot as plt
import numpy as np
from math import pi

x = np.linspace(-2*pi,2*pi,1000)
# Ensemble de x qui vont être pris en paramètres par la fct. (comme un range,
# mais avec des float).

plt.plot(x,np.sin(x))  
# on utilise la fonction sinus du module Numpy

plt.ylabel('La fonction sinus')
plt.xlabel("L'axe des abcisses")
# Ajoute des labels pour les axes.

plt.grid()
# Affiche la grille.

plt.axhline(color='red')
# Colore l'axe des abscisses en rouge.

plt.legend(['sinus'],loc='upper left')
# Indique en haut à gauche la légende 'sinus'.

plt.show()
# Affiche le graphe

# Conclusion :
print("\nRésultat :\nLe module numpy permet de faire du calcul scientifique, "+
    "le module matplotlib.pyplot permet de faire des graphiques.")