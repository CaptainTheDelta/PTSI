# coding: utf-8

print("TP1 - Ex20")

# Consigne :
print("""\nEcrire dans un fichier TP1-exercice20.py le programme suivant :

import random
nombre = random.randint(0,10)
n = int(input('Saisissez un entier dans [0, 10]'))
if n < nombre:
   print('Votre proposition est trop petite')
elif n > nombre:
   print('Votre proposition est trop grande')
else:
   print('Vous avez trouve le bon nombre!')



Que fait ce programme ? Vérifiez le.
\n\n""")

# Dans cet exercice, on introduit les conditions :
# if (= 'si') évalue une condition et exécute le contenu de son bloc si la
# condition est vérifiée.
# else (= 'sinon') exécute le contenu de son bloc si la condition du if n'est
# pas vérifiée.
# elif ('sinon si') elif est la contraction de else if. Sa condition est
# évaluée si le if (ou le elif précédent) est considérée comme fausse.

# Exercice :
import random
nombre = random.randint(0,10)
n = int(input('Saisissez un entier dans [0, 10]'))
if n < nombre:
   print('Votre proposition est trop petite')
elif n > nombre:
   print('Votre proposition est trop grande')
else:
   print('Vous avez trouve le bon nombre!')

# Conclusion :
print("\nCe programme permet de faire plusieurs tests à la suite.)")