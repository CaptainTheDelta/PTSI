# coding: utf-8
from math import *
def ex(nbr, consigne):
    a = ''
    if(nbr >= 10):
        a = '-'
    print("-------------Exercice n°{}-------------\n{}\
             ------------{}\n".format(nbr, consigne, a))

def res(conclusion):
    print("\nrésultat :", conclusion, sep='\n')

def finEx():
    input("\n")

def correctInput(txt, ty, end='\n>>> ', cons=[]):
    a = ""
    if(ty == str):
        a = 1
        while not type(a) == ty:
            try:
                a = ty(input(txt+end))
                assert len(a) > 0
                if(len(cons) > 0):
                    assert a.count(cons[0]) == cons[1]
            except:
                a = 1
                print("Valeur invalide.")
    else:
        while not type(a) == ty:
            try:
                a = ty(input(txt+end))
            except:
                a = ""
                print("Valeur invalide.")
    return a

ex(1,"""Taper les différentes opérations suivantes (chacune sur une ligne) :
2 + 3; 3 - 5; -2 * 7; 9 ** 2; 3.11 / 2.7; 2.2 / 3.5; 15.0 / 2.0; 15 // 2; 16 % 3

Observez le format des différents résultats.
Quittez l'IDLE et le relancer. Qu'observez-vous ?
""")

exo = ["2 + 3", "3 - 5", "-2 * 7", "9 ** 2", "3.11 / 2.7", "2.2 / 3.5", "15.0 / 2.0", "15 // 2", "16 % 3"]
[print("{} = {}".format(n, eval(n))) for n in "2 + 3; 3 - 5; -2 * 7; 9 ** 2; 3.11 / 2.7; 2.2 / 3.5; 15.0 / 2.0; 15 // 2; 16 % 3".split("; ")]

res("Python permet de faire des opérations simples.")
finEx()#----------------------------------------------------------

ex(2,"""Ouvrez une nouvelle fenêtre et sauvez le fichier dans votre dossier TP1 sous le nom : TP1.py. Dans ce fichier inscrivez les commandes suivantes :
1 + 1
print("2")
2 + 3
print(2*3)
2*3

Enregistrez et exécutez votre fichier. Qu'observez-vous ? Que fait Python exactement ?
""")

1 + 1
print("2")
2 + 3
print(2*3)
2*3

res("Utiliser un fichier permet de sauvegarder notre travail.")
finEx()#----------------------------------------------------------

ex(3,"""Modifiez le code contenu dans le fichier TP1.py pour qu'à l'exécution il affiche la table de 7 après avoir fait les calculs.
""")
print(1*7,2*7,3*7,4*7,5*7,6*7,7*7,8*7,9*7,10*7, sep='\n')

res("On obtient la table de 7.")
finEx()#----------------------------------------------------------

ex(4, """Remplacez le code du fichier TP1.py par :
for i in range(1,11):
    print(i,"* 7 = ", i*7)

Enregistrez et exécutez le avec Python 3. Magique non ? Que signifie ce code d'après vous ?
""")

for i in range(1,11):
    print(i,"* 7 = ", i*7)

res("On obtient la table de 7, mais avec un code plus lisible")
finEx()#----------------------------------------------------------

ex(5,"""Vérifiez que la console réagit exactement comme le shell de l'IDLE, en exécutant quelques commandes.
""")

res("Le code réagit de la même façon dans le shell.")
finEx()#----------------------------------------------------------

ex(6,"""Ouvrez le fichier TP1.py et exécutez le.
""")

res("Le fichier est exécuté dans Spyder")
finEx()#----------------------------------------------------------

ex(7,"""Dans la console créez une variable mon_annee et affectez lui votre année de naissance. Demandez à Python son identifiant et son type à l'aide des commandes id() et type(). Taper ensuite les différentes commandes suivantes :

mon_annee + 1 ; 3*mon_annee ; mon_annee + mon_annee ;
""")

mon_annee = 1999
print("id :",id(mon_annee))
print("type :",type(mon_annee))

