# coding: utf-8

print("TP1 - Ex26")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice26.py, un programme qui demande "+
    "une année à l'utilisateur et qui indique si elle est bissextile ou non. "+
    "Une année est bissextile par définition si sa valeur vérifie l'une des "+
    "conditions :\nêtre multiple de 4 mais pas de 100 ;\n"+
    "être multiple de 400.\n\n")

# Exercice :
an = int(input("Entrez une année : "))

if(an % 4 == 0):
    if(an % 100 != 0):
        print("L'année {} est bissextile.".format(an))
    elif(an % 400 == 0):
        print("L'année {} est bissextile.".format(an))
else:
    print("L'année {} n'est bissextile.".format(an))

# Conclusion :
print("\nUne solution est d'imbriquer les if entre eux, mais dans ce cas, on "+
    "ne respecte pas le \"Don't Repeat Yourself\".")