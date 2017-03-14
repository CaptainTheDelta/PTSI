# coding: utf-8

print("TP1 - Ex19")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice19.py un programme qui demande à "+
    "l'utilisateur son nom et son prénom et qui retourne ses initiales.\n\n")

# Exercice :
nom = input("Quel est votre nom ? ")
prenom = input("Quel est votre prénom ? ")

print(nom[0], prenom[0])
# Une chaîne de caractères est considérée comme une sorte de tableau.
# Par exemple "Hello World" ~ ['H','e','l','l','o',' ','W','o','r','l','d',]
# avec pour index :             0   1   2   3   4   5   6   7   8   9   10
# Ainsi, pour obtenir le premier caractère, on utilise ma_variable[0].
# Remarque : On ne peut pas modifier un string en faisant : ma_variable[3] = "e"

# Conclusion :
print("\nLes variables string sont des tableaux, pour obtenir les initiales, "+
    "on prend donc la première valeur de chaque tableau.")