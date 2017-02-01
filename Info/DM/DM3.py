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

def sc(u0,n):
    """Renvoie le n-ième terme de la suite SC.

    Args:
        u0 (int): Valeur du premier terme de la suite.
        n (int): Rang de la valeur attendue.

    Return:
        (int): n-ième terme de la suite SC.
    """
    u = u0
    
    while(n > 0):
        if(u % 2):
            u = 3 * u + 1
        u //= 2
        n -= 1

    return u

def trajectoire(u0):
    """Renvoie la trajectoire de la suite SC de valeur initiale u0.

    Args:
        u0 (int): Valeur du premier terme de la suite.

    Return:
        (list of int): Trajectoire de SC.
    """
    if(u0 == 1):
        return [1]
    
    u = u0
    
    if(u0 % 2):
        u = 3 * u + 1
    u //= 2
    
    return [u0] + trajectoire(u)

def temps_de_vol(u0):
    """Renvoie le temps de vol de la suite SC.

    Args:
        u0 (int): Valeur du premier terme de la suite.

    Return:
        (int): Temps de vol de la suite SC.
    """
    return len(trajectoire(u0)) - 1


def temps_de_vol_alt(u0):
    """Renvoie le temps de vol en altitude de la suite SC.

    Args:
        u0 (int): Valeur du premier terme de la suite.

    Return:
        (int): Temps de vol en altitude de la suite SC.
    """
    temps = 0
    traj = trajectoire(u0)

    for tps,alt in enumerate(traj):
        if(alt < u0):
            return tps - 1
    return False

def maximum(liste):
    """Renvoie la valeur max de la liste.

    Args:
        liste (list of int): Liste à traiter.

    Return:
        (int): Valeur maximale de la suite.
    """
    a = liste[0]

    for elt in liste:
        if(elt > a):
            a = elt
    return a

def alt_max(u0):
    """Renvoie l'altitude maximale de la suite SC.

    Args:
        u0 (int): Valeur du premier terme de la suite.

    Return:
        (int): Altitude maximale de la suite SC.
    """
    return maximum(trajectoire(u0))

def reverseListe(liste):
    """Renvoie la liste renversée.

    Args:
        liste (list): Tableau à renverser.

    Return:
        (list): Liste renversée.
    """
    return liste[::-1]
    
def infos_sc(N):
    """Renvoie les temps de vol, les altitudes maximales et les temps de vol en
    altitude de toutes les suites SC ayant pour valeur initiale chacun des
    entiers inférieurs à N.

    Args:
        N (int): Borne supérieure des valeurs initiales des listes SC.

    Return:
        (tuple of list): Temps de vol, altitudes maximales et temps de
        vol en altitude des listes SC déterminées.
    """

    # Méthode demandée :
    #SC = list(range(N+1))
    #return ([temps_de_vol(sc) for sc in SC],
    #        [alt_max(sc) for sc in SC],
    #        [temps_de_vol_alt(sc) for sc in SC])
    
    # Méthode optimisée
    SC = [trajectoire(u) for u in range(1,N+1)]
    tpsVol = [len(sc) for sc in SC]
    tpsVolAlt = []

    for u,traj in enumerate(SC):
        traj = reverseListe(traj)
        for tps,alt in enumerate(traj):
            if(alt > u):
                tpsVolAlt.append(tpsVol[u] - tps - 1)

    return (tpsVol, [maximum(sc) for sc in SC], tpsVolAlt)

def moyenne(liste):
    """Renvoie la moyenne de la liste liste.

    Args:
        liste (list): Liste à traiter.

    Return:
        (int): Moyenne de la liste.
    """
    somme = 0

    for i in liste:
        somme += i

    return somme / len(liste)

def positions(liste, x):
    """Renvoie les positions de x dans la liste.

    Args:
        liste (list): Liste à fouiller.
        x (val): Valeur à rechercher.

    Return:
        (list) / (None): Liste des positions de x, None si x n'appartient pas à
            la liste.
    """
    if(not x in liste):
        return None

    pos = []

    for i,elt in enumerate(liste):
        if(elt == x):
            pos.append(i)

    return pos

#-------------------------------------------------------------------------------

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

def tri(liste):
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

def isCroissante(liste):
    """Renvoie si la liste est croissante ou non.

    Args:
        liste (list): Liste à étudier

    Return:
        (bool): True si la liste est croissante, False sinon.
    """
    for i in range(1, len(liste)):
        if(liste[i-1] > liste[i]):
            return False
    return True

