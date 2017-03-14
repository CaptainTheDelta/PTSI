# coding: utf-8

print("TP1 - Ex")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice24.py, un programme qui demande un nombre à l'utilisateur et qui renvoie sa valeur absolue.\n\n")

# Exercice :
n = int(input('Entrez un nombre : '))
print('Valeur absolue : ',end='')
if(n < 0):
    print(-n)
else:
    print(n)

# Conclusion :
print("\nPour obtenir la valeur absolue d'un nombre, on ne s'intéresse qu'à "+
    "son signe. Il suffit donc d'un if et d'un else pour la déterminer.")