# coding: utf-8

print("TP4 - Ex05")

# Consigne :
print("\nEcrire une fonction graphe_puissance, qui prend comme argument un "+
    "entier n, une lettre correspondant à une couleur et des bornes et qui "+
    "renvoie le graphe (1000 points) de la fonction x -> x^n de la bonne "+
    "couleur, dans la fenêtre définie par les bornes.\n\n")

# Exercice :
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)

def graphe_puissance(n,l,coords):
    """Fonction qui affiche le graphe de x^n, de la couleur l et dans un cadre
    fixé par coords.

    Args:
        n (int): Puissance de la courbe.
        l (char): Lettre désignant la couleur de la courbe.
        coords (list): Liste d'entiers représentant les valeur minimales et 
            maximales de l'axe des ordonées et des abscisses.
    """
    xmin,xmax,ymin,ymax = coords
    x = np.linspace(xmin,xmax,1000)
    
    plt.grid()
    plt.axis([xmin,xmax,ymin,ymax])
    plt.plot(x,[a**n for a in x],l)
    plt.show()


graphe_puissance(2,'r',[-2,2,0,4])

# Conclusion :
print("\nRésultat :\nLa fonction permet de simplifier la création de graphes.")