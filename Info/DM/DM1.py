# -*- coding: utf-8 -*-
"""
@author Lesecq - Damien
"""
# DM1 - Informatique PTSI-B 2016/17

def ex(n):
    print("\n\n-------------Exercice {}-------------".format(n))

print("\n\tDM1 - Informatique")
print("\t   PTSIB 15/16")
print("\t  Lesecq Damien")

# Exercice 4
ex(4)

temps = 6.822
distance = 19.76

vitesse = distance/temps                                            # v = d/t
print("La vitesse en kilmoètre/heure est :", vitesse, "km/h")

print("La vitesse en kilmoètre/heure est : %.2f" %vitesse, "km/h")

# Exercice 5
ex(5)

Un = [1,2]                                                          # liste contenant u0 et u1
N = int(input("Entrez un entier n : "))

n = 0
while n+2 <= N:                                                     # comme la formule de (Un) est définie sur Un+2, on s'assure de bien trouver UN et pas UN+2
    Un.append(Un[n+1]**2 + 3*Un[n])                                 # ajout à la liste de Un+2
    n += 1                                                          # incrémentation de n
print("Un =", Un[N])

# Exercice 6
ex(6)

somme = 0
for i in range(31):                                                 # pour i dans [0, 31[
    for j in range(-10,11):                                         # pour j dans [-10, 11[
        for k in range(1,46,2):                                     # pour k dans [1,46[, de deux en deux
            somme += (1 + i * j * k)**2
print("La somme vaut", somme)

# Exercice 7
ex(7)

n = int(input("Entrez un entier n : "))
facto = 1
for i in range(1,n+1):
    facto *= i
print("La factorielle vaut :", facto)

facto = str(facto)                                                  # on convertit facto en string
nbr0 = 0
while(facto[-1] == '0'):                                            # tant que le dernier charactère de facto est un 0
    nbr0 += 1                                                       # on incrémente le compteur
    facto = facto[:-1]                                              # on supprime le dernier charactère
print("Il y a {} 0 qui finnissent {}!.".format(nbr0, n))

# Exercice 8
ex(8)

phrase = input("Entrez une phrase : ")
voyelle = 0
consonne = 0
for c in phrase:                                                    # Pour chaque lettre
    if(c in "aAeEiIoOuUyYéÉèÈàÀùÙâÂêÊîÎôÔûÛïÏëËüÜÿŸ"):              # si c'est une voyelle
        voyelle += 1
    elif(c in "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXzZçÇ"):        # si c'est une consonne
        consonne += 1
print("Dans votre phrase, il y a {} voyelles et {} consonnes".format(voyelle, consonne))

# Exercice 9
ex(9)

n = int(input("Entrez un entier n : "))

if(n%2 != 0 and n%5 != 0):                                          # si l'entrée vérifie les conditions initiales
    s = 1
    while s%n != 0:                                                 # tant que s n'est pas un multiple de n
        s = s*10 + 1                                                # determination du nbr suivant composé seulement de 1
    print("Le plus petit multiple de n qui ne contient que \
des 1 est : {}, il s'écrit avec {} 1.".format(s, len(str(s))))
else:
    print("Votre entier ne remplit pas les conditions.")

# Exercice 10
ex(10)

A = float(input("Entrez un réel A : "))
somme = 0
n = 0
while somme < A:                                                    # tant que la somme est inférieur à A
    n += 1
    somme = 0

    for k in range(1, n+1):                                         # calcul de la somme au n suivant
        somme += 1/k
print("Le plus petit entier n qui vérifie la proposition est :", n)

# Exercice 11
ex(11)

print("Question 1")
somme = 0
for n in range(64):                                                 # pour n appartenant à [0,64[
    somme += 2**n                                                   # calcul de la somme
    print("case {} : {}".format(n,2**n))                            # affichage du nbr de grains de riz
print("Il y a {} grain de riz en tout.".format(somme))

print("\nQuestion 2")
masse = somme*0.04                                                  # masse totale = nbr des grains de riz * masse d'un grain de riz
print("Il faut {} tonnes de riz.".format(masse))

print("\nQuestion 3")
print("Il faudra attendre {} années pour ramasser autant de riz.".format(masse/(740*10**6)))
                                                                    # masse totale divisée par la production d'une année

input("\nFin du DM")
