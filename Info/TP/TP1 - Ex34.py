# coding: utf-8

print("TP1 - Ex34")

# Consigne :
print("\nDans la console écrire un programme qui affiche toutes les "+
    "consonnes de la chaîne \"Vive les TP Python en PTSI-B\" et qui affiche "+
    "un underscore à la place des voyelles.\n\n")

# Exercice :
phrase = "Vive les TP Python en PTSI-B"

# enumerate(liste) renvoie le couple (i, liste[i]) à chaque itération.
for i,c in enumerate(phrase):
    if(c in "aAeEiIoOuUyY"):
        # on regarde si le caractère c se trouve dans une chaîne contenant
        # toutes les voyelles.

        phrase = phrase[:i] + '_' + phrase[i+1:]
        # On remplace la lettre par un '_' via du slicing.

print(phrase)

# Conclusion :
print("\nRésultat :\nIl faut être prudent avec les for : \n"+
    "- for var a in liste:\n    a += 3\nLes valeurs de liste ne sont pas "+
    "modifiées")