def isDecroissante(liste):
    """Renvoie si la liste est décroissante ou non.

    Args:
        liste (list): Liste à étudier

    Return:
        (bool): True si la liste est décroissante, False sinon.
    """
    for i in range(1, len(liste)):
        if(liste[i-1] < liste[i]):
            return False
    return True

#-------------------------------------------------------------------------------

#def chiffre(n):
#    """Renvoie une liste contenant les chiffres de n.
#
#    Args:
#        n (real): Nombre à décomposer.
#
#    Return:
#        (list): Chiffres de n.
#    """
#    if(n == 0):
#        return []
#    a = n
#    i = 1

#    while(a >= 10):
#        a /= 10
#        i /= 10
#    a = int(a)
#    print(n,a)
#    
#    return [a] + chiffre(int(n - a/i))

def chiffre(n):
    """Renvoie une liste contenant les chiffres de n.

    Args:
        n (real): Nombre à décomposer.

    Return:
        (list): Chiffres de n.
    """
    chiffres = []

    while(n != 0):
        chiffres.append(n % 10)
        n //= 10

    return reverseListe(chiffres)

def nmax(n):
    """Renvoie le nombre max que l'on puisse composer à l'aide des chiffres de n.

    Args:
        n (int): Entier à exploiter.

    Return:
        (int): Entier maximal composé des décimales de n.
    """
    nbr = tri(chiffre(n))
    s = 0

    for i,c in enumerate(nbr):
        s += c*10**i

    return s

def nmin(n):
    """Renvoie le nombre min que l'on puisse composer à l'aide des chiffres de n.

    Args:
        n (int): Entier à exploiter.

    Return:
        (int): Entier minimal composé des décimales de n.
    """
    nbr = reverseListe(tri(chiffre(n)))
    s = 0

    for i,c in enumerate(nbr):
        s += c*10**i

    return s

def drk(n):
    """Renvoie la différence de nmax(n) et nmin(n).

    Args:
        n (int): entier à étudier.

    Return:
        (int): Différence de nmax(n) et nmin(n).
    """
    return nmax(n) - nmin(n)

def drk_itere(i,n):
    """Renvoie la i-ème itérée de la fonction drk évaluée en n.

    Args:
        i (int): Nombre d'itération demandé.
        n (int): Valeur intiale.

    Return:
        (int): i-ème itérée de la fonction drk en n.
    """
    if(i <= 0):
        return n

    return drk_itere(i-1, drk(n))

def suiteDrk(n):
    """Renvoie les termes de la suite drk commençant par n.
    On considère que la suite est terminée pour Uk+1 = Uk.

    Args:
        n (int): Entier de départ.

    Return:
        (list): Valeurs prises par la suite avant de se stabiliser.
    """
    val = [n]

    while(n != drk(n)):
        n = drk(n)
        val.append(n)

    return val

#===============================================================================
print("\n\tDM1 - Informatique")
print("\t   PTSIB 15/16")
print("\t  Lesecq Damien")

ex(1,"SC")

(tpsVol, altMax, tpsVolAlt) = infos_sc(10**4)

# Question 1
q(1, "Quel est l'entier N <= 10^4 qui a le temps de vol le plus long ?")

res("L'entier inférieur à 10^4 qui a le temps de vol le plus long est : {}.".format(
    positions(tpsVol, maximum(tpsVol))))


# Question 2
q(2,"Combien d'entiers N <= 10^4, ont un temps de vol de 24, de 63, de 133 ?")

res("""Il y a :
(a) {} entiers inférieurs à 10^4 qui ont un temps de vol de 24.
(b) {} entiers inférieurs à 10^4 qui ont un temps de vol de 63.
(c) {} entiers inférieurs à 10^4 qui ont un temps de vol de 133.""".format(
    len(positions(tpsVol,24)), len(positions(tpsVol,63)), len(positions(tpsVol,133))
    ))


# Question 3
q(3,"Quel est l'entier N <= 10^4 qui a le temps de vol en altitude le plus long ?")

res("L'entier inférieur à 10^4 qui a le temps de vol en altitude le plus long "+
    "est : {}.".format(positions(tpsVolAlt, maximum(tpsVolAlt))))


# Question 4
q(4,"Quel est le premier entier qui a un temps de vol en altitude de 87 ?")

res("Le premier entier à avoir un temps de vol de 87 est : {}.".format(
    (positions(tpsVol, 87))[0]))


# Question 5
q(5,"Quel est l'entier N <= 10^4 qui a la plus grande altitude maximale ?")
res("L'entier inférieur a 10^4 qui à l'altitude maximale la plus grande est : {}.".format(
    positions(altMax, maximum(altMax))
    ))


