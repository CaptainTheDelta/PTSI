# coding: utf-8

print("TP1 - Ex")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice25.py, un programme qui demande "+
    "les trois coefficients réels d'un trinôme \(ax^2+bx+c\) à l'utilisateur "+
    "et qui retourne une phrase indiquant le nombre de racines réelles "+
    "distinctes de ce trinôme, après avoir vérifié qu'il s'agissait bien d'un "+
    "polynôme du second deg\n\n")

# Exercice :
print("Soit f(x) = ax^2 + bx + c.")

a = input("a :")
b = input("a :")
c = input("a :")
delta = b**2 -4*a*c

if(delta > 0):
    print("Le trinôme admet deux racines, X1 = {}, X2 = {} .".format(
        (-b - delta ** (1 / 2))/(2 * a),(-b + delta ** (1 / 2)) / (2 * a)))
elif(delta == 0):
    print("Le trinôme admet une racine, X = {} .".format((-b/(2*a)))
else:
    print("Le trinôme n'admet pas de racine.")

# Conclusion :
print("A l'aide des valeurs des coefficients du trinôme, on peut déterminer "+
    "les racines (si elles existent) du trinôme.\n")