print("\nmon_annee + 1 : ", mon_annee + 1)
print("3*mon_annee : ", (3*mon_annee)) 
print("mon_annee + mon_annee : ",mon_annee + mon_annee)

res("Python nous permet d'afficher des calculs sur des variables.")
finEx()#----------------------------------------------------------

ex(8,"""Dans la console tapez les lignes suivantes.

>>> a = 2013
>>> a = a + 1

Que vaut a à votre avis ? Vérifiez en affichant la valeur de a.

>>> a += 2
>>> a

Qu'a fait Python ? Essayez avec d'autres valeurs que 2 et avec d'autres opérations que +.
""")
a = 2013
a = a + 1
print("a vaut {}".format(a))
a += 2
print("a vaut {}".format(a))

res("La valeur de a est celle de la dernière valeur que nous lui avons attribué. La seconde partie permet de simplifier le code et de faire un calcul impliquant la variable, en ne l'appelant qu'une fois.")
finEx()#----------------------------------------------------------

ex(9,"""Dans la console, tapez les commandes suivantes.

>>> a = 10
>>> b = a + 1

Que vaut b ? Vérifiez en affichant la valeur.

>>> a = 10
>>> b = 20
>>> a = b
>>> b = a

Que valent a et b maintenant ? Vérifiez.

>>> a = 10
>>> b = 20
>>> c = a
>>> a = b
>>> b = c

Que valent a et b maintenant ? Vérifiez.

>>> a = 10
>>> b = 20
>>> print("a = ", a, "b = ", b)
>>> (a,b) = (b,a)
>>> print("a = ", a, "b = ", b)

Que s'est-il passé ?
""")
a = 10
b = a + 1
print("b vaut {}.".format(b))
a = 10
b = 20
a = b
b = a
print("a vaut {}, b vaut {}.".format(a,b))
a = 10
b = 20
c = a
a = b
b = c
print("a vaut {}, b vaut {}.".format(a,b))
a = 10
b = 20
print("a = ", a, "b = ", b)
(a,b) = (b,a)
print("a = ", a, "b = ", b)

res("Les variables ont été échangées.")
finEx()#----------------------------------------------------------

ex(10,"""Tapez les instructions suivantes dans le fichier TP1.py et sauvez.

a = 10
b = 20
c = 30
a *= 2
c = b-a
print((a+b)*c+1)

Quel résultat va s'afficher à l'exécution ? Vérifiez.
""")

a = 10
b = 20
c = 30
a *= 2
c = b-a
print((a+b)*c+1)

res("Le résultat est 1, car pour le calcul final, c = 0 et comme python applique les priorités opératoires")
finEx()#----------------------------------------------------------

ex(11,"""Dans la console, tapez les instructions suivantes.

>>> a = 1 ; type(a)
>>> b = 1. ; type(b)
>>> import cmath
>>> c = 1j ; type( c )
>>> import fractions
>>> d = fractions.Fraction(3,8) ; f = fractions.Fraction(6,4)
>>> print(d+f); type(d)
>>> a+2 ; type(a+2)
>>> 2*a ;type(2*a)
>>> a+2. ; type(a+2.)
>>> 2.*a ; type(2.*a)
>>> b+2 ; type(b+2)
>>> b+2. ; type(b+2.)
>>> 2 + c ; type(2+c)

Qu'observez-vous ?
""")
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

res("On observe que python opère des conversions de type, les float l'emportant sur les int.")
finEx()#----------------------------------------------------------

ex(12,"""Tapez les différentes instructions suivantes dans la console.

>>> s = "Hello World!"
>>> print(s)
>>> s[0]
>>> s[11]
>>> s[3:5]
>>> s[:5]
>>> s[6:]
>>> s[:]
>>> s[-3]
>>> s[-3:]
>>> s[0:8:2]
>>> s[::3]
""")

s = "Hello World!"
print(s)
print(s[0])
print(s[11])
print(s[3:5])
print(s[:5])
print(s[6:])
print(s[:])
print(s[-3])
print(s[-3:])
print(s[0:8:2])
print(s[::3])

