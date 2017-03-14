# Pistes pour le DM6

## Exercice 1

**Q1 :** Une matrice est une liste de listes.  
`n` : nombre de lignes.  
`p` : nombre de colonnes.  
`k` : valeur des coefficients.  

**Q2 :** Pareil, mais avec k aléatoire.  
Rappel :
```python
from random import randint
randint(a,b) # renvoie un entier dans [a;b]
```

**Q3 :** Copie d'une grosse liste, c'est pareil que pour une petite.

**Q4 :** Objectif : renvoyer n et p, ou bien déterminer s'il y a un problème dans la matrice.

**Q5 :** Tester chaque élément de liste.  
Indice : vraiment, vraiment chercher au plus simple.

**Q6 :** `isCarre` : vérifier que n et p sont égaux.  
`isDiag` : la matrice est carrée, et "tous les coefficients non diagonaux sont nuls".  
`isTriangSup` : la matrice est carrée, et tous les coefs en dessous de la diagonales sont nuls.  
Indices :   - les coefficients diagonaux ont pour 'indices' i = j.  
            - les coefficients sous la diagonale vérifient :
    prendre une ligne (resp. une colonne) et regarder où se trouvent les coefs 'intéressants' **par rapport** à cette ligne (resp. colonne).

**Q7 :** Vérifier que les matrices sont sommables. Ajouter coefs à coefs.

**Q8 : a)** Création de la matrice transposée via `cree_matrice`. Remplissage en inversant les indices.  
**b)** rappel du cours : matrices symétriques : transposée(A) = a  
matrices antisymétriques : transposée(A) = -A  
Pour la matrice triangulaire inférieure, étudier transposée(A).

**Q9 :** Besoin d'aide ?

**Q10 : a)** Vérifier que le produit est possible.  
Pour le calcul, imbriquer deux for me paraît raisonnable (pas encore fait de mon côté, 14/03).  
**b)** Tenter une récurrence ?  
Rappel :  
```python
def pow(x,n):
    """Renvoie la n-ième puissance de x.

    Args:
        x (int): Indice.
        n (int): Exposant.

    Return:
        (int): N-ième puissance de x.
    """
    if(x == 0):
        return 1

    return pow(x, n-1)
```

**Q11 : a)** Etudier la somme des indices des coefs non nuls.  
**b)** `centroMat` est plus difficile à appréhender :
```
    / 11 21 31 41 \        / 44 34 24 14 \
A = | 12 22 32 42 | et Â = | 43 33 23 13 |
    | 13 23 33 43 |        | 42 32 22 12 |
    \ 14 24 34 44 /        \ 41 31 21 11 /
```
(pas sûr, à vérifier de votre côté)  
On a donc (attention, absence de math dans les mots suivants :) une sorte de double inversion de A.  
**c)** De la bidouille et des tests à faire.  
Indice : essayer les multiplications à droite, à gauche...  
**d)** Application des fonctions.

## Exercice 2

**Q **
