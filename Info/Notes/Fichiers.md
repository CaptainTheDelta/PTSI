# Enregistrer des fichiers

## Méthode générale

### Ouverture

```python
fichier = open("MonFichier",'r')

# Mon code ici

fichier.close()

# Ou bien

with open("MonFichier",'r') as fichier:
    # Mon code ici.
```

Avec `'r'` pour la lecture, `'w'` pour l'écriture, et `'a'` pour écrire à la fin.  
Si le fichier n'existe pas, il est créé lorsqu'on utilise `'w'` ou `'a'`.  
Dans certains cas particuliers, on peut ajouter le `'b'` du binaire.

### Lecture

Pour obtenir l'ensemble du fichier sous forme de `str`.
```python
with open("MonFichier",'r') as fichier:
    data = fichier.read()
```
*Naturellement, on déclare data avant...*

Pour obtenir l'ensemble des lignes du fichier dans un tableau (chaque ligne du tableau : une ligne du fichier)
```python
with open("MonFichier",'r') as fichier:
    data = fichier.readlines()
```

Pour obtenir une ligne du fichier sous forme de `str`.
```python
with open("MonFichier",'r') as fichier:
    data = fichier.readline()
```

### Ecriture

```python
with open("MonFichier",'w') as fichier:
    fichier.write(data)
```

## json

Le module json est une manière assez propre de stocker des infos. Il est de plus en plus utilisé, remplaçant progressivement le xml.

```python
import json

with open("MonFichier",'r') as fichier:
    data = json.load(fichier)

with open("MonFichier",'w') as fichier:
    json.dump(data)
```

Ou bien avec des `s`:

```python
import json

with open("MonFichier",'r') as fichier:
    data = json.loads(fichier)

with open("MonFichier",'w') as fichier:
    json.dumps(data)
```

Avec le `s`, on enregistre/récupère une variable, sans le `s`, on enregistre/récupère sa représentation sous forme de string.