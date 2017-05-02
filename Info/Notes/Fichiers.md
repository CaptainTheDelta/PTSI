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
with open("MonFichier",'r') as fichier:
    data = fichier.readline()
```