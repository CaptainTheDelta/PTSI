# Pistes pour le DM7
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
Donc  dY/dt = {expression de dz/dt; expression de dv/dt} = {v(t); -9.81} 

**Q7 :** Faire un euler2 pour cette question (cf remarque du prof).  
```
(le prof au tableau :)
euler2(F,...)
    -> liste t
    -> liste F  -> liste z
                -> liste v
```

**Q8 :** Comme pour la question 3, on cherche une liste de valeurs de z(t). Et comme pour la question 3, il faut appliquer les fonctions qu'on vient de définir.

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

