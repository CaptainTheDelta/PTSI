from random import randint

# Exercice 1

# Question 1

def creer_matrice2(n,p,k):
    """Renvoie la matrice de n lignes et p colonnes dont tous les coefficients
    valent k.

    Args:
        n (int): Nombre de lignes.
        p (int): Nombre de colonnes.
        k (int): Valeur des coefficients.

    Return:
        (list): Matrice à n lignes et p colonnes, chacun de ses coefficient vaut
            k.
    """
    return [[k]*p for i in range(n)]

# Question 2

def createMatRdm(n,p):
    """Renvoie une matrice de n lignes et p colonnes dont chacun des coefficients
    vaut une valeur aléatoire entre 0 et 100

    Args:
        n (int): Nombre de lignes.
        p (int): Nombre de colonnes.
        k (int): Valeur des coefficients.

    Return:
        (list): Matrice à n lignes et p colonnes, chacun de ses coefficient vaut
            k.
    """
    mat = []

    for i in range(n):
        mat.append([])

        for j in range(p):
            mat[-1] += [randint(0,100)]

    return mat

mat_int_alea = lambda n,p : createMatRdm(n,p)

# Question 3

def copie_matrice(A):
    """Renvoie une copie de A.

    Args:
        A (list): Matrice à copier.

    Return:
        (list): Matrice copiée.
    """
    return [a[:] for a in A]

# Question 4

def taille(A):
    """Renvoie les dimensions de la matrice A, et vérifie si elle est valide.

    Args:
        A (list): Matrice à analyser.

    Return:
        (tuple): Dimensions de A, une erreur si A n'est pas une matrice.
    """
    assert len(A) != 0 or len(A[0]) != 0

    n = len(A)
    p = len(A[0])

    for l in A[1:]:
        if(len(l) != p):
            raise ValueError("La matrice n'est pas valide.")

    return n,p

# Question 5

def isMatNulle(A):
    """Renvoie si A est une matrice nulle ou non.

    Args:
        A (list): Matrice.

    Return:
        (bool): Nullité de la fonction.
    """
    for sA in A:
        for coef in sA:
            if(coef != 0): return False

    return True

def isEqual(A,B):
    """Renvoie si A et B sont égales ou non.

    Args:
        A (list): Matrice.
        B (list): Matrice.

    Return:
        (bool): Egalité de A et de B.
    """
    return A == B or (isMatNulle(A) and isMatNulle(B))

# Question 6:

def isCarre(A):
    """Renvoie si A est une matrice carrée ou non.

    Args:
        A (list): Matrice.

    Return:
        (bool): True si la matrice est carrée, False sinon.
    """
    n,p = taille(A)

    return n == p

def isDiag(A):
    """Renvoie si A est une matrice diagonale ou non.

    Args:
        A (list): Matrice.

    Return:
        (bool): Diagonalité de A.
    """
    n,p = taille(A)

    if(n != p): return False

    for i in range(n):
        for j in range(p):
            if(i == j):
                continue

            elif(A[i][j] != 0):
                return False

    return True

def isTriangSup(A):
    """Renvoie si A est une matrice triangulaire supérieure ou non.

    Args:
        A (list): Matrice.

    Return:
        (bool): Triangularité supérieure de A.
    """
    n,p = taille(A)

    if(n != p): return False

    for i in range(n):
        for j in range(i):
            if(i == j):
                continue

            elif(A[i][j] != 0):
                return False

    return True

# Question 7

def Add(A,B):
    """Renvoie la somme de A et de B.

    Args:
        A (list): Matrice.
        B (list): Matrice.

    Return:
        (list): Somme de A et de B.
    """
    if(isMatNulle(A)): return B
    if(isMatNulle(B)): return A

    n,p = taille(A)

    assert (n,p) == taille(B)

    mat = creer_matrice2(n,p,None)

    for i in range(n):
        for j in range(p):
            mat[i][j] = A[i][j] + B[i][j]

    return mat

# Question 9

def lambdaProd(A,x):
    """Renvoie le produit de A par x.

    Args:
        A (list): Matrice.
        x (int): Facteur multiplicateur.

    Return:
        (list): Produit de A par x.
    """
    #return [[x*c for c in ligne] for ligne in A]
    n,p = taille(A)
    A1 = copie_matrice(A)

    for i in range(n):
        for j in range(p):
            A1[i][j] *= x

    return A1

# Question 8
# Q8.a

def transpose(A):
    """Renvoie la transposée de A.

    Args:
        A (list): Matrice.

    Return:
        (list): Transposée de A.
    """
    n,p = taille(A)

    mat = creer_matrice2(p,n,None)

    for i in range(n):
        for j in range(p):
            mat[j][i] = A[i][j]

    return mat

# Q8.b

def isSym(A):
    """Renvoie si A est une matrice symétrique ou non.

    Args:
        A (list): Matrice.

    Return:
        (bool): Symétrie de A.
    """
    return isEqual(A, transpose(A))

def isAntiSym(A):
    """Renvoie si A est une matrice antisymétrique ou non.

    Args:
        A (list): Matrice.

    Return:
        (bool): Antisymétrie de A.
    """
    return isEqual(A, lambdaProd(transpose(A), -1))

def isTriangInf(A):
    """Renvoie si A est une matrice triangulaire inférieure ou non.

    Args:
        A (list): Matrice.

    Return:
        (bool): Triangularité inférieure de A.
    """
    return isTriangSup(transpose(A))

# Question 10
# Q.a

def prod(A,B):
    """Renvoie le produit de A et de B.

    Args:
        A (list): Matrice.
        B (list): Matrice.

    Return:
        (list): A*B.
    """
    n1,p = taille(A)
    n,p1 = taille(B)

    assert n == p

    mat = creer_matrice2(n,p,None)

    for i in range(n):
        for j in range(p):
            coef = 0

            for x in range(p):
                coef += A[i][x] * B[x][j]
            
            mat[i][j] = coef

    return mat

# Q.b

def isId(A):
    """Renvoie si A est l'identité ou non.

    Args:
        A (list): Matrice.

    Return:
        (bool): True si A est la matrice identité, Fasle sinon.
    """
    n,p = taille(A)

    if(n != p): return False

    for i in range(n):
        for j in range(p):
            if(not ((i == j and A[i][j] == 1) or (A[i][j] == 0))):
                return False

    return True


def power(A,n):
    """Renvoie la puissance n-ième de A.

    Args:
        A (list): Matrice.
        n (int): Exposant.
    
    Return:
        (list): A ** n.
    """
    assert isCarre(A)

    mat = copie_matrice(A)

    for i in range(n-1):
        mat = prod(mat, A)

    return mat

# Question 11
# Q11.a

def J(n):
    """Renvoie la matrice Jn.

    Args:
        n (int): Rang de la matrice désirée.

    Return:
        (list): Matrice Jn.
    """
    mat = creer_matrice2(n,n,0)

    for i in range(n):
        for j in range(n):
            if(i+j+1 == n):
                mat[i][j] = 1

    return mat

# Q11.b

def centroMat(A):
    """Renvoie la matrice Â.

    Args:
        A (list): Matrice.

    Return:
        (list): Â.
    """
    n,p = taille(A)

    mat = creer_matrice2(n,p,None)

    for i in range(n):
        for j in range(p):
            mat[i][j] = A[n-i-1][p-j-1]

    return mat

# 11.c

print("Question 11.c")
print("On trouve : A = JÂJ.")

# 11.d

print("Question 11.d")

print(isEqual(centroMat(prod(A,B)), prod(centroMat(A),centroMat(B))))

print("L'égalité est vérifiée.")


def printMat(A):
    n,p = taille(A)

    strA = [[str(coef) for coef in line] for line in A]
    lenCoef = [[len(coef) for coef in line] for line in strA]
    maxLen = max([max(line) for line in lenCoef])

    for i in range(n):
        for j in range(p):
            l = maxLen - lenCoef[i][j]
            ap = l // 2
            av = l - ap

            strA[i][j] = ' ' * av + strA[i][j] + ' ' * ap

    if(n == 1):
        print('( ' + ' '.join(strA[0]) + ' )')
        return

    mat = [' '.join(a) for a in strA]

    mat[0] = '/ ' + mat[0] + ' \\'

    for i in range(1,n-1):
        mat[i] = '| ' + mat[i] + ' |'

    mat[-1] = '\\ ' + mat[-1] + ' /'

    for m in mat:
        print(m)



# Exercice 2

import matplotlib.pyplot as plt
import numpy as np
from math import pi

x = np.linspace(-5,5,25)

plt.plot(x,np.cosh(x),color='b',marker='+')
plt.plot(x,np.sinh(x),color='r',marker='x')
plt.plot(x,np.tanh(x),color='g',marker='o')

plt.axis([-5,5,-20,25])

plt.grid()

plt.axhline(color='black')
plt.axvline(color='black')

plt.legend(['cosh','sinh','tanh'],loc='upper right')

from scipy.misc import derivative

a = -3

for f in [np.cosh, np.sinh, np.tanh]:
    fprimea = derivative(f,a)
    fa = f(a)
    y = lambda x: fprimea * (x - a) + fa
    plt.plot(x,y(x),color='black',linestyle='--')

plt.savefig('Lesecq_damien_DM6_info_graphe1.pdf',format='pdf')


# Exercice 3

# Question 1

def crible(n):
    """Implémentation du crible d'Erathostène.

    Args:
        n (int): Limite supérieure.

    Return:
        (list of int): Nombres premiers jusqu'à n.
    """
    if(n < 2):
        return []

    premiers = []
    for i in range(n+1):
        premiers.append(True)
    
    premiers[0],premiers[1] = False,False
    for p in range(int(n ** (1/2)) + 1):
        if(premiers[p]):
            for i in range(2 * p,n+1,p):
                premiers[i] = False
    return [i for i,p in enumerate(premiers) if p]

def pi(x):
    """Renvoie le nombre de premiers inférieurs à x.

    Args:
        x (int): Limite supérieure des premiers.

    Return:
        (int): Nombre de premiers inférieurs à x.
    """
    return len(crible(x))

# Question 2

from scipy.integrate import quad

def li(x):
    """Renvoie l'approximation du nombre de premiers inférieurs à x.

    Args:
        x (int): Limite supérieure des premiers.

    Return:
        (int): Approximation du nombre de premiers inférieurs à x.
    """
    f = lambda x: 1 / np.log(x)
    return quad(f,2,x)[0]

# Question 3

f = lambda x: x / np.log(x)

nbrPoints = 20

x = np.linspace(2,10**4,nbrPoints)
era = crible(10**4)
piL = []
n = 0
i = 0

liL = [li(e) for e in x]
fL = [f(e) for e in x]

for p in era:
    if(p > x[i]):
        i += 1
        piL.append(n)
        if(i >= nbrPoints):
            break
    n += 1
piL.append(n)

plt.plot(x,piL,color='b',marker='+')
plt.plot(x,liL,color='r',marker='x')
plt.plot(x,fL,color='g',marker='o')


plt.grid()

plt.legend(['pi','li','f'],loc='upper left')

plt.savefig('Lesecq_damien_DM6_info_graphe2.pdf',format='pdf')