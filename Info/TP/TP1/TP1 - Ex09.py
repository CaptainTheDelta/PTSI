# coding: utf-8

print("TP1 - Ex9")

# Consigne :
print("\nDans la console, tapez les commandes suivantes.\n\n"+
    ">>> a = 10\n"+
    ">>> b = a + 1\n\n"+
    "Que vaut b ? Vérifiez en affichant la valeur.\n\n"+
    ">>> a = 10\n"+
    ">>> b = 20\n"+
    ">>> a = b\n"+
    ">>> b = a\n\n"+
    "Que valent a et b maintenant ? Vérifiez.\n\n"+
    ">>> a = 10\n"+
    ">>> b = 20\n"+
    ">>> c = a\n"+
    ">>> a = b\n"+
    ">>> b = c\n\n"+
    "Que valent a et b maintenant ? Vérifiez.\n\n"+
    ">>> a = 10\n"+
    ">>> b = 20\n"+
    ">>> print("a = ", a, "b = ", b)\n"+
    ">>> (a,b) = (b,a)\n"+
    ">>> print("a = ", a, "b = ", b)\n\n"+
    "Que s'est-il passé ?\n\n")

# Exercice :
print(">>> a = 10")
a = 10
print(a)
print(">>> b = a + 1")
b = a + 1
print(b)

print("b vaut {}.".format(b))

print(">>> a = 10")
a = 10
print(a)
print(">>> b = 20")
b = 20
print(b)
print(">>> a = b")
a = b
print(a)
print(">>> b = a")
b = a
print(b)

print("a vaut {}, b vaut {}.".format(a,b))

print(">>> a = 10")
a = 10
print(a)
print(">>> b = 20")
b = 20
print(b)
print(">>> c = a")
c = a
print(c)
print(">>> a = b")
a = b
print(a)
print(">>> b = c")
b = c
print(b)

print("a vaut {}, b vaut {}.".format(a,b))

print(">>> a = 10")
a = 10
print(a)
print(">>> b = 20")
b = 20
print(b)
print(">>> print(\"a = \", a, \"b = \", b)")
print("a = ", a, "b = ", b)
print(">>> (a,b) = (b,a)")
(a,b) = (b,a)
print(">>> print("a = ", a, "b = ", b)")
print("a = ", a, "b = ", b)

# Conclusion :
print("\nLes variables ont été échangées.")