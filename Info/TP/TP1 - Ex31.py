# coding: utf-8

print("TP1 - Ex31")

# Consigne :
print("""\nQue calcule ce programme ?
somme = 0
i=0
while i <= 20:
    if i % 2 == 0:
       somme += i
    i += 1
print(somme)


Réécrire ce code sans la structure conditionnelle.\n""")

# Exercice :
somme = 0
i=0

while i <= 10:
    somme += 2 * i
    i += 1

print(somme)

# Conclusion :
print("\nRésultat :\nCe programme permet de calculer la somme des nombres "+
    "pairs inférieurs à 20")