res("On opère du slicing. Les paramètres sont s[début:fin:pas]")
finEx()#----------------------------------------------------------

ex(13,"""Définissez la chaîne de caractère s = "0123456789" et écrivez les instructions qui afficheront les résultats suivants :

'0123456789'
'5'
'345'
'789'
'02468'
'13579'
'036'
""")

print(s[:])
print(s[5])
print(s[3:6])
print(s[7:])
print(s[::2])
print(s[1::2])
print(s[:-1:3])

res("Même conclusion que pour l'exercice précédent.")
finEx()#----------------------------------------------------------

ex(14,"""Dans la console tapez les instructions qui affichent :

"J'aime beaucoup Python.
        Même si je ne comprends pas tout."
""")

print("J'aime beaucoup Python.\n\tMême si je ne comprends pas tout.")

res("\\n permet correspond à un retour à la ligne, \\t correspond à une tabulation.")
finEx()#----------------------------------------------------------

ex(15,"""Tapez dans la console et évaluez les instructions suivantes.

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
""")

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

res("Les opérations entre true et false retournent des entiers. Pour faire de la logique booléenne, on utilise not, and et or.\nLes calculs sont prioritaires sur les comparaisons. La comparaison de textes porte sur leur longueurs.")
finEx()#----------------------------------------------------------

ex(16,"""Dans la console essayez les conversions suivantes :

float(123) ; bool(0) ; str(True) ; float('1.22') ; int(1.23)
bool(1) ; bool('abc') ; float('123') ; int(True) ; str(123) ; bool('')
float(True) ; int(False) ; str(1.23) ; bool(1.23) ; float(False)
""")

print(float(123))
print(bool(0))
print(str(True))
print(float('1.22'))
print(int(1.23))
print(bool(1))
print(bool('abc'))
print(float('123'))
print(int(True))
print(str(123))
print(bool(''))
print(float(True))
print(int(False))
print(str(1.23))
print(bool(1.23))
print(float(False))

res("Python opère les conversions qu'on lui demande, en opérant des équivalences lorsque la conversion ne peut être directe.")
finEx()#----------------------------------------------------------

ex(17,"""Ecrire dans un fichier TP1-exercice17.py un programme qui demande à l'utilisateur son nom, son prénom et son année de naissance et qui retourne le résultat suivant sous la forme :

Nom : Leponge
Prénom : Bob
Année de naissance : 1900
""")

info = correctInput("Entrez <Nom> <Prénom> <année de naissance> : ", str, cons=[' ',2]).split()
print("Nom : {}\nPrénom : {}\nAnnée de naissance : {}".format(info[0], info[1], info[2]))

res("On peut demander des données de type int ou string à l'utilisateur.")
finEx()#----------------------------------------------------------

ex(18,"""Ecrire dans un fichier TP1-exercice18.py un programme qui demande à l'utilisateur le rayon d'une sphère et qui retourne le résultat suivant sous la forme :

Entrez le rayon en cm : 5
Une sphere de rayon 5.0 cm a pour surface : 314.159265359 cm2
Une boule de rayon 5.0 cm a pour volume : 523.5987755982989 cm3
""")

print("Entrez le rayon de la sphère en cm")
r = correctInput("r : ", int, end='')
print("Une sphere de rayon {r} cm a pour surface : {s} cm2\nUne boule de rayon {r} cm a pour volume : {v} cm3".format(r=r, s=4*pi*(r**2), v=(4/3)*pi*(r**3)))

res("Ces valeurs, une fois traduites (ici en nombre entier), peuvent servir comme les autres variables.")
finEx()#----------------------------------------------------------

ex(19,"""Ecrire dans un fichier TP1-exercice19.py un programme qui demande à l'utilisateur son nom et son prénom et qui retourne ses initiales.
""")

info = correctInput("Entrez <Nom> <Prénom> : ", str, cons=[' ',1]).split()
print(info[0][0], info[1][0])

