# Pistes pour le DM5

### Exercice 1

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
`isDiag` : la matrice est carrée, et "tous les coefficients non diagonnaux sont nuls".  
`isTriangSup` : la matrice est carrée, et tous les coefs en dessous de la diagonnales sont nuls.  
Indices :   - les coefficients diagonaux ont pour 'indices' i = j.  
            - les coefficients sous la diagonnale vérifient :
    prendre une ligne (resp. une colonne) et regarder où se trouvent les coefs 'interressants' **par rapport** à cette ligne (resp. colonne).

**Q7 :** Vérifier que les matrices sont sommables. Ajouter coefs à coefs.

**Q8 : a)** Création de la matrice transposée via `cree_matrice`. Remplissage en inversant les indices.
**b)** rappel du cours : matrices symétriques : transposée(A) = a
matrices antisymtriques : transposée(A) = -A
Pour la matrice triangulaire inférieure, étudier transposée(A).

**Q9 :** Besoin d'aide ?

**Q10 : a)** Vérifier que le produit est possible.
Pour le calcul, embriquer deux for me paraît raisonnable (pas encore fait de mon côté, 14/03).  
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

**Q11 : a)** Etudier la somme des indices des coeffs non nuls.  
**b)** 