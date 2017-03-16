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
Aide plus poussée toooout en [bas](https://github.com/CaptainTheDelta/PTSI/tree/master/Info/DM#aide)...

**Q7 :** Vérifier que les matrices sont sommables. Ajouter coefs à coefs.

**Q8 : a)** Création de la matrice transposée via `cree_matrice`. Remplissage en inversant les indices.  
**b)** rappel du cours : - matrices symétriques : transposée(A) = a  
- matrices antisymétriques : transposée(A) = -A  
- Pour la matrice triangulaire inférieure, étudier la transposée(A).

**Q9 :** Besoin d'aide ?

**Q10 : a)** Vérifier que le produit est possible.  
Pour le calcul, imbriquer deux for me paraît raisonnable (pas encore fait de mon côté, 14/03/17).  
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
Après test, pas nécessairement une bonne idée.

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

Pour tout l'exercice, on a besoin de `matplotlib.pyplot` et de `numpy`
Rappel sur les arguments : [Options (TP4)](http://jstiker.free.fr/TP4.html#des-options)

**Q1** Les fonctions `cosh`, `sinh` et `tanh` sont dans le module numpy.

**Q2** Besoin d'aide ?

**Q3** Rappel sur les légendes : [ex2 TP4](https://github.com/CaptainTheDelta/PTSI/blob/master/Info/TP/TP4/TP4%20-%20Ex02.py)

**Q4** Pour les axes, [ex1 TP4](https://github.com/CaptainTheDelta/PTSI/blob/master/Info/TP/TP4/TP4%20-%20Ex01.py), en sachant que la fonction `axhline` n'a que des paramètres optionnels (et si vous chipotez, sachez que la couleur `black` existe dans `matplotlib.pyplot`. De plus il existe la fonction `plt.axvline`.

**Q5** Pour les tangentes, ai pas trouvé s'il existe une méthode sous `matplotlib.pyplot` ou `numpy` pour le faire à notre place. A creuser... (15/03/17)

Sauvegarder en format pdf :
> Il est toujours conseillé de mettre une extension aux noms de fichier ; si vous y tenez plt.savefig('toto',format='pdf') sauvegardera l’image sous le nom “toto” (sans extension !) au format “pdf”.  
La syntaxe est donc :
```python
plt.savefig('toto.pdf',format='pdf')
```
Remarque : Si jamais vous vouliez sauvegarder **et** afficher votre graphique, eh bien sauvegardez le en premier.

## Exercice 3

**Q1** `crible` pour crible d'Eratosthène, naturellement... Pour ceux qui ne l'ont pas encore fait / compris, voici un [site](http://www.math93.com/index.php/histoire-des-maths/notions-et-theoremes/186-crible-d-eratosthene) qui l'explique bien.  
"`pi(x)` est le nombre d'entiers premiers inférieurs ou égaux à x."

**Q2** Des infos sur quad [ici](http://www.science-emergence.com/Articles/Calculer-une-int%C3%A9grale-simple-avec-python/) :
```python
quad(fonction,borne_inf,borne_sup) # renvoie (valeur,erreur)
```
Attention, `numpy` est fourbe : `log` <=> ln, et `log10` <=> log :expressionless:

**Q3** Besoin d'aide ?

Pour les questions 2 et 3, faire de 2 à x, ou de 2 a 10\**4.

---


## Aide

Pour le parcourrs des matrices :  
Pour rappel, il y a deux types de `for` :
```python
for i in range(n):
for elt in liste:
```
Pour choisir, demandez vous ce que vous voulez obtenir : une position dans la liste, ou bien une valeur.  
Ce choix effectué, demandez vous comment accéder au sous-éléments de votre liste matrice.

Il n'existe aucune meilleure solution, mais juste, sachez que :
```python
liste = [['a','b','c'],['d'],['e','f','g']]

# pour tout afficher, on peut faire :
for ssliste in liste:
    for elt in ssliste:
        print(elt)

# ou bien :
for i in range(len(liste)):
    for j in range(len(liste[i])):
        print(liste[i][j])
```




Je vous fais don d'une fonction afin d'observer vos matrices d'une manière plus parlante :
```python
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
```
*PS: ça me paraît evident, mais cette fonction, vous l'enlevez avant de rendre le DM* :smile:
