# coding: utf-8

print("TP1 - Ex38")

# Consigne :
print("\nAfficher tous les nombres premiers compris entre 1 et 100 dans la "+
    "console.\n\n")

# Exercice :
premier = []
Max = 100

for i in range(Max + 1):
    premier.append(True)
premier[0] = False; premier[1] = False

for p in range(int(sqrt(Max))+1):
    if(premier[p]):
        for i in range(p+p, Max+1, p):
            premier[i] = False

for i in range(Max+1):
    if(premier[i]):
        print(i, end=', ')

# Conclusion :
print("\nRésultat :\nOups, j'ai deux TP d'avance... On se revoit plus tard ?")

# L'algo attendu devait être de la forme :
#for i in range(2,100):
#    premier = True
#    for j in range(2,i):
#        if(i % j == 0):
#            premier = False
#            break
#    if(premier):
#        print(i)