Pistes pour le DM de physique, le [DM7](https://github.com/CaptainTheDelta/PTSI/tree/master/Info/DM#pistes-dm-7)

# Pistes pour le DM de physique
*Désolé pour le retard, j'ai eu quelques difficultés imprévues...*

## Préliminaires

**Q1 :** 100% cours pour Yk+1, pour Xk+1, se rappeler la relation entre Xk et Xk+1.

**Q2 :** On peut reprendre la fonction du cours, mais faire gaffe au `n` qui devient `h` !  
Un peu d'aide en plus :
```python
import numpy as np
np.linspace(m,M,n)
# m : min, M : max, n : nombre de divisions.

# Autre fonction intéressante :
np.arange(m,M,h)
# m,M pareils, h : pas
```

## Étude de la chute libre

**Q1 :** De la physique, pas de l'info. C'est tout facile !

**Q2 :** v_libre renvoie la dérivée de la fonction y en t.  
Nota Bene :
```python
from scipy.misc import derivative

derivative(f,x) # Renvoie f'(x). Ou pas.

# Quand on envoie une fonction comme paramètre, on fait attention à ce qu'on fait :
y(t) # -> Nombre
y    # -> Fonction
```
A vous de voir si vous voulez dériver un nombre ou une fonction...
Et la dérivée de la vitesse reste égale à -9.81...

**Q3 :** On cherche une liste des valeurs prises par v(t).  
Application de la fonction Euler avec v_libre.  
Euler renvoie une liste des temps et une liste contenant les valeurs de v(t).

**Q4 :** Trivial.

**Q5 :** Physique, pas de l'info. (trivial)

**Q6 :** On a : Y = {z; v} et dY/dt = {dz/dt; dv/dt}.  
On cherche à exprimer exprimer dz/dt et dv/dt en fonction de z et v (par les équa. diff).
Donc  F = dY/dt = {expression de dz/dt; expression de dv/dt} = {v(t); -9.81} 

**Q7 :** z_libre renvoie le vecteur F. (de ce que j'ai compris.)

**Q8 :** Comme pour la question 3, on cherche une liste de valeurs de z(t). Et comme pour la question 3, il faut appliquer les fonctions qu'on vient de définir.  
Faire un euler2 pour cette question (cf remarque du prof).  
```
(le prof au tableau :)
euler2(F,...)
    -> liste t
    -> liste F  -> liste z
                -> liste v
```

**Q9 :** La joie des graphiques. Besoin d'aide ?

**Q10 :** Nouvelle façon de présenter les choses...

**Q11 :** Rien à ajouter.  
**Q12 :** Rien à ajouter.  
**Q13 :** Rien à ajouter.  

**Q14 :** Comparaison avec vos résultats, lecture graphique. Besoin d'aide ?


## Étude dynamique d'une chute avec frottements


**Q1 :** Rappel de calcul pour les mauvais : Vsphère = (4/3) * pi * (r^3)

**Q2 :** Faire un PFD avec le poids et Archimède, en déduire g_2 (l'ensemble).

**Q3 :** Refaire un PFD avec les frottements en plus. Pour f, regarder la partie hypothèse n°1.

**Q4 :** Refaire un PFD avec les frottements en plus. Pour f, regarder la partie hypothèse n°2.


## Hypothèse n°1 sur les frottements


**Q1 :** Physique, pas info.

**Q2 :** On prend v = dy/dt. On dans l'équa diff, on se débrouille pour obtenir dy/dt en fonction de y (intégration), et tadam, on a notre fonction !

**Q3 :** Exploitation des résultats.


## Hypothèse n°2 sur les frottements


**Q1 :** Physique, pas info

**Q2 :** On prend v = dy/dt. On dans l'équa diff, on se débrouille pour obtenir dy/dt en fonction de y (intégration), et tadam, on a notre fonction !

**Q3 :** Exploitation des résultats.


## Étude expérimentale et confrontation aux hypothèses des modèles


**Q1 :** Question très dure. Je ne peux rien pour vous.

**Q2 :** Idem.


## Remerciements

A un copain qui m'a fait comprendre Euler et fait bien avancé sur le DM.


# Pistes DM 7

## Partie I : Des matrices avec `numpy`

**Q1 :** shape <-> forme  
ndim <-> n lignes  
size <-> taille => nombre d'éléments.  
dtype <-> type d'élément.

**Q2 :**  
```python
A + 4               # dur à comprendre...
A \\ 2              # /!\ Faux !!! Il faut faire :
A // 2              # cf division euclidienne
A % 2               # cf reste de la DE
A * 4               # dur à comprendre...
```

**Q3 :**  
```python
np.zeros            # Matrice de 0.
np.zeros(tuple)     # tuple : dimensions de la matrice.
np.zeros(int)       # int : matrice à une ligne, dont on précise le nombre d'éléments.

np.ones             # pareil, mais avec des 1.

np.eye              # Matrice identité

np.array            # Déjà vu

np.diag(x)          # Matrice diagonale avec les coefs diagonaux égaux à ceux de la matrice ligne
np.diag(x,2)        # Plein de zéro, les coef de x sont disposés sur la deuxième diagonale à droite de la diag centrale.
np.diag(x,-2)       # Plein de zéro, les coef de x sont disposés sur la deuxième diagonale à gauche de la diag centrale.

np.random.rand(3)   # Matrice de valeurs aléatoires (entre 0 et 1) à 3 éléments.
np.random.rand((2,3)) # /!\ Faux !!! Il faut faire :
np.random.rand(2,3) # Pareil, mais on définit les dimensions de la matrice.
```

**Q4 :**  
```python
A.reshape(x,y)      # Créé une matrice à x lignes et y colonnes à partir de la matrice A.
```
A noter que si les nouvelles dimensions ne permettent pas d'exploiter toutes les données, cela engendre une erreur. (en tout cas de mon côté)

**Q5 :**
```python
A * D               # Opération entre les coef à 'la même place'.
A ** n              # Il s'agit des coefficients de la matrice qui sont mis à la puissance n.
I * A               # Comme pour A * D. => Pas comme un produit de matrices !!!
```

**Q6 :** 
```python
transpose           # /!\ Faux !!! Il faut faire :
np.transpose        # Donne... la transposée !

np.dot              # Permet la multiplication entre deux matrices
np.trace            # La trace de la matrice...

nplg.inv            # Donne l'inverse de la matrice.
nplg.solve          # Résout le système.
nplg.matrix_power   # Matrice à la puissance...
```

**Q7 :** `A[a:b, c:d]` : on prend les lignes [a;b[ et les colonnes [c;d[.

**Q8 :** `B[a:b,c:d,e:f]` ~ `B[a:b][c:d][e:f]`, et même fonctionnement que pour 2D.

**Q9 :** Si on n'utilise pas la commande `copy`, dès lors qu'on modifie une des valeurs de notre nouveau tableau, on modifie le tableau d'origine.


## Partie II : Manipulation d'images

**Q5 :** Penser à vérifier que les paramètres sont valides, et réutiliser les fonctions déjà créées.

**Q6 :**