res("Les variables string sont des tableaux, pour obtenir les initiales, on prend donc la première valeur de chaque tableau.")
finEx()#----------------------------------------------------------

ex(20,"""Ecrire dans un fichier TP1-exercice20.py le programme suivant :

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
""")

import random
nombre = random.randint(0,10)
n = correctInput('Saisissez un entier dans [0, 10]', int)
if n < nombre:
   print('Votre proposition est trop petite')
elif n > nombre:
   print('Votre proposition est trop grande')
else:
   print('Vous avez trouve le bon nombre!')

res("Ce programme permet de faire plusieurs tests à la suite. (elif <=> else if)")
finEx()#----------------------------------------------------------

ex(21,"""Ecrire dans un fichier TP1-exercice21.py, un programme qui demande un nombre entier à l'utilisateur et qui affiche si oui ou non il appartient à l'intervalle entier allant de 0 à 10.
""")

n = correctInput('Entrez un nombre : ', int)
if(0 <= n <= 10): # <=> 0 <= n and n <= 10
    print(n, 'appartient à [0;10].')
else:
    print(n, "n'appartient pas à [0;10].")

res("if et else sont pratiques dans le cas où il n'y a que deux issues possibles.")
finEx()#----------------------------------------------------------

ex(22,"""Ecrire dans un fichier TP1-exercice22.py, un programme qui demande un nombre entier à l'utilisateur et qui affiche le double s'il est impair et le triple s'il est pair.
""")

n = correctInput('Entrez un nombre : ', int)
# si la méthode modulo n'est pas valide :
# if(str(n)[-1] in '13579'):
if(n%2 == 1):
    print(n*2)
else:
    print(n*3)

res("En fonction de la valeur de n, le code s'execute de deux manières différentes.")
finEx()#----------------------------------------------------------

ex(23,"""Ecrire dans un fichier TP1-exercice23.py, un programme qui demande un nombre entier à l'utilisateur et qui affiche le double s'il est impair, le triple s'il est pair mais pas divisible par 4 et sa moitié sinon.
""")

n = correctInput('Entrez un nombre : ', int)
if(n%2 == 1):
    print(n*2)
elif(n%4 != 0):
    print(n*3)
else:
    print(n/2)

res("De même, le code affiche des valeurs différentes en fonction de la valeur de n. Comme il y a trois cas d'utilisation, on utilise if, elif et else.")
finEx()#----------------------------------------------------------

ex(24,"""Ecrire dans un fichier TP1-exercice24.py, un programme qui demande un nombre à l'utilisateur et qui renvoie sa valeur absolue.
""")

n = correctInput('Entrez un nombre : ', int)
print('Valeur absolue : ',end='')
if(n < 0):
    print(-n)
else:
    print(n)

res("Pour obtenir la valeur absolue d'un nombre, on ne s'intéresse qu'à son signe. Il suffit donc d'un if else pour la déterminer.")
finEx()#----------------------------------------------------------

ex(25,"""Ecrire dans un fichier TP1-exercice25.py, un programme qui demande les trois coefficients réels d'un trinôme \(ax^2+bx+c\) à l'utilisateur et qui retourne une phrase indiquant le nombre de racines réelles distinctes de ce trinôme, après avoir vérifié qu'il s'agissait bien d'un polynôme du second degré.
""")

print("Soit f(x) = ax^2 + bx + c.")
coef = list(map(int, correctInput("Entrez <a> <b> <c> :", str, cons=[' ', 2]).split()))
a = coef[0]; b = coef[1]; c = coef[2]
delta = b**2 -4*a*c
if(delta > 0):
    print("Le trinôme admet deux racines, X1 = {}, X2 = {} .".format((-b-sqrt(delta))/(2*a),(-b+sqrt(delta))/(2*a)))
elif(delta == 0):
    print("Le trinôme admet une racine, X = {} .".format((-b-sqrt(delta))/(2*a)))
else:
    print("Le trinôme n'admet pas de racine.")

res("A l'aide des valeurs des coefficients du trinôme, on peut déterminer les racines (si elles existent) du trinôme.")
finEx()#----------------------------------------------------------

