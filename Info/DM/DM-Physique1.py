import numpy as np
import matplotlib.pyplot as plt
from math import pi

# -------------------------------- Préliminaire --------------------------------

def euler(f,t0,tf,y0,h):
    """Renvoie la liste des valeurs prises par x et par y.

    Args:
        f (fct): Fonction à deux arguments.
        t0 (real): Valeur minimale de t.
        tf (real): Valeur maximale de t.
        y0 (real): Valeur initiale de y.
        h (real): Pas séparant chaque valeur de x.

    Return:
        (tuple): Couple de la liste des valeurs prise par x et par y.
    """
    x = np.arange(t0,tf,h)
    n = len(x)
    y = [y0]
    
    for i in range(n-1):
        y += [y[i] + h * f(y[i], x[i])]

    return x,y

# -------------------------- Étude de la chute libre ---------------------------

def v_libre(y,t):
    """Renvoie la dérivée de v au moment t.

    Args:
        y (fct): Fonction à dériver.
        t (real): Valeur à donner à la dérivée.

    Return:
        (real): Nombre y'(t).
    """
    return - 9.81


def z_libre(Y,t):
    """Renvoie le vecteur F (sorte de dérivée de Y: [z,v]).

    Args:
        Y (list): Couple position, vitesse.

    Return:
        (list): Dérivée du vecteur Y.
    """
    return [Y[1], - 9.81]


def euler2(f,t0,tf,y0,h):
    """Renvoie la liste des valeurs prises par le temps et par Y.

    Args:
        f (fct): Fonction à deux arguments.
        t0 (real): Valeur minimale de t.
        tf (real): Valeur maximale de t.
        y0 (list): Valeur initiale de Y.
        h (real): Pas séparant chaque valeur de x.

    Return:
        (tuple): Couple de la liste des valeurs prise par le temps et par Y.
    """
    x = np.arange(t0,tf,h)
    n = len(x)
    Y = [y0]
    
    for i in range(n-1):
        y0, y1 = Y[-1][0],Y[-1][1]
        yp = z_libre(Y[-1],x[i])
        
        y0 += h * yp[0]
        y1 += h * yp[1]
        
        Y.append([y0,y1])

    return x,Y


def phase(e):
    """Affiche le diagramme de phase.

    Args:
        e (list): Tableau renvoyé par euler2.
    """
    z = [e[1][k][0] for k in range(len(t))]
    v = [e[1][k][1] for k in range(len(t))]

    plt.plot(v,z,color='r',marker='x')

    plt.ylabel('z')
    plt.xlabel("v")

    plt.show()
    plt.close()

# --------------------------------- Constantes ---------------------------------

pa = 1.3
p = 8000
r = 0.02
alpha = 10
beta = 38
g = 9.81

t0 = 0
tf = 0.1
v0 = 0
h = 0.001

# ------------------------------- Hypothèse n°1 --------------------------------

g_2 = g * (pa/p - 1)

m = p * (4/3) * pi * (r ** 3)
k = alpha / m
k_2 = beta / m


def chute_1(y,t):
    """Renvoie y'.

    Args:
        y (fct):
    """
    return - k * y + g_2

# ------------------------------- Hypothèse n°2 --------------------------------

def chute_2(y,t):
    """Renvoie y'.

    Args:
        y (fct):
    """
    return - k_2 * y + g_2

# ---------------------------------- Réponses ----------------------------------




print("""# DM - Informatique (physique)

# Préliminaires

Q1: Les formules de récurrence de la méthode d'Euler explicite sont données par : 
    Yk+1 = Yk + h * f(Xk,Yk)
    Xk+1 = Xk + h
    Xk = X0 + h * k
Q2: La fonction euler est : BLA (elle apparaît d'ailleurs dans le code).

# Étude de la chute libre

Q1: L'équation différentielle est donnée par l'application du PFD. On arrive à dv/dt = -g.
Q2: La fonction v_libre est : BLA (elle apparaît d'ailleurs dans le code).""")


e = euler(v_libre,0,2,0,0.1)
p = "f : v_libre, t0 = 0, tf = 2, y0 = 0, h = 0.1"

