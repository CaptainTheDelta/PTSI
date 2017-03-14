# coding: utf-8

print("TP1 - Ex36")

# Consigne :
print("\nDans la console écrire un programme qui calcule 5^245 en effectuant "+
    "toutes les multiplications. Comparer avec 5**245\n\n")

# Exercice :
i = 0
prod = 1

while i < 245:
    prod *= 5
    i += 1

print("5^245 = {}\n5**245 = {}".format(prod, 5**245))

# Conclusion :
print("\nRésultat :\nOn obtient le même résultat. (wow.)")