ex(26,"""Ecrire dans un fichier TP1-exercice26.py, un programme qui demande une année à l'utilisateur et qui indique si elle est bissextile ou non. Une année est bissextile par définition si sa valeur vérifie l'une des conditions :


être multiple de 4 mais pas de 100 ;
être multiple de 400.
""")

an = correctInput('Entrez une année : ', int)
if(an%4 == 0):
    if(an%100 != 0):
        print("L'année {} est bissextile.".format(an))
    elif(an%400 == 0):
        print("L'année {} est bissextile.".format(an))
else:
    print("L'année {} n'est bissextile.".format(an))

res("Une solution est d'imbriquer les if entre eux, mais dans ce cas, on  ne respecte pas le \"Don't Repeat Yourself\".")
finEx()#----------------------------------------------------------

ex(27,"""Ecrire dans un fichier TP1-exercice26r.py, un programme qui fait la même chose que TP1-exercice26.py mais avec une structure conditionnelle minimale et des opérateurs booléens.
""")

an = correctInput('Entrez une année : ', int)
if(an%4 == 0 and (an%100 != 0 or an%400 == 0)):
    print("L'année {} est bissextile.".format(an))
else:
    print("L'année {} n'est bissextile.".format(an))


res("De cette manière, il n'y a plus de répétition du code.")
finEx()#----------------------------------------------------------

ex(28,"""Ecrire ce programme en pseudo-code.
""")

print("""soit i = 0
tant que i < 10:
    afficher 7*(i+1)
    incrémenter i
""")

res("Ce pseudo code permet d'afficher la table de 7.")
finEx()#----------------------------------------------------------

ex(29,"""(Racine carrée entière) Ecrire dans un fichier TP1-exercice29.py, un programme qui demande à l'utilisateur un nombre entier n , qui affiche l'entier dont le carré est l'entier, inférieur ou égal, le plus proche de n. Par exemple il affichera 2 si l'utilisateur rentre 7.
""")

n = correctInput('Entrez un nombre : ', int)
r = 0
while(not (r**2 <= n < (r+1)**2)):
    r+=1
print("r:{},r+1:{}".format(r,r+1))

print("La partie entière de la racine de {} est : {}".format(n,r))

res("De cette manière, on peut trouver une valeur approchée de la racine.")
finEx()#----------------------------------------------------------

ex(30,"""Ecrire dans un fichier TP1-exercice30.py, un programme qui calcule la somme des n premiers entiers, n étant rentré par l'utilisateur.
""")

n = correctInput('Entrez un nombre : ', int)
s = 0
while n != 0:
    s += n
    n -= 1
print(s)

res("A l'aide de la boucle while, on peut simplifier le code, afin de le rendre peu 'volumineux'.")
finEx()#----------------------------------------------------------

ex(31,"""Que calcule ce programme ?
somme = 0
i=0
while i <= 20:
    if i % 2 == 0:
       somme += i
    i += 1
print(somme)


Réécrire ce code sans la structure conditionnelle.
""")

somme = 0
i=0
while i <= 20:
    if i % 2 == 0:
       somme += i
    i += 1
print(somme)
print("Ce programme permet de calculer la somme des nombres pairs inférieurs à 20")
somme = 0
i=0
while i <= 10:
    somme += (i*2)
    i += 1
print(somme)

res("On voit qu'il est parfois possible d'obtenir le même résultat, à l'aide d'un code plus simple.")
finEx()#----------------------------------------------------------

ex(32,"""Ecrire dans un fichier TP1-exercice32.py, un programme qui calcule la somme des multiples de 3 ou de 5 strictement inférieurs à 1000.
""")

somme = 0
i = 0
while i < 1000:
    if(i%5 == 0 or i%3 == 0):
        somme += i
    i += 1
print("somme :", somme)

res("Cette somme est obtenue en vérifiant que l'incrément est un multiple de 3 ou de 5. On aurait pu faire deux boucles while en reprenant le principe de l'exercice précedent.")
finEx()#----------------------------------------------------------

