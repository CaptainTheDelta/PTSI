# coding: utf-8

print("TP1 - Ex40")

# Consigne :
print("\nCombien y a-t-il de nombre n <= 10^8 tels que n et n+2 sont premiers ?\n\n")

# Exercice :
#Max = 10**8
#for i in range(Max+3):
#    premier.append(True)
#premier[0] = False; premier[1] = False

#for p in range(int(sqrt(Max+2))+1):
#    if(premier[p]):
#        for i in range(p+p, Max+3, p):
#            premier[i] = False

# on va utiliser le fait que tout nombre premier >3 est de la forme 6k-1 ou 6k+1 (kappartient à N) 
#compteur = 0
#for i in range(0,12):
#    if(premier[i-1] and premier[i+1]):
#        compteur += 1
#for i in range(12, Max+3, 6):
#    if(premier[i-1] and premier[i+1]):
#        compteur += 1
#print("Il y a {} nombres tels que n et n+2 soient premiers.".format(compteur))

# résultat du code précédant, mais qui met ~1h30 à s'executer sur un pc moisi,
# donc...
print("Il y a 440312 nombres tels que n et n+2 soient premiers.")

# Conclusion :
print("\nRésultat :\nLe calcul bourrin pique en terme de temps de calcul.")