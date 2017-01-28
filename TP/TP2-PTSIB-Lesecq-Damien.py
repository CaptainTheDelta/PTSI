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
#===============================================================================
    """
    
    Args:
        

    Return:
        
    """
ex(1,"""Ecrire une fonction somme_n_entiers qui prend comme argument un """
    """entier n et qui retourne la somme des n premiers entiers.
""")

def somme_n_entiers(n):
    """Si n est un entier positif, retourne la somme des n premiers entiers,
    sinon renvoie False.
    
    Args:
        n (int): Entier jusqu'auquel on veut faire la somme.

    Return:
        (bool) / (int): False si le paramètre est incorrect, la somme sinon.
    """
    if(type(n) != int or n < 0):
        print("Erreur")
        return False
    
    return int(n*(n+1)/2)

finEx()#------------------------------------------------------------------------

ex(2, """Ecrire une fonction factorielle qui prend comme argument un entier """
    """n et qui retourne n!, après avoir testé que n est bien un entier positif.
""")

def factorielle(n):
    """Renvoie la factorielle de n si n est un entier positif, False sinon.
    
    Args:
        n (int): Entier dont on veut calculer la factorielle.

    Return:
        (bool) / (int): False si le paramètre est incorrect, la factorielle
            sinon.
    """
    if(type(n) != int or n < 0):
        print("Erreur")
        return False
    
    fact = 1
    
    while n > 0:
        fact *= n
        n -= 1
    
    return fact

finEx()#------------------------------------------------------------------------

ex(3, """Ecrire une fonction syracuse1 qui prend comme argument un entier """
    """N positif et qui retourne u100 où la suite (uk), k appartenant à N, """
    """est définie par u0=N et pour tout k appartenant à N, uk+1=uk/2 si uk """
    """est pair et sinon uk+1=3uk+1.
""")

def syracuse1(n):
    """Si n est un entier positif, renvoie u100 par la suite syracuse, sinon
    renvoie False.
    
    Args:
        n (int): Entier auquel on veut appliquer la suite Syracuse.

    Return:
        (bool) / (int): False si n n'est pas un entier positif, le terme u100
        sinon.
    """
    if(type(n) != int or n < 0):
        print("Erreur")
        return False
    
    for i in range(100):
        if(n%2 == 0):
            n = n//2
        else:
            n = 3*n+1
    
    return n

finEx()#------------------------------------------------------------------------

ex(4, """Ecrire une fonction fibo qui prend comme argument un entier n et """
    """qui retourne le n-ième terme de la suite de Fibonacci.
""")

def fibo(n):
    """Si n est un entier positif, renvoie le n-ième terme de la suite de
    Fibonacci, sinon renvoie False.
    
    Args:
        n (int): Rang attendu de la suite de Fibonacci

    Return:
        (bool) / (int): False si n n'est pas un entier positif, le n-ième terme
        sinon.
    """
    if(type(n) != int or n < 0):
        print("Erreur")
        return False
    
    a = 1
    b = 1
   
    while n > 0:
        (a, b) = (b, a+b)
        n -= 1
    
    return b

finEx()#------------------------------------------------------------------------

ex(5, """Ecrire une fonction isPositive qui prend comme argument un réel x """
    """est qui renvoie True si x est positif et False sinon.
""")

def isPositive(n):
    """Si n est un réel positif, renvoie True, sinon renvoie False.
    
    Args:
        n (int): Entier à tester.

    Return:
        (bool): True si n est réel positif, False sinon.
    """
    if((type(n) != int and type(n) != float) or n < 0):
        return False
    
    return True

finEx()#------------------------------------------------------------------------

ex(6, """Ecrire une fonction somme_dec qui prend comme argument un entier n """
    """et qui retourne la somme de ses décimales.
""")

def somme_dec(n):
    """Si n est un entier, renvoie la somme des décimales de n, sinon False.
    
    Args:
        n (int): Entier dont on va additionner les décimales.

    Return:
       (bool) / (int): False si le paramètre est incorrect, la somme de ses
       décimales sinon. 
    """
    if(type(n) != int):
        print("Erreur")
        return False
    
    somme = 0
    N = str(n)
    
    if(n < 0):
        N = N[1:]
    for dec in N:
        somme += int(dec)
    
    return somme

finEx()#------------------------------------------------------------------------

ex(7, """Ecrire une fonction isPalindrome qui prend comme argument une """
    """chaîne de caractère et qui retourne True si cette chaîne est un """
    """palindrome et False sinon.
""")

