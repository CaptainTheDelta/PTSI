# coding: utf-8

print("TP1 - Ex32")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice32.py, un programme qui calcule "+
    "la somme des multiples de 3 ou de 5 strictement inférieurs à 1000.\n\n")

# Exercice :
somme = 0
i = 0

while i < 1000:
    if(i % 5 == 0 or i % 3 == 0):
        somme += i
    i += 1

print("somme :", somme)

# Conclusion :
print("\nRésultat :\nCette somme est obtenue en vérifiant que l'incrément (i)"+
    "est un multiple de 3 ou de 5.")