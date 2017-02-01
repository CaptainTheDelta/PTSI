# -*- coding: utf-8 -*-
"""
@author: Lesecq - Damien
"""
# DM2 - Informatique PTSI-B 2016/17

import math

def isPrime(n):
    if n in [0,1] or (n != 2 and n % 2 == 0):
        return False
    for k in range(3,int(n**(1/2))+1,2):
        if n % k == 0:
            return False
    return True
#===============================================================================

# Exercice 2 : Des questions

# Question 1

def liste_premiers_dans(a,b):
    """Renvoie les nombres premiers compris entre a et b.
    
    Args:
        a (int): La borne inférieure.
        b (int): La borne supérieure.

    Return:
        (list of int): Liste des nombres premiers.
    """
    return [i for i in range(a,b+1) if isPrime(i)]

# Question 2

def nb_de_premiers_dans(a,b):
    """Renvoie le nombre de nombres premiers compris entre a et b.
    
    Args:
        a (int): La borne inférieure.
        b (int): La borne supérieure.
    
    Return:
        (int): Nombre de nombres premiers.
    """
    return len(liste_premiers_dans(a,b))

# Question 3.a

def bolowitz(n):
    """Renvoie les n premiers nombres premiers.
    
    Args:
        n (int): Nombre de premiers désirés.
    
    Return:
        (list of int): Liste des nombres premiers.
    """
    k = 1
    premiers = []
    if(n >= 1):
        premiers.append(2)
    while len(premiers) < n:
        k += 2
        if(isPrime(k)):
            premiers.append(k)
    return premiers

# Question 3.b

def leonard(n):
    """Renvoie la somme des n premiers nombres premiers.
    
    Args:
        n (int): Valeur jusqu'à laquelle on va faire la somme.
    
    Return:
        (int): Somme.
    """
    return sum(bolowitz(n))

# Question 3.c

def andrica(n):
    """Renvoie la liste contenant la différence de la racine des n nombres 
    remiers par la racine des nombres premiers différent.

    Cette fonction renvoie la liste des différences de premiers de la forme:
    sqrt(Pn) - sqrt(Pn-1), Pn étant un nombre premier, et Pn-1 le nombre premier
    précédent.
    
    Args:
        n (int): Nombre de premiers sur lesquels on veut opérer.
    
    Return:
        (list of float): liste des différences opérées.
    """
    p = bolowitz(n)
    return [p[i]**(1/2) - p[i-1]**(1/2) for i in range(1, n)]

# Question 3.d

def sheldon(n):
    """Renvoie le nombre de premiers inférieurs à n qui restent premiers si on
    leur ajoute 4.

    On renvoie le nombre de k tels que k premier et k + 4 premier.
    
    Args:
        n (int): Borne supérieure de l'intervalle des nombres premiers testés.
    
    Return:
        (int): Nombre de premiers vérifiant la propriété.
    """
    c = 0
    premiers = liste_premiers_dans(0,n)
    for k in premiers:
        if k+4 in premiers:
            c += 1
    return c

# Question 3.e

def penny(n):
    """Renvoie les n premiers nombres premiers.
    
    Args:
        n (int):  
    
    Return:
        (list of int): Liste des n premiers nombres premiers.
    """
    p = []
    somme = 0
    premiers = liste_premiers_dans(0,n)
    for a in range(10):
        for b in range(a,10):
            somme = a**2 + b**2
            if(somme < 100 and somme in premiers):
                p.append(a**2 + b**2)
    return sorted(p)

#def penny(n):
#    return [ (a,b) for a in range(ceil((n/2)**(1/2))) for b in range(a, ceil(n**(1/2))) if isPrime(a**2 + b**2)]


# Question 6.a

def isBeruntung(a):
    """Vérifie que a est beruntung.

    a est beruntung si pour tout 0 <= n < a-1, n**2 + n + a est premier. 
    
    Args:
        a (int): Nombre à tester.
    
    Return:
        (bool): True si a est beruntung, False sinon.
    """
    if(a < 2):
        return False
    for n in range(a-1):
        if(not isPrime(n**2 + n + a)):
            return False
    return True

# Question 6.b

def liste_beruntung(n):
    """Renvoie la liste des beruntung inférieurs à n.
    
    Args:
        n (int): Borne supérieure de l'intervalle des nombres à tester.
    
    Return:
        (list of int): Nombres beruntung inférieurs à n.
    """
    return [i for i in range(1,n+1) if isBeruntung(i)]

