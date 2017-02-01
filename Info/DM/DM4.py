# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 20:10:42 2016

@author: Lesecq - Damien
"""
# DM3 - Informatique PTSI-B 2016/17

#===============================================================================
def ex(nbr,consigne):
    a = ''
    if(nbr >= 10):
        a = '-'
    print("-------------Exercice n°{}-------------\n{}\n\
             ------------{}".format(nbr, consigne, a))

def q(nbr,consigne):
    print("\n\nQuestion {}: {}".format(nbr,consigne))

def res(conclusion):
    print("\nrésultat :", conclusion, sep='\n')

def finEx():
    input("\nAppuyez sur entrer...")
#===============================================================================

def echange(liste,i,j):
    """Echange les éléments aux rangs i et j de la liste. 

    Args:
        liste (list): Liste à modifier.
        i (int): Indice du premier élément.
        j (int): Indice du deuxième élément.
    """
    liste[i], liste[j] = liste[j], liste[i]

def pos_min(liste):
    """Renvoie l'indice du plus petit élément de la liste.

    Args:
        liste (list): Liste non vide.

    Return:
        (int): Indice du plus petit élément.
    """
    m = 0

    for i,elt in enumerate(liste):
        if(liste[m] > elt):
            m = i

    return m

def inserer(x,liste,i):
    """Renvoie la liste avec l'élément x à la position i.

    Args:
        x (val): Valeur à placer.
        liste (list): Liste dans laquelle on place .
        i (int): Indice auquel placer l'élément x.

    Return:
        (list): Liste modifiée.
    """
    return liste[:i] + [x] + liste[i:]

def copie_liste(liste):
    """Renvoie une copie de la liste.

    Args:
        liste (list): Liste à copier.

    Return:
        (list): Copie de la liste.
    """
    return liste[:]

def Tri(liste):
    """Renvoie la liste liste triée.

    Args:
        liste (list): Liste à trier.

    Return:
        (list): Liste triée.
    """
    l = copie_liste(liste)

    for i in range(len(l)):
        echange(l, i, i + pos_min(l[i:]))
    
    return l

def Tri2(liste):
    """Renvoie la liste liste triée.

    Args:
        liste (list): Liste à trier.

    Return:
        (list): Liste triée.
    """
    n = len(liste)
    l = copie_liste(liste)
    listeEnOrdre = False

    while not listeEnOrdre:
        listeEnOrdre = True
        for j in range(n - 1):
            if(l[j] > l[j+1]):
                listeEnOrdre = False
                echange(l,j,j + 1)

    return l

def ajouter(x,liste_triee):
    """Ajoute x dans la liste triée à la bonne place afin de conserver l'ordre.

    Args:
        x (int): élément à insérer.
        liste (list): Liste à modifier.
    """
    l = len(liste_triee)
    i = 0

    while(i < l):
        if(liste_triee[i] > x):
            break
        i += 1
    
    return inserer(x,liste_triee,i)

def Tri3(liste):
    """Renvoie la liste liste triée.

    Args:
        liste (list): Liste à trier.

    Return:
        (list): Liste triée.
    """
    l = []

    for elt in liste:
        l = ajouter(elt,l)

    return l

def Tri4(liste):
    """Renvoie la liste liste triée.

    Args:
        liste (list): Liste à trier.

    Return:
        (list): Liste triée.
    """
    if(len(liste) <= 1):
        return liste

    test = liste[0]
    inf = []
    equ = []
    sup = []

    for elt in liste:
        if(elt < test):
            inf.append(elt)
        elif(elt == test):
            equ.append(elt)
        else:
            sup.append(elt)
    
    if(len(inf) == 0 and len(sup) == 0):
        return equ
        
    return Tri4(inf) + Tri4(equ) + Tri4(sup)


def minimumEntre(a,b):
    return 0 if a < b else 1

def somme(liste1,liste2):
    """Renvoie une liste triée des éléments des listes 1 et 2.

    Args:
        liste1 (list): Liste à sommer.
        liste2 (list): Liste à sommer.

    Return:
        (list): Liste triée.
    """
   #n = len(liste1) + len(liste2)
   #liste = [copie_liste(liste1),copie_liste(liste2)]
   #l = []

   #while True:
   #    if(len(liste[0]) == 0):
   #        l += liste[1]
   #        break
   #    elif(len(liste[1]) == 0):
   #        l += liste[0]
   #        break
   #    else:
   #        m = minimumEntre(liste[0][0], liste[1][0])
   #        l.append(liste[m][0])
   #        liste[m] = liste[m][1:]

   #return l

    l = []
    l1 = copie_liste(liste1)
    l2 = copie_liste(liste2)
    ll1 = len(l1)
    ll2 = len(l2)

    while(ll1 + ll2 != 0):
        if(ll1 == 0):
            l += l2
            break
        elif(ll2 == 0):
            l += l1
            break
        else:
            if(l1[0] < l2[0]):
                l.append(l1[0])
                l1 = l1[1:]
                ll1 -= 1
            else:
                l.append(l2[0])
                l2 = l2[1:]
                ll2 -= 1

    return l

def Tri5(liste):
    """Renvoie la liste liste triée.

    Args:
        liste (list): Liste à trier.

    Return:
        (list): Liste triée.
    """
    l = len(liste)
    if(l == 1):
        return liste

    m = int(l/2)

    return somme(Tri5(liste[:m]), Tri5(liste[m:]))

#===============================================================================
