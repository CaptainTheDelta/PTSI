# coding: utf-8

print("TP4 - Ex10")

# Consigne :
print("\nEcrire une fonction qui prend comme argument un entier naturel "+
    "n<=1000 et qui retourne la somme des n premiers nombres premiers après "+
    "les avoir lu dans le fichier premiers_1000.\n\n")

# Exercice :

import os

os.chdir("C:\\Users\\lesec\\Documents\\Boulot\\Info\\TP\\Ressources")
nameFile = "premiers_1000.txt"

def sommePremiers(n):
    """Renvoie la somme des n premiers nombres premiers.

    Args:
        n (int): Nombre de nombre premiers.

    Return:
        (int): Somme des nombres premiers.
    """
    assert 0 <= n <= 1000
    # Vérifie que n est valide.

    s = 0
    nP = open(nameFile, 'r')
    # nP pur nombresPremiers

    while(n > 0):
        s += int(nP.readline())
        n -= 1
        # Tant qu'il y a des lignes, on lit le fichier.

    nP.close()

    return s

n = int(input("Nombre de premiers : "))
print("Somme :", sommePremiers(n))

# Conclusion :
print("\nRésultat :\nOn peut stocker des résultats, afin de ne pas avoir à "+
    "faire les mêmes calculs plusieurs fois, même si on relance le programme.")