# Les deux méga-pièges du TP !!! :

### Lorsque le csv est "français" :
C'est à dire lorsque les séparateurs sont des ';' et non des ',':

```python
csv.reader(fichier, delimiter=';')
```


### Lors de l'écriture :
C'est génial, mais lorsqu'on veut écrire dans un fichier, c'est moins cool quand les lignes se sautent toutes seules...

```python
with open('test.csv', 'w', newline='') as fichier:
```