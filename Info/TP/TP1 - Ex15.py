# coding: utf-8

print("TP1 - Ex15")

# Consigne :
print("""\nTapez dans la console et évaluez les instructions suivantes.

>>> True + True ; True + False ; True * False ; False + False ; False * False
>>> 2 < 3
>>> 2 != 3
>>> s1 = "trois" ; s2 = "sept"
>>> s1 > s2
>>> 2 + 3 == 5
>>> a = 2 ; b = 2.
>>> a == b
>>> a is b
>>> a = 2 ; b = 2
>>> a == b
>>> a is b
>>> 1 < 2 and 3 <= 5
>>> not(3 > 4)
>>> 'a'+'b' == 'ab' or 7 < 3
\n""")

# Exercice :
print(True + True)
print(True + False)
print(True * False)
print(False + False)
print(False * False)
print(2 < 3)
print(2 != 3)
s1 = "trois"
s2 = "sept"
print(s1 > s2)
print(2 + 3 == 5)
a = 2
b = 2.
print(a == b)
print(a is b)
a = 2
b = 2
print(a == b)
print(a is b)
print(1 < 2 and 3 <= 5)
print(not(3 > 4))
print('a'+'b' == 'ab' or 7 < 3)

# Conclusion :
print("\nLes opérations entre true et false retournent des entiers. Pour "+
    "faire de la logique booléenne, on utilise not, and et or.\nLes calculs "+
    "sont prioritaires sur les comparaisons. La comparaison de textes porte "+
    "sur leur longueurs.")