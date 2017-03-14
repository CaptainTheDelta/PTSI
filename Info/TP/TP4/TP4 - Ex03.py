# coding: utf-8

print("TP4 - Ex03")

# Consigne :
print("\nAvec les fonctions sinus et cosinus. Essayer d'obtenir "+
    "successivement, peu ou prou, les courbes suivantes :\n\n")

# Exercice :
import matplotlib.pyplot as plt
import numpy as np
from math import pi



plt.axis([0,2*pi,-1,1])
# Fixe des limites aux axes.

x = np.linspace(-2*pi,2*pi,1000)

plt.plot(x,np.sin(x),'g')
plt.plot(x,np.cos(x),'b')

plt.show()#-----------



plt.close()
# Supprime les graphes.

plt.axis([0,2*pi,-1,1])
plt.plot(x,np.sin(x),'g')
plt.plot(x,np.cos(x),'b')

plt.legend(['sinus', 'cosinus'], loc='upper right')

plt.show()#-----------



plt.close()
plt.axis([0,2*pi,-1,1])
x = np.linspace(-2*pi,2*pi,50)

plt.plot(x,np.cos(x),'r')
plt.plot(x,np.sin(x),'b',marker='o')

plt.legend(['sinus', 'cosinus'], loc='upper right')

plt.show()#-----------



plt.close()
plt.axis([0,2*pi,-1,1])
x = np.linspace(-2*pi,2*pi,50)

plt.plot(x,np.cos(x),'r',linewidth=4.0)
plt.plot(x,np.sin(x),'b',marker='o')

plt.legend(['sinus', 'cosinus'], loc='upper right')

plt.show()#-----------



# Conclusion :
print("\nRésultat :\nLe module matplotlib.pyplot permet de personnaliser ses "+
    "graphes à l'aide de paramètres et de fonctions diverses et variées.")