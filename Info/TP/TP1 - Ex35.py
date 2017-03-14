# coding: utf-8

print("TP1 - Ex35")

# Consigne :
print("\nDans la console écrire un programme qui affiche la somme des carrés "+
    "des entiers de 10 à 38, puis la somme des cubes des entiers impaires de "+
    "10 à 38, qui utilise l'expression range().\n\n")

# Exercice :
somme = 0

for i in range(10,38+1):
    somme += i**2

print("somme des carrés des entiers de 10 à 38 :", somme)

somme = 0

for i in range(11,38,2):
    somme += i**3

print("somme des cubes des entiers impaires de 10 à 38 :", somme)

# Conclusion :
print("\nRésultat :\nLe range permet d'itérer sur des suites simples de "+
    "nombres. Les paramètres sont les mêmes que pour le slicing.")