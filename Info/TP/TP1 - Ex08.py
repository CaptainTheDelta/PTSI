# coding: utf-8

print("TP1 - Ex8")

# Consigne :
print("\nDans la console tapez les lignes suivantes.\n\n"+
    ">>> a = 2013\n"+
    ">>> a = a + 1\n\n"+
    "Que vaut a à votre avis ? Vérifiez en affichant la valeur de a.\n"+
    ">>> a += 2\n"+
    ">>> a\n\n"+
    "Qu'a fait Python ? Essayez avec d'autres valeurs que 2 et avec d'autres "+
    "opérations que +.\n\n")

# Exercice :
print(">>> a = 2013")
a = 2013
print(a)

print(">>> a = a + 1")
a = a +1
print(a)

print(">>> a += 2")
a += 2
print(a)

print(">>> a")
print(a)

# Conclusion :
print("\nLa valeur de a est celle de la dernière valeur que nous lui avons "+
    "attribué. La seconde partie permet de simplifier le code et de faire un "+
    "calcul impliquant la variable, en ne l'appelant qu'une fois.")