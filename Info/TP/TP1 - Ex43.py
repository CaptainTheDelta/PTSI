# coding: utf-8

print("TP1 - Ex43")

# Consigne :
print("\nDéterminer les nombres premiers p <= 100 tels qu'il existe deux "+
    "entiers a et b tels que a^2 + b^2 = p.\n\n")

# Exercice :
Max = 100
premier = []
for i in range(Max+1):
    premier.append(True)
premier[0] = False; premier[1] = False

for p in range(int(sqrt(Max))+1):
    if(premier[p]):
        for i in range(p+p, Max+1, p):
            premier[i] = False

for a in range(10):
    for b in range(a,10):
        somme = a**2 + b**2
        if(somme < 100 and premier[somme]):
            print("{}**2 + {}**2 = {}".format(a, b, somme))

# Conclusion :
print("\nRésultat :\nOn peut imbriquer les for entre eux pour faire des "+
    "calculs sur plusieurs variables changeantes.")