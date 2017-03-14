# coding: utf-8
from math import factorial

print("TP1 - Ex37")

# Consigne :
print("\nDans la console écrire un programme qui calcule 100! en effectuant "+
    "toutes les multiplications. Comparer le résultat avec la fonction "+
    "factorial du module math. Calculer la somme des décimales de ce "+
    "nombre.\n\n")

# Exercice :
i = 1
prod = 1

while i <= 100:
    prod *= i
    i += 1

print(prod)

print(factorial(100))

print("Ces résultats sont égaux.")

prod = str(prod)
somme = 0

for n in prod:
    somme += int(n)

print("Somme :", somme)

# Conclusion :
print("\nRésultat :\nIl faut savoir utiliser les for et les while à bon "+
    "escient.")