def removeSpaces(string):
    """Renvoie la chaîne string dénuée de ses espaces.
    
    Args:
        string (str): Chaîne de caractères à dépouiller de ses espaces.

    Return:
        (bool) / (str): Chaîne dénuée d'espaces.
    """
    text = ""
    
    for c in string:
        if(c != ' '):
            text += c
    
    return text

def isPalindrome(string):
    """Renvoie True si string est un palindrome et False sinon.

    Args:
        string (str): Chaîne de caractère à analyser.

    Return:
        (bool): True si string est un palindrome, False sinon.
    """
    text = removeSpaces(string).lower()
    
    for c in range(len(text)//2):
        if(text[c] != text[-1-c]):
            return False
    
    return True

finEx()#------------------------------------------------------------------------


ex(8, """Ecrire une fonction inverse_liste qui prend une liste comme """
    """argument et qui renvoie la liste obtenue en la lisant par la fin.
""")

def inverse_liste(array):
    """Renvoie la liste array renversée.
    
    Args:
        array (list): Tableau à renverser.

    Return:
        (list): Tableau renversé.
    """
    
    #for i,value in enumerate(array[:]):
    #    array[-1-i] = value
    #return array
    
    return array[::-1]

finEx()#------------------------------------------------------------------------


ex(9,"""Ecrire une fonction somme_cube qui prend deux entiers p et q comme """
    """arguments et qui retourne la somme de k^3, k allant de p à q.
""")

def somme_cube(p,q):
    """Si n est un entier positif, retourne la somme des k^3, k allant de p à q,
    sinon renvoie False.
    
    Args:
        n (int): Entier jusqu'auquel on veut faire la somme.

    Return:
        (bool) / (int): False si le paramètre est incorrect, la somme sinon.
    """
    if(type(n) != int or n < 0):
        print("Erreur")
        return False
    
    somme = 0

    for i in range(p,q+1):
        somme += i**3

    return somme

finEx()#------------------------------------------------------------------------

ex(10, """Ecrire une fonction max2 qui prend deux nombres réels en argument """
    """et qui retourne le maximum des deux.
""")

def max2(a,b):
    """Si a et b sont des réels, renvoie le pls grand des deux, sinon renvoie 
    False.
    
    Args:
        a (int): Réel à comparer.
        b (int): Réel à comparer.

    Return:
        (bool) / (int): False si , False sinon.
    """
    if((type(a) != int and type(b) != float) 
        or (type(b) != int and type(b) != float)):
        return False
    
    return a if a > b else b

finEx()#------------------------------------------------------------------------

ex(11, """Ecrire une fonction max2 qui prend deux nombres réels en argument """
    """et qui retourne le maximum des deux.
""")

def max3(a,b,c):
    """Si a, b et c sont des réels, renvoie le pls grand des trois, sinon 
    renvoie False.
    
    Args:
        a (int): Réel à comparer.
        b (int): Réel à comparer.
        b (int): Réel à comparer.

    Return:
        (bool) / (int): False si un paramètre est incorrect, sinon le plus grand
            des trois
    """
    if((type(a) != int and type(b) != float) 
        or (type(b) != int and type(b) != float)
        or (type(c) != int and type(c) != float)):
        return False
    
    return min2(a, min2(b, c))

ex(12,"""Ecrire une fonction decompo_base qui prend deux entiers n et b et """
    """qui retourne sous forme de liste la décomposition de n dans la base b.
""")

def decompo_base(n,b):
    """Si n et b sont des entiers positifs, retourne la décomposition de n en
    base b, sinon on renvoie False.
    
    Args:
        n (int): Entier à décomposer.
        b (int): Base.

    Return:
        (bool) / (int): False si un paramètre est incorrect, la décomposition
            sinon.
    """
    if((type(n) != int or n < 0) and (type(b) != int or b < 0)):
        print("Erreur")
        return False
    
    nbr = []
    
    while n != 0:
        nbr.insert(0, n%b)
        n //= b
    
    return nbr

finEx()#------------------------------------------------------------------------

ex(13,"""Ecrire une fonction produit_fk qui prend en argument une fonction f """
    """et deux entiers p<q et qui retourne le produit des nombres f(k) pour """
    """p<= k <=q. Vérifiez votre résultat sur la fonction cube et la """
    """fonction factorielle .
""")

def produit_fk(f,p,q):
    """Si p et q sont des entiers positifs, retourne la somme des f(k), k allant
    de p à q, sinon renvoie False.
    
    Args:
        f (function): Fonction à appliquer.
        p (int): Borne inférieure.
        q (int): Borne supérieure.

    Return:
        (bool) / (int): False si un paramètre est incorrect, la somme sinon.
    """
    if((type(p) != int or p < 0) and (type(q) != int or q < 0)):
        print("Erreur")
        return False

    prod = 1

    for i in range(p, q+1):
        prod *= f(i)

    return prod

finEx()#------------------------------------------------------------------------

ex(14,"""Réécrire la fonction map.
""")

def map2(f, array):
    """Applique la fonction f à la liste array.
    
    Args:
        f (function): Fonction à appliquer.
        array (list): List à traiter.

    Return:
        (bool) / (list): False si un paramètre est incorrect, la liste modifiée
            sinon.
    """
    return [f(i) for i in array]

finEx()#------------------------------------------------------------------------

ex(15,"""Ecrire une fonction isEven prenant un entier n et renvoyant True """
    """s'il est pair et False sinon. Puis une fonction filtre qui prend en """
    """argument une liste et une fonction test et qui renvoie la liste des """
    """éléments de liste pour lesquels la fonction test renvoie True . """
    """L'essayer avec une liste d'entiers et la fonction isEven .
""")

def isEven(n):
    """Renvoie si n est pair.
    
    Args:
        n (int): Entier à tester.

    Return:
        (bool): False si le paramètre est incorrect, la parité sinon.
    """
    return n%2 == 0

def filtre(f,array):
    """Renvoie le tableau contenant les elements de array vérifiant f.
    
    Args:
        f (function): Fonction à appliquer.
        array (list): List à traiter.

    Return:
        (list): Liste modifiée.
    """
    return [a for a in array if f(a)]

finEx()#------------------------------------------------------------------------

ex(16,"""Ecrire une fonction récursive qui prend deux nombres entiers positifs """
    """comme argument, et qui retourne leur somme.
""")

def sommeRec(a,b):
    """Renvoie la somme de a et b par récursivité.

    Args:
        a (int): Entier à sommer.
        b (int): Entier à sommer

    Return:
        (int): Somme de a et b.
    """
    if(b == 0):
        return a

    return sommeRec(a+1, b-1)

finEx()#------------------------------------------------------------------------

ex(17,"""Ecrire une fonction puissance récursive qui prend un réel x et un """
    """entier n , et qui retourne leur x^n.
""")

def puissance(x,n):
    """Renvoie x puissance n par récursivité.

    Args:
        x (int): réel dont on veut la puissance.
        n (int): Exposant.

    Return:
        (int): x puissance n.
    """
    if(n <= 1):
        return 1

    return x * puissance(x, n-1)

finEx()#------------------------------------------------------------------------

ex(18,"""Que calcule la fonction suivante où x est un réel et n un entier ?
""")

print("La fonction p est une optimisation de la fonction x puissance n.")

finEx()#------------------------------------------------------------------------

ex(19,"""
""")

def fibo1(n):
    """Si n est un entier positif, renvoie le n-ième terme de la suite de
    Fibonacci, sinon renvoie False.

    On calcule le terme à l'aide d'une fonction récurrente.
    
    Args:
        n (int): Rang attendu de la suite de Fibonacci

    Return:
        (bool) / (int): False si n n'est pas un entier positif, le n-ième terme
        sinon.
    """
    if(type(n) != int or n < 0):
        print("Erreur")
        return False

    if(n <= 1):
        return 1
    
    return fibo(n-1) + fibo(n-2)

def fibo2(n):
    """Si n est un entier positif, renvoie le n-ième terme de la suite de
    Fibonacci, sinon renvoie False.

    On calcule le terme à l'aide d'une fonction itérative.
    
    Args:
        n (int): Rang attendu de la suite de Fibonacci

    Return:
        (bool) / (int): False si n n'est pas un entier positif, le n-ième terme
        sinon.
    """
    if(type(n) != int or n < 0):
        print("Erreur")
        return False

    if(n <= 1):
        return 1

    fib = [1,1]

    while n != 0:
        fib.append(fib[-1] + fib[-2])
        n -= 1
    
    return fib[-1]

finEx()#------------------------------------------------------------------------

ex(20,"""Importer le module time et faire des mesures d'efficacité en temps """
    """des deux fonctions fibo1 et fibo2 à l'aide de la fonction time(). """
    """Comment expliquer ces différences ?
""")

from time import time

tps = int(time());
fibo1(10000);
print(time() - tps);

tps = int(time());
fibo2(10000);
print(time() - tps);

print("L'enregistrement dans une liste ralentit le processus.")

finEx()#------------------------------------------------------------------------


