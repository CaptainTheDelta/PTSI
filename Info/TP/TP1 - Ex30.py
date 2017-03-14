# coding: utf-8

print("TP1 - Ex30")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice30.py, un programme qui calcule "+
    "la somme des n premiers entiers, n étant rentré par l'utilisateur.\n\n")

# Exercice :
n = int(input("Entrez un nombre : "))
s = 0

while n != 0:
    s += n
    n -= 1

print(s)

# Conclusion :
print("\nRésultat :\nA l'aide de la boucle while, on peut simplifier le "+
    "code, afin de le rendre peu 'volumineux'.")

# Comme je suis un peu crétin sur le bord, je laisse cet exemple. Mais toi,
# élève de PTSI-B sur-intelligent, tu as pris le temps de réfléchir un peu
# avant de te lancer éperdument dans la résolution de ce problème.

# En effet, il suffisait d'utiliser la formule n * (n + 1) / 2, comme ça :
# int(n * (n + 1) / 2)
# Et tadam ! Le même résultat calculé de façon bcp moins bourrine !
# (A chaque fois que l'on opère une division, Python se fait une joie de nous
# transformer le résultat en float (nombre à virgule). D'où le int...)

# Moralité : réfléchir plus de 1 sec avant de se lancer dans la résolution
# d'un problème.