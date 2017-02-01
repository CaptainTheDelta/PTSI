# coding: utf-8

print("TP1 - Ex22")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice22.py, un programme qui demande "+
    "un nombre entier à l'utilisateur et qui affiche le double s'il est "+
    "impair et le triple s'il est pair.\n\n")

# Exercice :
n = int(input('Entrez un nombre : '))

if(n % 2 == 1):
    print(n * 2)
else:
    print(n * 3)
# % : modulo = reste de la division euclidienne

# Conclusion :
print("\nEn fonction de la valeur de n, le code s'execute de deux manières "+
    "différentes.")