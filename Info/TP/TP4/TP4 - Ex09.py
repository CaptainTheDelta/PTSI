# coding: utf-8

print("TP4 - Ex09")

# Consigne :
print("\nEcrire dans un fichier premiers_1000 les 1000 premiers nombres "+
    "premiers.\n\n")

# Exercice :
def isPrime(n):
    if n in [0,1] or (n != 2 and n % 2 == 0):
        return False
    for k in range(3,int(n**(1/2))+1,2):
        if n % k == 0:
            return False
    return True

def bolowitz(n):
    """Renvoie les n premiers nombres premiers.
    
    Args:
        n (int): Nombre de premiers désirés.
    
    Return:
        (list of int): Liste des nombres premiers.
    """
    k = 1
    premiers = []
    if(n >= 1):
        premiers.append(2)
    while len(premiers) < n:
        k += 2
        if(isPrime(k)):
            premiers.append(k)
    return premiers

# Deux fonctions d'un des DM.

prims = bolowitz(1000)

import os

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "premiers_1000.txt"

fichier = open(nameFile, 'w')

for p in prims:
    fichier.write(str(p)+'\n')
    # write remplace ce qu'il y avait dans le fichier au moment où on l'ouvre,
    # pas à chaque fois qu'on utilise la fonction write.

fichier.close()

# Conclusion :
print("\nRésultat :\nOn peut stocker des résultats, afin de ne pas avoir à "+
    "les recalculer plus tard.")