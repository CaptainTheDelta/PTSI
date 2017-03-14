# coding: utf-8

print("TP1 - Ex39")

# Consigne :
print("\nEcrire un programme qui retourne le nombre d'entiers premiers "+
    "compris entre deux nombres a et b rentrés par l'utilisateur.\n\n")

# Exercice :
a = int(input("Entrez une borne inférieure : "))
b = int(input("Entrez une borne supérieure : "))

Max = b
for i in range(Max + 1):
    premier.append(True)
premier[0] = False; premier[1] = False

for p in range(int(sqrt(Max))+1):
    if(premier[p]):
        for i in range(p+p, Max+1, p):
            premier[i] = False
compteur = 0

for i in range(a, b+1):
    if(premier[i]):
        compteur += 1

print("Il y a {} nombres premiers entre {} et {}".format(compteur,a,b))

# Conclusion :
print("""
Résultat :
Comme pour l'exercice précédant, on utilise plusieurs itérations pour : 
 - Définir un tableau nombre:True
 - définir les nombres premiers
 - en tirer un résultat.""")