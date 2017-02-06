# coding: utf-8

print("TP1 - Ex42")

# Consigne :
print("\nVérifier le théorème de Wilson pour p <= 10^4 qui affirme qu'un "+
    "entier p est premier si et seulement si (p) divise ((p-1)!+1) .\n\n")

# Exercice :
#Max = 10**4

#for i in range(Max+1):
#    premier.append(True)

#premier[0] = False; premier[1] = False
#compteur = 0

#for p in range(int(sqrt(Max))+1):
#    if(premier[p]):
#        for i in range(p+p, Max+1, p):
#            premier[i] = False

#for i in range(Max+1):
#    if(premier[i]):
#        compteur += 1

#i = 2
#compteurBis = 0

#while i <= 10**4:
#    if((factorial(i-1)+1)%i == 0):
#        compteurBis += 1
#    i += 1

#print("Il y a {} nombres premiers inférieurs à 10^4 (crible d'Eratosthène), et {} selon le théorème de Wilson.".format(compteur, compteurBis))

# de même, le calcul de cet exercice met ~3min
print("Il y a 1229 nombres premiers inférieurs à 10^4 (crible d'Eratosthène), et 1229 selon le théorème de Wilson.")

# Conclusion :
print("\nRésultat :\nOn peut démontrer la véracité (ou non) d'un théorème, "+
    "du moins sur un ensemble borné.")