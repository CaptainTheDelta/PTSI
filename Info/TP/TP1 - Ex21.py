# coding: utf-8

print("TP1 - Ex21")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice21.py, un programme qui demande "+
    "un nombre entier à l'utilisateur et qui affiche si oui ou non il "+
    "appartient à l'intervalle entier allant de 0 à 10.\n\n")

# Exercice :
n = int(input('Entrez un nombre : '))
if(0 <= n <= 10): # <=> 0 <= n and n <= 10
    print(n, 'appartient à [0;10].')
else:
    print(n, "n'appartient pas à [0;10].")

# Conclusion :
print("\nif et else sont pratiques dans le cas où il n'y a que deux issues "+
    "possibles.")