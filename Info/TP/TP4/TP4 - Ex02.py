# coding: utf-8

print("TP4 - Ex02")

# Consigne :
print("\nEssayer de comprendre comment on peut superposer des graphes, en "+
    "exécutant les commandes :\n\n")

# Exercice :
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)

p1 = plt.plot(x,np.sin(x),marker='o')
p2 = plt.plot(x,np.cos(x),marker='v')
# Pour ajouter un graphe, il suffit de refaire plot.
# marker indique la forme des points qui vont être affichés.

plt.title("Fonctions trigonometriques")  # Problemes avec accents (plot_directive) !
# Affiche un titre à l'ensemble.

plt.legend(['sinus', 'cosinus'], loc='upper left')
plt.show()

# Conclusion :
print("\nRésultat :\nPour supperposer des courbes, il suffit de les ajouter à"+
    "l'aide d'un nouvel appel de la fonction plot.")