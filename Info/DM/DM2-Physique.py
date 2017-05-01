import numpy as np
import matplotlib.pyplot as plt

# --------------------------------- Constantes ---------------------------------


m,g,k,l0,r,e,p = [None] * 7


# --------------------------------- Fonctions ----------------------------------


def equilibre(m,g,k,l0):
    """Renvoie la position d'équilibre z_equ.

    Args:
        m (real): Masse.
        g (real): Accélération de la pesanteur
    """
    return m * g / k + l0


def euler2ressort(z0,v0,t0,tf,h):
    """Renvoie trois listes des valeurs prises par t, z et v.

    Args:
        z0 (real): Hauteur initiale.
        v0 (real): Vitesse initiale.
        t0 (real): Temps de départ.
        tf (real): Temps de fin.
        h (real): Pas séparant les valeurs de t.
    """
    t = np.arange(t0,tf,h)
    n = len(t)

    z = [z0]
    v = [v0]

    for i in range(n-1):
        z += [z[i] + h * v[i]]
        v += [v[i] + h * (k / m) * (l0 - z[i])]

    return t,z,v


def euler2lapins(L,R,t0,tf,h):
    """Renvoie trois listes des valeurs prises par t, z et v.

    Args:
        L (real): Nombre de lapins initial.
        R (real): Nombre de renards initial.
        t0 (real): Temps de départ.
        tf (real): Temps de fin.
        h (real): Pas séparant les valeurs de t.
    """
    t = np.arange(t0,tf,h)
    n = len(t)

    l = [L]
    re = [R]

    for i in range(n-1):
        l += [l[i] * (1 + h * r - h * e * re[i])]
        re += [re[i] * (1 - h * k + h * p * l[i])]

    return t,l,re


def constantes(part):
    """Initialise les constantes en fonctions de la partie du DM.

    Args:
        part (int): Partie du dm.
    """
    global m,g,k,l0,r,e,p
    
    if(part == 1):
        m = 0.2
        g = 9.81
        k = 10
        l0 = 10

    elif(part == 2):
        r = 0.1
        k = 0.04
        e = 0.0005
        p = 0.00004


def graphe(x,y,axes=True):
    """Affiche le graphe des tableaux de valeurs de y en fonction de x.

    Args:
        x (list): Liste de valeurs en abscisses.
        y (dict): Dictionnaire de liste de valeurs en ordonnées.
    """
    colors = ['r', 'b', 'g', 'k', 'c', 'm', 'y', 'w']
    
    for i,f in y.items():
        plt.plot(x,f,color=colors.pop(0))

    if(axes):
        plt.axhline(color='black')
        plt.axvline(color='black')

    plt.legend(y.keys(),loc='upper right')
    plt.show()
    plt.close()


# ---------------------------------- Tableaux ----------------------------------


constantes(1)
z0 = 20
v0 = 0
t0 = 0
tf = 2
h = 1e-4

t,z,v = euler2ressort(z0,v0,t0,tf,h)

zeq = equilibre(m,g,k,l0)
n = len(t)

Ec = [1/2 * m * vitesse ** 2 for vitesse in v]
Eepp = [m * g * altitude for altitude in z]
Epe = [1/2 * k * (altitude - zeq) ** 2 for altitude in z]
E = [Ec[i] + Eepp[i] + Epe[i] for i in range(n)]

constantes(2)
tf = 365
h = 0.01
L = 2000
R = 600

t2,l,r = euler2lapins(L,R,t0,tf,h)


# ================================ Compte-rendu ================================


# Les réponses nécessitants des équations auront le droit à du latex.

# Q2:
"\frac{dz(t)}{dt} = v(t)"
# Q3 :
"\frac{dv(t)}{dt} + \frac{k}{m}z(t) = \frac{k}{m}z_{eq}"
# Q4 :
"\ddot{z}(t) + \frac{k}{m}z(t) = \frac{k}{m}z_{eq}"
# Q5 :
"v_{n+1} = v_{n} + h * \frac{k}{m} (l_{0} - z_{n}"
"z_{n+1} = z{n} + h * v_{n}" 




print("""               DM - Informatique (physique)
                           PTSIB
                       Lesecq Damien

Système masse-ressort
=====================

Allure de la position et de la vitesse :""")

graphe(t,{'p':z,'v':v})

print("Portrait de phase :")

graphe(z,{'v':v})

print("Allure des énergies :")

graphe(t,{'E':E,'Ec':Ec,'Eepp':Eepp,'Epe':Epe})

print("Commentaire :\nOn remarque que l'énergie mécanique est constante, "+
    "comme on pouvait s'y attendre. On remarque aussi que les énergies "+
    "cinétiques et potentielles sont périodiques.")

print("""
Système lapins-renards
======================

Evolution des populations :""")

graphe(t2,{'L':l,'R':r})

print("On remarque que le nombre de lapins est bien plus important que celui "+
    "des renards.")