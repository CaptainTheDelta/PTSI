# coding: utf-8

print("TP1 - Ex17")

# Consigne :
print("\nEcrire dans un fichier TP1-exercice17.py un programme qui demande à "+
    "l'utilisateur son nom, son prénom et son année de naissance et qui "+
    "retourne le résultat suivant sous la forme :\n\n"+
    "Nom : Leponge\n"+
    "Prénom : Bob\n"+
    "Année de naissance : 1900\n\n")

# Exercice :
nom = input("Quel est votre nom ? ")
prenon = input("Quel est votre prénom ? ")
annee = input("Quelle est votre année de naissance ? ")
# La commande input demande une donnée à l'utilisateur. Elle renvoie toujours
# une chaîne de caractères. Elle peut avoir une chaîne de caractères en
# en paramètre, qui sera affichée avant la saisie de l'utilisateur.

print("Nom : {}\nPrénom : {}\nAnnée de naissance : {}".format(nom,prenom,annee))
# La fonction format permet de "formater" des chaînes de caractères, alias
# string. Elle attend autant de paramètres que le nombre de {} placés dans le
# string. 
# Une autre façon de l'utiliser est de mettre des noms (ou des nombres) 
# entre les crochets. Un équivalent de l'exercice aurait été :
# "Nom : {nom}\nPrénom : {pr}\nAnnée de naissance : {AN}".format(nom=nom,pr=prenom,AN=annee)
# A noter que l'ordre des paramètres dans la fonction n'a plus d'importance.

# Conclusion :
print("\ninput() permet la saisie de string à l'utilisateur.")