# Exercice 3

# Question 1.a

def suiteD(n):
    """Renvoie les n premiers termes de la suite D.
    
    Args:
        n (int): Nombre attendu de termes de la suite.
    
    Return:
        (liste of int): Liste des n premiers termes de la suite D. 
    """
    D = [0]
    if(n >= 1):
        D.append(1)
    if(n >= 2):
        D.append(1)
    i = 3
    while i <= n:
        D.append(D[i - D[i-1]] +D[i - D[i-2]])
        i += 1
    return D[1:]

# Question 2

def G(n):
    """Renvoie la suite G(n).

    La suite G(n) est définie par : G = (G(n))n, G est croissante et G(1)=1 et
    pour n >= 1, G(n) est le nombre de fois que l'entier n apparait dans la 
    suite G(n).
    
    Args:
        n (int): Rang auquel on désire la suite.
    
    Return:
        (list of int): Liste des termes de G(n).
    """
    if(n == 1):
        return [1]
    
    g = G(n-1) + [n]
    return g + [n for i in range(1, g[n-1])]

def suiteG(n):
    """Renvoie les n premiers termes de la suite (G).
    
    Args:
        n (int): Nombre attendu de termes de la suite.
    
    Return:
        (list of int): Liste des n premiers termes de (G).
    """    
    return G(math.ceil((n+1)/2))[:n]

#===============================================================================
def ex(n):
    print("\n\n-------------Exercice {}-------------".format(n))

def q(n):
    print("\nQuestion n°{}".format(n))
#===============================================================================

print(              "\n\tDM1 - Informatique\n"
                        "\t   PTSIB 16/17\n"
                        "\t  Lesecq Damien")

ex(2) #                    ------------------

q(1) #--------------------------------------------------------------------------
print("Les nombres premiers inférieurs à 100 sont :\n",
    liste_premiers_dans(0,100))

q(2) #--------------------------------------------------------------------------
f7 = math.factorial(7)
print("Dans l'intervalle [7!; 7! + 6] il y a", nb_de_premiers_dans(f7,f7+6),
    "nombres premiers.")

q("3.b") #----------------------------------------------------------------------
print("La somme des 111 premiers nombres premiers est :", leonard(111))

q("3.c") #----------------------------------------------------------------------
for a in andrica(60000):
    if(a > (11**(1/2) - 7**(1/2))):
        print("La conjecture d'Andrica n'est pas vérifée pour les 60 000 "
            "premiers nombres premiers.")
        break
else:
    print("La conjecture d'Andrica est vérifée pour les 60 000 premiers "
        "nombres premiers.")

q("3.d") #----------------------------------------------------------------------
print("Il y a", sheldon(1000), "entiers k plus petits que 1000 tels que k et "
        "k + 4 sont premiers.")

q("3.e") #----------------------------------------------------------------------
print("Les nombres premiers p inférieurs à 100 qui vérifent la propriétée "
    "sont :", penny(100))

q(4) #--------------------------------------------------------------------------
for n in range(40):
    k = n**2 + n + 41
    print("P({})={}".format(n,k), end='')
    if(isPrime(k)):
        print(" est premier.")
    else:
        print(" n'est pas premier.")

q(5) #--------------------------------------------------------------------------
i=1
compteur = 0
while i <= 10**4:
    if((math.factorial(i-1)+1)%i == 0):
        compteur += 1
    i += 1
if(compteur == nb_de_premiers_dans(0,10**4)):
    print("Le théorème de Wilson est vérifié jusqu'à 10^4.")
else:
    print("Le théorème de Wilson n'est pas vérifié jusqu'à 10^4.")

q("6.c") #----------------------------------------------------------------------
print("La liste des nombres beruntung inférieurs à 1000 est :",
    liste_beruntung(1000))

ex(3) #                    ------------------

q("1.a") #----------------------------------------------------------------------
print("La liste des 30 premiers termes de la suites D est :\n", suiteD(30))

q("1.b") #----------------------------------------------------------------------
print("Challenge Accepted !")

q(2) #--------------------------------------------------------------------------
print("La liste des 30 premiers termes de la suites G est :", suiteG(30))

#===============================================================================
input("\nFin du DM")