# coding: utf-8

print("TP1 - Ex23")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice23.py, un programme qui demande "+
    "un nombre entier à l'utilisateur et qui affiche le double s'il est "+
    "impair, le triple s'il est pair mais pas divisible par 4 et sa moitié "+
    "sinon.\n\n")

# Exercice :
n = int(input('Entrez un nombre : '))
if(n%2 == 1):
    print(n*2)
elif(n%4 != 0):
    print(n*3)
else:
    print(n/2)

# Conclusion :
print("\nDe même, le code affiche des valeurs différentes en fonction de la "+
    "valeur de n. Comme il y a trois cas d'utilisation, on utilise if, elif "+
    "et else.")