ex(33,"""(L'algorithme des différences successives)
Que calcule ce programme ?
Ecrire dans un fichier TP1-exercice33.py le code de ce programme.
Le modifier pour obtenir la division euclidienne de a par b.
""")
tab = list(map(int, correctInput("Entrez <a> <b> :", str, cons=[' ', 1]).split()))
a = tab[0] ; b = tab[1]

div = 0
while a > b:
    div += 1
    a = a-b

print("Cet algorithme permet de calculer (sans modification) {a}%{b} = {m}, et la division euclidienne {a}//{b} = {d}".format(a=tab[0], b=b, m=a, d=div))

res("On peut opérer une division euclidienne à l'aide de l'algorithme des différences successives.")
finEx()#----------------------------------------------------------

ex(34,"""Dans la console écrire un programme qui affiche toutes les consonnes de la chaîne "Vive les TP Python en PTSI-B" et qui affiche un underscore à la place des voyelles.
""")

phrase = "Vive les TP Python en PTSI-B"
for i,c in enumerate(phrase):
    if(c in "aAeEiIoOuUyY"):
        phrase = phrase[:i] + '_' + phrase[i+1:]
print(phrase)

res("Il faut être attentif car la boucle for a in b ne modifie pas b !!!")
finEx()#----------------------------------------------------------

ex(35,"""Dans la console écrire un programme qui affiche la somme des carrés des entiers de 10 à 38, puis la somme des cubes des entiers impaires de 10 à 38, qui utilise l'expression range().
""")
somme = 0
for i in range(10,38+1):
    somme += i**2
print("somme des carrés des entiers de 10 à 38 :", somme)
for i in range(11,38,2):
    somme += i**3
print("somme des cubes des entiers impaires de 10 à 38 :", somme)

res("Le range permet d'itérer sur des suites simples de nombres. Les paramètres sont les mêmes que pour le slicing.")
finEx()#----------------------------------------------------------

ex(36,"""Dans la console écrire un programme qui calcule 5^245 en effectuant toutes les multiplications. Comparer avec 5**245
""")

i = 0
prod = 1
while i < 245:
    prod *= 5
    i += 1
print("5^245 = {} \n5**245 = {}".format(prod, 5**245))

res("On obtient le même résultat.")
finEx()#----------------------------------------------------------

ex(37,"""Dans la console écrire un programme qui calcule 100! en effectuant toutes les multiplications. Comparer le résultat avec la fonction factorial du module math. Calculer la somme des décimales de ce nombre.
""")

i=1
prod = 1
while i <= 100:
    prod *= i
    i += 1
print(prod)
print(factorial(100))
print("Ces résultats sont égaux.")
prod = str(prod)
somme = 0
for n in prod:
    somme += int(n)
print("Somme :", somme)

res("Il faut savoir utiliser les for et les while à bon escient.")
finEx()#----------------------------------------------------------

ex(38,"""Afficher tous les nombres premiers compris entre 1 et 100 dans la console.
""")

premier = []
Max = 100
for i in range(Max + 1):
    premier.append(True)
premier[0] = False; premier[1] = False

for p in range(int(sqrt(Max))+1):
    if(premier[p]):
        for i in range(p+p, Max+1, p):
            premier[i] = False
for i in range(Max+1):
    if(premier[i]):
        print(i, end=', ')

res("On utilise le crible d'Eratosthène afin de déterminer les nombres premiers.")
finEx()#----------------------------------------------------------

ex(39,"""Ecrire un programme qui retourne le nombre d'entiers premiers compris entre deux nombres a et b rentrés par l'utilisateur.
""")

a = correctInput('Entrez une borne inférieure : ',int)
b = correctInput('Entrez une borne supérieure : ',int)

Max = b
for i in range(Max + 1):
    premier.append(True)
premier[0] = False; premier[1] = False

for p in range(int(sqrt(Max))+1):
    if(premier[p]):
        for i in range(p+p, Max+1, p):
            premier[i] = False
