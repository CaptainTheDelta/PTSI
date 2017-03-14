# coding: utf-8

print("TP1 - Ex11")

# Consigne :
print("\nDans la console, tapez les instructions suivantes."+
    ">>> a = 1 ; type(a)\n"+
    ">>> b = 1. ; type(b)\n"+
    ">>> import cmath\n"+
    ">>> c = 1j ; type( c )\n"+
    ">>> import fractions\n"+
    ">>> d = fractions.Fraction(3,8) ; f = fractions.Fraction(6,4)\n"+
    ">>> print(d+f); type(d)\n"+
    ">>> a+2 ; type(a+2)\n"+
    ">>> 2*a ;type(2*a)\n"+
    ">>> a+2. ; type(a+2.)\n"+
    ">>> 2.*a ; type(2.*a)\n"+
    ">>> b+2 ; type(b+2)\n"+
    ">>> b+2. ; type(b+2.)\n"+
    ">>> 2 + c ; type(2+c)\n\n"+
    "Qu'observez-vous ?\n\n")

# Exercice :
a = 1
print(type(a))
b = 1. ; print(type(b))
import cmath
c = 1j ; print(type(c))
import fractions
d = fractions.Fraction(3,8) ; f = fractions.Fraction(6,4)
print(d+f,'\t',type(d)) #on additione deux fractions -> fraction
print(a+2,'\t',type(a+2))
print(2*a,'\t',type(2*a))
print(a+2.,'\t',type(a+2.))
print(2.*a,'\t',type(2.*a))
print(b+2,'\t',type(b+2))
print(b+2,'\t',type(b+2.))
print(2 + c,'\t',type(2+c))

# Conclusion :
print("\nOn observe que python opère des conversions de type, les float "+
    "l'<<emportent>> sur les int pendant les opérations.")