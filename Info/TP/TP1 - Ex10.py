# coding: utf-8

print("TP1 - Ex10")

# Consigne :
print("Tapez les instructions suivantes dans le fichier TP1.py et sauvez.\n\n"+
    "a = 10\n"+
    "b = 20\n"+
    "c = 30\n"+
    "a *= 2\n"+
    "c = b-a\n"+
    "print((a+b)*c+1)\n\n"+
    "Quel résultat va s'afficher à l'exécution ? Vérifiez.\n\n")

# Exercice :
print(">>> a = 10")
a = 10
print(">>> b = 20")
b = 20
print(">>> c = 30")
c = 30
print(">>> a *= 2")
a *= 2
print(">>> c = b-a")
c = b-a
print(">>> print((a+b)*c+1)")
print((a+b)*c+1)

# Conclusion :
print("Le résultat est 1, car pour le calcul final, c = 0 et comme python "+
    "applique les priorités opératoires")