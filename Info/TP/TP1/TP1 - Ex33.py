# coding: utf-8

print("TP1 - Ex33")

# Consigne :
print("""\n(L'algorithme des différences successives)
Que calcule ce programme ?
Ecrire dans un fichier TP1-exercice33.py le code de ce programme.
Le modifier pour obtenir la division euclidienne de a par b.\n\n""")

# Exercice :
a = int(input("Entrez a : "))
b = int(input("Entrez b : "))
div = 0
A = a

while a > b:
    div += 1
    a = a - b

# Conclusion :
print("\nRésultat :\nCet algorithme permet de calculer (sans modification) "+
    "{a}%{b} = {m}, et la division euclidienne {a}//{b} = {d}".format(
        a=A, b=b, m=a, d=div))

# Comme indiqué dans un précédent exercice, on voit qu'on peut utiliser des
# arguments pour la fonction format. L'utilité est peut-être plus parlante dans
# ce cas.