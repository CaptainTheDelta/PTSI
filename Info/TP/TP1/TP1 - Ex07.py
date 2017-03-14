# coding: utf-8

print("TP1 - Ex7")

# Consigne :
print("\nDans la console créez une variable mon_annee et affectez lui votre "+
    "année de naissance. Demandez à Python son identifiant et son type à "+
    "l'aide des commandes id() et type(). Taper ensuite les différentes "+
    "commandes suivantes :\n\n"+
    "mon_annee + 1 ; 3*mon_annee ; mon_annee + mon_annee ;\n\n")

# Exercice :
mon_annee = 1999 # Eh oui je suis de 99 messieurs dames !
print("id :",id(mon_annee))
print("type :",type(mon_annee))

print("\nmon_annee + 1 : ", mon_annee + 1)
print("3*mon_annee : ", (3*mon_annee)) 
print("mon_annee + mon_annee : ",mon_annee + mon_annee)

# Conclusion :
print("\nPython nous permet d'afficher des calculs sur des variables.")