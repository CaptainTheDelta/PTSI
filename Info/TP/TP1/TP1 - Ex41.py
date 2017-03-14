# coding: utf-8

print("TP1 - Ex41")

# Consigne :
print("\nCalculer la somme des 111 premiers nombres premiers.\n\n")

# Exercice :
premier = [2]
while len(premier) <= 111:
    encore = True
    i = premier[-1]

    while encore:
        i += 1

        for p in premier:
            if i%p == 0:
                break
            elif(p == premier[-1]):
                premier.append(i)
                encore = False


print("La somme des 111 nombres premiers vaut", str(sum(premier)))

# Conclusion :
print("\nRésultat :\n")

# Besoin d'explication ? (partie à mettre en commentaire si jamais vous testez)

premier = [2]
# On déclare une liste contenant le premier nombre premier.

while len(premier) <= 111:
    # Tant qu'on a pas 111 nombres premiers,

    encore = True
    i = premier[-1]
    # On prend le dernier nombre premier trouvé

    while encore:
        # Et on boucle tant qu'on a pas trouvé le suivant.
        i += 1

        # Via cette boucle, on vérifie que i n'est divisible par aucun des
        # nombres premiers déjà trouvés.
        for p in premier:
            if i%p == 0:
                break
            elif(p == premier[-1]):
                premier.append(i)
                encore = False

# Maintenant que je relis ce code, je pense que je l'aurais fait différement.
# Mais à chacun ces méthodes, je ne donne pas une correction, mais un exemple
# de solution.