# Pistes pour le DM7

## Préliminaires

**Q1 :** 100% cours pour Yk+1, pour Xk+1, se rappeler la relation entre Xk et Xk+1.

**Q2 :** On peut reprendre la fonction du cours, mais faire gaffe au `n` qui devient `h` !  
Un peu d'aide en plus :
```python
import numpy as np
np.linspace(m,M,n)
# m : min, M : max, n : nombre de divisions.

# Autre fonction interressante :
np.arange(m,M,h)
# m,M pareils, h : pas
```

## Étude de la chute libre

**Q1 :** De la physique, pas de l'info. C'est tout facile !

**Q2 :** v_truc renvoie la dérivée de la fonction y en t.  
Nota Bene :
```python
from scipy.misc import derivative

derivative(f,x) # Renvoie f'(x)

# Quand on envoie une fonction comme paramètre, on fait attention à ce qu'on fait :
y(t) # -> Nombre
y    # -> Fonction
```
A vous de voir si vous voulez dériver un nombre ou une fonction...

**Q3 :** Pas encore fait.