# Question 6
q(6, "Pour les entiers compris entre 1 et 104, quels sont le temps de vol, le "+
    "temps de vol en altitude et l'altitude maximale moyen(ne) ? Les résultats "+
    "seront donné sous forme d'entiers.")

res("""Pour les entiers inférieurs a 104 :
(a) L'altitude maximale moyenne est d'environ {}
(b) Le temps de vol en altitude moyen est d'environ {}
(c) Le temps de vol moyen est d'environ {}
""".format(int(moyenne(altMax)),
    int(moyenne(tpsVolAlt)),
    int(moyenne(tpsVol))
    ))

finEx()#------------------------------------------------------------------------

ex(2,"DRK")

sDrk1 = [drk(i) for i in range(1000, 10000)]
sDrk = [None for i in range(1000, 10000)]

def completeSDrk(n):
    """Complete le tableau sDrk représentant les suites.
    On opère de manière optimisée afin de ne pas calculer deux fois la même chose
    """
    global sDrk

    if(n == 6174 or n == 0):
        return []
    if(n == 999):
        return [0]

    if(sDrk[n-1000] != None):
        return sDrk[n-1000]
    
    sDrk[n-1000] = [sDrk1[n-1000]] + completeSDrk(sDrk1[n-1000])
    return sDrk[n-1000]

for i in range(1000, 10000):
    if(i%1000==0):
        print("[Debug:]",i)
    completeSDrk(i)

for i in range(1000,10000):
    if(i == 6174):
        sDrk[i-1000] = [6174]
        continue
    sDrk[i-1000] = [i] + sDrk[i-1000]
print("[Debug:] Init done.")



# Question 1
q(1, "Montrer que l'ensemble E des images de la fonction drk pour n "+
    "appartenant à |[1000, 9999]| est E = |[1000, 9999]| U {0, 999}.")

arr = tri(list(set(sDrk1)))
print("\nL'enchainement des fonctions set, list et tri permettent de transformer "+
    "la liste des valeurs en un ensemble sans répétiton et trié.")
print(arr)
print("Les deux premières valeurs sont 0 et 999. Ensuite, la liste étant "+
    "triée, et sa dernière valeur étant inférieure à 9999, on peut dire que :")
res("L'ensemble des valeurs prises par la fonction est bien E.")


# Question 2
q(2, "Quels sont les points fixes de la fonction drk, pour n appartenant à E ?")

arr = tri(list(set([tab[-1] for tab in sDrk])))
res("Les points fixes de la fonction drk sont : {}.".format(arr))


# Question 3
q(3, "Pour combien d'entiers N appartenant à |[1000, 9999]|, la suite DRK "+
    "est-elle croissante ? décroissante ?")

arr = [0,0]
for sdrk in sDrk:
    if(isCroissante(sdrk)):
        arr[0] += 1
    if(isDecroissante(sdrk)):
        arr[1] += 1
res("La suite DRK est croissante pour {} entiers et décroissante pour {} entiers.".format(arr[0],arr[1]))

# Question 4
q(4,"Quel est le temps de vol moyen d'un entier N appartenant à |[1000, 9999"+
    "]| ? On retournera un entier.")

tpsVolDrk = [len(i)-1 for i in sDrk]
res("Le temps de vol moyen est : {}.".format(moyenne(tpsVolDrk)))


# Question 5
q(5,"Quel est le temps de vol maximum d'un entier N  appartenant à |[1000, 99"+
    "99]| ? On le notera tmax.")

res("Le temps de vol maximum est : {}.".format(maximum(tpsVolDrk)))


# Question 6
q(6,"Pour chaque temps de vol inférieur ou égal à tmax donner le nombre "+
    "d'entiers N appartenant à |[1000, 9999]|, dont c'est le temps de vol. "+
    "Quel est le temps de vol le plus fréquent ?")

arr = tri(list(set(tpsVolDrk)))
arr = [[len(positions(tpsVolDrk, x)) for x in arr], arr]
txt = ''
for i in range(len(arr[0])):
    txt += " - {} entiers ont un temps de vol de {}.\n".format(arr[0][i],arr[1][i])
res(str(txt))
print("Le temps de vol le plus fréquent est : {}.".format(arr[1][positions( arr[0], maximum(arr[0]) )[0]]))


# Question 7
q(7,"Quelle est l'altitude maximale la plus grande pour un entier N "+
    "appartenant à |[1000, 9999]| ?")

res("L'altitude maximale la plus grande est : {}.".format(maximum([maximum(i) for i in sDrk])))

finEx()#------------------------------------------------------------------------
#===============================================================================
