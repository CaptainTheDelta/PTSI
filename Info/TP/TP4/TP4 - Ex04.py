# coding: utf-8

print("TP4 - Ex")

# Consigne :
print("\nTracer sur un même graphique, les courbes des fonctions x -> x^n, "+
    "pour n=1,2,3,5.\n\n")

# Exercice :
import matplotlib.pyplot as plt
import numpy as np

plt.xlim(-10,10)
plt.ylim(-30,30)
# Fixe des limites à l'axe des abscisses, à l'axe des ordonées.


x = np.linspace(-10,10,1000)

for n in range(1,6):
    plt.plot(x,[a ** n for a in x])
    # Ajoute le graphe de x ** n

plt.grid()
plt.show()#-----------

# Conclusion :
print("\nRésultat :\nOn peut afficher plusieurs courbes vai une boucle for.")