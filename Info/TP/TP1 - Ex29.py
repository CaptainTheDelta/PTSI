# coding: utf-8

print("TP1 - Ex29")

# Consigne :
print("\n(Racine carrée entière) Ecrire dans un fichier TP1-exercice29.py, un "+
    "programme qui demande à l'utilisateur un nombre entier n , qui affiche "+
    "l'entier dont le carré est l'entier, inférieur ou égal, le plus proche "+
    "de n. Par exemple il affichera 2 si l'utilisateur rentre 7.\n\n")

# Exercice :
n = int(input("Entrez un nombre : "))
r = 0

while(not (r ** 2 <= n < (r + 1) ** 2)):
    # Le language Python permet d'encadrer les nombres dans ses conditions
    # booléennes.
    r += 1

print("r:{},r+1:{}".format(r,r+1))

print("La partie entière de la racine de {} est : {}".format(n,r))

# Conclusion :
print("\nRésultat :\nDe cette manière, on peut trouver une valeur approchée "+
    "de la racine.")

# Cette méthode n'est pas la seule !!!
# En algorithmique, il y a souvent beaucoup de manières différentes pour 
# programmer la même chose, le plus important est que la technique soit claire !

# (sauf dans les cas d'optimisation ou pour les pbm complexes, mais là y'a plein
# de commentaires et c'est pas exactement le même niveau)