compteur = 0
for i in range(a, b+1):
    if(premier[i]):
        compteur += 1
print("Il y a {} nombres premiers entre {} et {}".format(compteur,a,b))

res("""Comme pour l'exercice précédant, on utilise plusieurs itérations pour : 
 - Définir un tableau nombre:True
 - définir les nombres premiers
 - en tirer un résultat.""")
finEx()#----------------------------------------------------------

ex(40,"""Combien y a-t-il de nombre n <= 10^8 tels que n et n+2 sont premiers ?
""")

#Max = 10**8
#for i in range(Max+3):
#    premier.append(True)
#premier[0] = False; premier[1] = False

#for p in range(int(sqrt(Max+2))+1):
#    if(premier[p]):
#        for i in range(p+p, Max+3, p):
#            premier[i] = False

# on va utiliser le fait que tout nombre premier >3 est de la forme 6k-1 ou 6k+1 (kappartient à N) 
#compteur = 0
#for i in range(0,12):
#    if(premier[i-1] and premier[i+1]):
#        compteur += 1
#for i in range(12, Max+3, 6):
#    if(premier[i-1] and premier[i+1]):
#        compteur += 1
#print("Il y a {} nombres tels que n et n+2 soient premiers.".format(compteur))

# résultat du code précédant, mais qui met ~1h30 à s'executer
print("Il y a 440312 nombres tels que n et n+2 soient premiers.")
res("Idem que l'exercice précedant.")
finEx()#----------------------------------------------------------

ex(41,"""Calculer la somme des 111 premiers nombres premiers.
""")

premier = [2]
while len(premier) <= 111:
    encore = True
    i = premier[-1]
    while encore:
        i += 1
        for p in premier:
            if i%p == 0:
                break
            elif(p == premier[-1]):
                premier.append(i)
                encore = False
print("La somme des 111 nombres premiers vaut", str(sum(premier)))

res("On utilise une méthode différente pour déterminer les nombres premiers. Pour chaque nombre testé, on vérifie s'il n'est pas le multiple d'un nombre premier.")
finEx()#----------------------------------------------------------

ex(42,"""Vérifier le théorème de Wilson pour p <= 10^4 qui affirme qu'un entier p est premier si et seulement si (p) divise ((p-1)!+1) .
""")

#Max = 10**4
#for i in range(Max+1):
#    premier.append(True)
#premier[0] = False; premier[1] = False
#compteur = 0
#for p in range(int(sqrt(Max))+1):
#    if(premier[p]):
#        for i in range(p+p, Max+1, p):
#            premier[i] = False
#for i in range(Max+1):
#    if(premier[i]):
#        compteur += 1
#i = 2
#compteurBis = 0
#while i <= 10**4:
#    if((factorial(i-1)+1)%i == 0):
#        compteurBis += 1
#    i += 1
#print("Il y a {} nombres premiers inférieurs à 10^4 (crible d'Eratosthène), et {} selon le théorème de Wilson.".format(compteur, compteurBis))

# de même, le calcul de cet exercice met ~3min
print("Il y a 1229 nombres premiers inférieurs à 10^4 (crible d'Eratosthène), et 1229 selon le théorème de Wilson.")

res("On peut démontrer la véracité (ou non) d'un théorème, du moins sur un ensemble borné.")
finEx()#----------------------------------------------------------

ex(43,"""Déterminer les nombres premiers p <= 100 tels qu'il existe deux entiers a et b tels que a^2 + b^2 = p.
""")

Max = 100
premier = []
for i in range(Max+1):
    premier.append(True)
premier[0] = False; premier[1] = False

for p in range(int(sqrt(Max))+1):
    if(premier[p]):
        for i in range(p+p, Max+1, p):
            premier[i] = False

for a in range(10):
    for b in range(a,10):
        somme = a**2 + b**2
        if(somme < 100 and premier[somme]):
            print("{}**2 + {}**2 = {}".format(a, b, somme))

res("On peut imbriquer les for entre eux pour faire des calculs sur plusieurs variables changeantes.")
finEx()#----------------------------------------------------------