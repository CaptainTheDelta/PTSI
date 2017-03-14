# coding: utf-8

print("TP1 - Ex27")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice26r.py, un programme qui fait la même chose que TP1-exercice26.py mais avec une structure conditionnelle minimale et des opérateurs booléens.\n\n")

# Exercice :
an = int(input("Entrez une année : "))

if(an % 4 == 0 and (an % 100 != 0 or an % 400 == 0)):
    print("L'année {} est bissextile.".format(an))
else:
    print("L'année {} n'est bissextile.".format(an))

# On utilise 'or' et 'and' qui sont des opérateurs booléens.

# Conclusion :
print("\nDe cette manière, il n'y a plus de répétition du code.")