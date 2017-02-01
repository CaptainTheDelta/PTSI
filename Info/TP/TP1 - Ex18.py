# coding: utf-8

print("TP1 - Ex18")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice18.py un programme qui demande à "+
    "l'utilisateur le rayon d'une sphère et qui retourne le résultat suivant "+
    "sous la forme :\n\n"+
    "Entrez le rayon en cm : 5\n"+
    "Une sphere de rayon 5.0 cm a pour surface : 314.159265359 cm2\n"+
    "Une boule de rayon 5.0 cm a pour volume : 523.5987755982989 cm3\n\n")

# Exercice :
print("Entrez le rayon de la sphère en cm")
r = correctInput("r : ", int, end='')
print("Une sphere de rayon {r} cm a pour surface : {s} cm2\nUne boule de rayon {r} cm a pour volume : {v} cm3".format(
    r=r, s=4*pi*(r**2), v=(4/3)*pi*(r**3)))

# Conclusion :
print("\nCes valeurs, une fois traduites (ici en nombre entier), peuvent "+
    "servir comme les autres variables.")