print("Q3: Voici la liste des vitesses v(t) : {lstV1}, celle-ci a été obtenue\
avec les paramètres {param1}.".format(lstV1=e[1],param1=p))

print("""Q4: L'équation différentielle est donnée par définition. On arrive à dz/dt = v.
Q5: La masse n'intervient pas dans le résultat final.
Q6: Le vecteur F est le vecteur dérivé de Y.
Q7: La fonction z_libre est : BLA (elle apparaît d'ailleurs dans le code).""")

e = euler2(z_libre,0,2,[10,0],0.1)

t = e[0]
z = [e[1][k][0] for k in range(len(t))]
v = [e[1][k][1] for k in range(len(t))]

p = "f : z_libre, t0 = 0, tf = 2, Y = [10,0], h = 0.1"

print("Q8: Voici la liste des positions z(t) : {lstZ1}, celle-ci a été obtenue \
avec les paramètres {param2}.".format(lstZ1=z,param2=p))

print("Q9: Voici les graphes de z(t) et v(t).")

plt.plot(t,v,color='b',marker='+')
plt.plot(t,z,color='r',marker='x')
plt.legend(['vitesse','position'],loc='upper right')

plt.show()
plt.close()

print("Q10: Ci-dessous le premier portrait de phase.")
phase(euler2(z_libre,0,20,[10,10],0.1))

print("Q11: Le deuxième.")
phase(euler2(z_libre,0,20,[10,-10],0.1))

print("Q12: Le troisième.")
phase(euler2(z_libre,0,20,[20,10],0.1))

print("Q13: Le dernier.")
phase(euler2(z_libre,0,20,[20,-10],0.1))

print("""Q14: Je ne suis pas parvenu à identifier les graphes.
En m'appuyant sur mes graphes je trouve que la vitesse au moment de l'impact est la plus importante pour le dernier.

# Étude dynamique d'une chute avec frottements

Q1: La masse m est donnée par (4/3) * pi * (r^3) * rhô
Q2: g2 est donnée par g * (Pair/P - 1)
Q3: On a : k = alpha/m
Q4: Et : k2 = beta/m

# Hypothèse n°1 sur les frottements

Q1: L'équation différentielle est donnée par l'application du PFD. On arrive à dv/dt = - k * v - g_2.
Q2: Fonction qui apparaît dans le code.""")

# On prend v = y
p = "f : chute_1, t0 = 0, tf = 0.1, v0 = 0, h = 0.001"

print("Q3: Voici l'allure de v1(t) pour les paramètres {}".format(p))

e = euler(chute_1,t0,tf,v0,h)

t = e[0]
v = e[1]

plt.plot(t,v)

plt.title("Vitesse en fonction du temps")

plt.show()
plt.close()

print("""# Hypothèse n°2 sur les frottements

Q1: L'équation différentielle est donnée par l'application du PFD. On arrive à dv/dt = - k_2 * v - g_2.
Q2: Fonction qui apparaît dans le code.
Q3: Voici l'allure de v2(t) pour les paramètres {}""".format(p))

e = euler(chute_2,t0,tf,v0,h)

t = e[0]
v = e[1]

plt.plot(t,v)

plt.title("Vitesse en fonction du temps")

plt.show()
plt.close()

print("""# Étude expérimentale et confrontation aux hypthèses des modèles

Q1: Voici les graphes des deux modèles et celui des données expérimentales.""")

t_exp = [0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11]
v_exp = [0.0001,-0.007,-0.2,-0.25,-0.24,-0.26,-0.25,-0.27,-0.25,-0.28,-0.24,-0.27]

e = euler(chute_1,t0,tf,v0,h)
t,v = e[0],e[1]
plt.plot(t,v,color='b')

e = euler(chute_2,t0,tf,v0,h)
t,v = e[0],e[1]
plt.plot(t,v,color='r')

plt.plot(t_exp,v_exp,color='black')

plt.legend(['Hyp 1','Hyp 2', 'exp'],loc='upper left')

plt.show()

print("Q2: Le modèle qui suit le mieux celui de l'hypothèse 1.")
