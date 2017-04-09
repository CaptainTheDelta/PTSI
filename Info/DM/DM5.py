# Préliminaires
# Question 1

table = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
for lettre in alphabet: table.append(str(lettre))
# table = [l for l in alphabet]

# Question 2

def epure(texte):
    """Renvoie la chaîne de caracctères texte en minuscule et sans caractères
    accentés.

    Args:
        texte (str): Chaîne à épurer.

    Return:
        (str): Chaîne épurée.
    """
    texte = texte.lower()
    accents = [('à','a'),('ç','c'),('é','e'),('ê','e'),('è','e'),('ë','e'),
        ('î','i'),('ï','i'),('ô','o'),('û','u'),('ù','u'),('ÿ','y')]

    for f,r in accents:     # find,replace
        texte = texte.replace(f,r)

    return texte

# Question 3

def analyseOccurenceTexte(texte,table):
    """Renvoie la liste du nombre d'occurences dans la chaîne texte des 
    caractères de la liste table.

    Args:
        texte (str): Chaîne de caractères à analyser.
        table (list): Ensemble de caractères simples.

    Return:
        (list): Liste du nombre d'occurence dans la chaîne texte des caractères
            de la liste table.
    """
    texte = epure(texte)
    occ = [0] * len(table)
    dT = {} # pour dictionnaireTable

    for i,t in enumerate(table):
        dT[t] = i

    for t in texte:
        if(t in dT):
            occ[dT[t]] += 1

    return occ

#def analyseOccurenceTexte(texte,table):
#    texte = epure(texte)
#    return [texte.count(t) for t in table]

def analyseFreqTexte(texte,table):
    """Renvoie la liste des fréquences d'apparition dans la chaîne texte des
    caractères de la liste table.

    Args:
        texte (str): Chaîne de caractères à analyser.
        table (list): Ensemble de caractères simples.

    Return:
        (list): Liste des fréquences d'apparition dans la chaîne texte des 
            caractères de la liste table.
    """
    texte = epure(texte)
    occ = analyseOccurenceTexte(texte,table)
    l = sum(occ)
    assert l != 0

    return [o/l if l != 0 else 0 for o in occ]

# Question 4

import matplotlib.pyplot as plt
import pylab

donnees = list(range(10))
hauteur = [8,12,8,5,4,3,2,1,0,1]
largeur = 0.5

plt.bar(donnees, hauteur, largeur, color='b')

etiquettes = ['a','b','c','d','e','f','g','h','i','j']
pylab.xticks(donnees, etiquettes, rotation=40)

plt.xlim(-1,10)
plt.ylim(0,14)

plt.ylabel("Apparitions")
plt.title("Nombres d'apparitions des lettres")

plt.grid()

# plt.show()
plt.close()

# Question 5

def diagAnalyseFreqTexte(texte,table,nom_image):
    """Affiche et enregistre le graphique des fréquences d'apparitions des 
    caractères de la table dans la chaîne texte.

    Args:
        texte (str): Chaîne à analyser.
        table (str): Ensemble de caractères simples.
        nom_image (str): Nom sous lequel enregistrer l'image.
    """
    l = len(table)
    d = list(range(l))

    data = analyseFreqTexte(texte, table)

    pylab.xticks(d,table,rotation=40)

    m = max(data)

    plt.xlim(-1,l)
    plt.ylim(0,m + 0.05 * m)
    plt.grid()

    plt.title("Nombres d'apparitions des lettres")
    plt.ylabel("Apparitions")

    plt.bar(d, data, 0.05, color='b')

    if(not nom_image.endswith(".jpg")):
        nom_image += ".jpg"

    plt.savefig(str(nom_image))

    plt.show()
    plt.close()

# Question 6

import os

def lire_fichier(nom_fichier):
    """Renvoie le contenu du fichier sous forme d'une chaîne de caractères.
    
    Args:
        nom_fichier (str): Nom du fichier.

    Return:
        (str): Contenu du fichier.
    """
    if(not nom_fichier.endswith(".txt")):
        nom_fichier += ".txt"

    data = None

    if os.path.exists(nom_fichier):
        with open(nom_fichier,'r',encoding="utf8") as f:
            data = f.read()

    return data

def ecrire_fichier(texte,nom_fichier):
    """Sauve texte dans un fichier nommé nom_fichier.

    Args:
        texte (str): Texte à sauvegarder.
        nom_fichier (str): Nom du fichier.
    """
    if(not nom_fichier.endswith(".txt")):
        nom_fichier += ".txt"

    with open(nom_fichier,'w',encoding='utf8') as f:
        f.write(texte)

# Chiffrement : première méthode
# Question 1

def codeCChar(char,cle,table):
    """Renvoie char si char n'est pas dans la table, l'élément char décalé de 
    cle dans la table sinon.

    Args:
        char (char): Caractère à coder.
        cle (int): Décalage.
        table (list): Ensemble de caractères simples.

    Return:
        (char): char si char n'est pas dans la table, l'élément char décalé de 
            cle dans la table sinon.
    """
    l = len(table)

    for i,t in enumerate(table):
        if(char == t):
            return table[(i + cle) % l]

    return char

# Question 2

def codeCTexte(texteClair,cle,table):
    """Renvoie le texteClair codé avec la clef (code César).

    Args:
        texteClair (str): Phrase à coder.
        cle (int): Décalage.
        table (list): Ensemble de caractères simples.

    Return:
        (str): texteClair codé.
    """
    texte = ''

    for t in epure(texteClair):
        texte += codeCChar(t,cle,table)

    return texte

# Question 3

def codeCFichier(fichier_source,cle,table):
    """Créé un fichier contenant le texte de fichier_source codé (code César).

    Args:
        fichier_source (str): Fichier à coder.
        cle (int): Décalage.
        table (list): Liste de caractères simples.
    """
    data = lire_fichier(fichier_source)

    if(data != None):
        data = codeCTexte(str(data),cle,table)

    if(fichier_source.endswith(".txt")):
        fichier_source = fichier_source[:-4]

    fichier_source += "_Ccode.txt"

    ecrire_fichier(data,fichier_source)

# Question 4

def decodeCTexte(texteCode,cle,table):
    """Renvoie le texteCode décodé avec la clef.

    Args:
        texteCode (str): Phrase à décoder.
        cle (int): Décalage.
        table (list): Ensemble de caractères simples.

    Return:
        (str): texteCode décodé.
    """
    return codeCTexte(texteCode,-cle,table)

def decodeCFichier(fichier_source,cle,table):
    """Créé un fichier contenant le texte de fichier_source décodé.

    Args:
        fichier_source (str): Fichier à décoder.
        cle (int): Décalage.
        table (list): Liste de caractères simples.
    """
    data = lire_fichier(fichier_source)

    if(data != None):
        data = decodeCTexte(str(data),cle,table)

    if(fichier_source.endswith(".txt")):
        fichier_source = fichier_source[:-4]

    fichier_source += "_Cdecode.txt"

    ecrire_fichier(data,fichier_source)

# Chiffrement : seconde méthode
# Question 1

def codeVTexte(texteClair,cle,table):
    """Renvoie le texteClair codé avec la clef (code Vigenère).

    Args:
        texteClair (str): Phrase à coder.
        cle (list): Liste de clefs.
        table (list): Ensemble de caractères simples.

    Return:
        (str): texteClair codé.
    """
    res = ''
    c = len(cle)

    for i,char in enumerate(epure(texteClair)):
        res += codeCChar(char,cle[i % c],table)

    return res

def decodeVTexte(texteCode,cle,table):
    """Renvoie le texteCode décodé avec la clef (code Vigenère).

    Args:
        texteCode (str): Phrase à coder.
        cle (list): Liste de clefs.
        table (list): Ensemble de caractères simples.

    Return:
        (str): texteClair codé.
    """
    cle = [-c for c in cle]
    return codeVTexte(texteCode,cle,table)

# Question 2

def codeVFichier(fichier_source,cle,table):
    """Créé un fichier contenant le texte de fichier_source codé
    (code Vigenère).

    Args:
        fichier_source (str): Fichier à coder.
        cle (list): Liste de clefs.
        table (list): Ensemble de caractères simples.
    """
    data = lire_fichier(fichier_source)

    if(data != None):
        data = codeVTexte(str(data),cle,table)

    if(fichier_source.endswith(".txt")):
        fichier_source = fichier_source[:-4]

    fichier_source += "_Vcode.txt"

    ecrire_fichier(data,fichier_source)

def decodeVFichier(fichier_source,cle,table):
    """Créé un fichier contenant le texte de fichier_source décodé.

    Args:
        fichier_source (str): Fichier à décoder.
        cle (int): Liste de clefs.
        table (list): Ensemble de caractères simples.
    """
    data = lire_fichier(fichier_source)

    if(data != None):
        data = decodeVTexte(str(data),cle,table)

    if(fichier_source.endswith(".txt")):
        fichier_source = fichier_source[:-4]

    fichier_source += "_Vdecode.txt"

    ecrire_fichier(data,fichier_source)

# Cryptanalyse
# Question 1
# Question 1.a

def force_brute(texteCode,table):
    """Affiche des décodages de texteCode, tant que l'utilisateur n'est pas
    satisfait.

    Args:
        texteCode (str): Texte à décoder.
        table (list): Ensemble de caractères simples.
    """
    texte = texteCode[:35]
    input("Presser entrer pour essayer la première clef.")

    for clef in range(1,26):
        print(clef,':',decodeCTexte(texte,clef,table))

        if(input("Presser entrer pour essayer la clef suivante ou N "+
            "pour arreter").lower() == 'n'):
            return

# Question 2
# 2.a

def position(x,liste):
    """Récupère la position de x dans la table.
    
    Args:
        x (obj): Élément dont on cherche l'indice dans la liste.
        liste (list): Liste d'objets.

    Return:
        (int): Position de x, ou None si il n'appartient pas à la liste.
    """
    for i,elt in enumerate(liste):
        if(x == elt): return i

    return None

def attaque_stat1(texteCode,table):
    """Affiche des décodages de texteCode, tant que l'utilisateur n'est pas
    satisfait.

    Args:
        texteCode (str): Texte à décoder.
        table (list): Ensemble de caractères simples.
    """
    freq  = analyseFreqTexte(texteCode,table)
    freqFr =  [ ('a',0.083944),('b',0.007669),('c',0.033297),('d',0.040699),
                ('e',0.145037),('f',0.012109),('g',0.009495),('h',0.007973),
                ('i',0.081828),('j',0.006377),('k',0.000638),('l',0.058405),
                ('m',0.029355),('n',0.075570),('o',0.053669),('p',0.032087),
                ('q',0.012613),('r',0.070209),('s',0.080091),('t',0.074775),
                ('u',0.059808),('v',0.015791),('w',0.000067),('x',0.004098),
                ('y',0.003155),('z',0.001240)]
    freqFrOrd = sorted(freqFr,key=lambda freq:freq[1],reverse=True)

    texte = texteCode[:35]
    rg = position(max(freq),freq)

    input("Presser entrer pour essayer la première clef.")

    for l,f in freqFrOrd:
        clef = rg - position(l,table)

        print(clef,':',decodeCTexte(texte,clef,table))

        if(input("Presser entrer pour essayer la clef suivante ou N "+
            "pour arreter").lower() == 'n'):
            return

# 2.b

def distance(texteCode,table):
    """Renvoie la clef pour laquelle la différence entre les fréquences 
    d'apparition dans la langue française et le texte décalé de cette clef est 
    la plus faible.

    Args:
        texteCode (str): Texte à analyser.
        table (list): Ensemble de caractères simples.

    Return:
        (int): Clef correspondante.
    """
    rg,m = 0,2
    freq = analyseFreqTexte(texteCode,table)
    freqFr = [0.083944,0.007669,0.033297,0.040699,0.145037,0.012109,0.009495,0.007973,0.081828,0.006377,0.000638,0.058405,0.029355,0.07557,0.053669,0.032087,0.012613,0.070209,0.080091,0.074775,0.059808,0.015791,6.7e-05,0.004098,0.003155,0.00124]

    for i in range(26):
        s = 0
        
        for j in range(26):
            s += abs(freqFr[j] - freq[(i + j) % 26])
        
        if(s < m):
            m = s
            rg = i
        
    return rg

def attaque_stat2(texteCode,table):
    """Renvoie le texteCode décodé, par analyse statistique (un peu plus)
    poussée.

    Args:
        texteCode (str): Texte à décoder.
        table (list): Ensemble de caractères simples.

    Return:
        (str): Renvoie le texte décodé.
    """
    rg = distance(texteCode,table)

    return decodeCTexte(texteCode,rg,table)

# Question 3
# 3.a

def indice(texte,table):
    """Renvoie l'indice de coïncidence du texte.
    (cf http://fr.wikipedia.org/wiki/Indice_de_coincidence)

    Args:
        texte (str): Chaîne de caractères.
        table (list): Ensemble de caractères simples.

    Return:
        (float): Indice de coïncidence du texte.
    """
    texte = epure(texte)
    n = len([c for c in texte if c in table])
    occ = analyseOccurenceTexte(texte,table)
    ic = 0

    for na in occ:
        ic += (na * (na - 1) / (n * (n - 1)))

    return ic

# 3.b

def divTexte(texte,n):
    """Renvoie le texte divisé en n sous-chaînes.

    Args:
        texte (str): Chaîne de caractères.
        n (int): Nombre de division du texte.
    
    Return:
        (list): Liste composé de n sous-chaînes de texte.
    """
    t = []
    
    for i in range(n):
        t.append(texte[i::n])

    return t
    #return [texte[i::n] for i in range(n)]

def liste_indices(texteCode,N,table):
    """Renvoie la liste des indices de coïncidences moyens de texte divisé de 1 
    à N fois.

    Args:
        texte (str): Chaîne de caractères.
        N (int): Nombre de division maximal du texte.
        table (list): Ensemble de caractères simples.

    Return:
        (list): Liste des incidices de coïncidences moyens.
    """
    ic = []

    for n in range(1,N+1):
        ind = 0
        texte = divTexte(texteCode,n)

        for ssTxt in texte:
            ind += indice(ssTxt,table)
        
        ic += [ind / n]

    return ic

# 3.c

def cle(texteCode,N,table):
    """Renvoie la longueur probable de la clef.

    Args:
        texte (str): Chaîne de caractères.
        N (int): Nombre de division maximal du texte.
        table (list): Ensemble de caractères simples.

    Return:
        (int): Longueur probable de la clef.
    """
    ic = liste_indices(texteCode,N,table)
    l = 0
    diff = [abs(0.0778 - ic[i]) for i in range(N)]
    
    for i in range(N):
        if(ic[i] > 0.07):
            return i+1
        if(diff[i] < diff[l]):
            l = i
    
    return l+1

# 3.d

def decodage_automatique(texteCode,N,table):
    """Affiche le texte décodé.

    Args:
        texte (str): Chaîne de caractères.
        N (int): Nombre de division maximal du texte.
        table (list): Ensemble de caractères simples.
    """
    lClef = cle(texteCode,N,table)
    texte = []
    res = ''

    for i in range(lClef):
        texte += [attaque_stat2(texteCode[i::lClef],table)]

    l = len(texte[0])

    for i in range(l):
        for c in range(lClef):
            if(i < len(texte[c])):
                res+= texte[c][i]

    return res

# Présentation des résultats :

import os
os.chdir("C:\\Users\\lesec\\Desktop\\N")

texte = ''
clef = 0

# -------- Chiffre de César --------

#texte = input("1.\t(a) Entrer un texte à coder avec la méthode C : ")
#clef = int(input("\t(b) Entrer la clé : "))
#print("\t(c) Voici le texte codé :",codeCTexte(texte,clef,table))
#print('')
#
#texte = input("2.\t(a) Entrer un texte à décoder avec la méthode C : ")
#clef = int(input("\t(b) Entrer la clé : "))
#print("\t(c) Voici le texte décodé :",decodeCTexte(texte,clef,table))
#print('')
#
#
#fichier = input("3.\t(a) Entrer le nom du fichier à coder avec la méthode C : ")
#clef = int(input("\t(b) Entrer la clé : "))
#codeCFichier(fichier,clef,table)
#print('')
#
#
#fichier = input("4.\t(a) Entrer le nom du fichier à décoder avec la méthode C : #")
#clef = int(input("\t(b) Entrer la clé : "))
#decodeCFichier(fichier,clef,table)
#print('')
#
## -------- Chiffre de Vigenère --------
#import re
#
#def getClefV():
#    """Obtient de l'utilisateur une clef valide pour le chiffre de Vigenère.
#
#    Return:
#        (list): Clef valide.
#    """
#    c = input("\t(b) Entrer la clé (sous la forme '**,*,*', où * sont des #nombres): ")
#
#    while(not re.match("^\d+(,\d+)*$",c)):
#        c = input("Format incorrect !\nEntrer la clé : ")
#
#    return [int(clef) for clef in c.split(',')]
#
#
#texte = input("5.\t(a) Entrer un texte à coder avec la méthode V : ")
#clef = getClefV()
#print("\t(c) Voici le texte codé :",codeVTexte(texte,clef,table))
#print('')
#
#
#texte = input("6.\t(a) Entrer un texte à décoder avec la méthode V : ")
#clef = getClefV()
#print("\t(c) Voici le texte décodé :",decodeVTexte(texte,clef,table))
#print('')
#
#
#fichier = input("7.\t(a) Entrer le nom du fichier à coder avec la méthode V : ")
#clef = getClefV()
#codeVFichier(fichier,clef,table)
#print('')
#
#
#fichier = input("8.\t(a) Entrer le nom du fichier à décoder avec la méthode V : #")
#clef = getClefV()
#decodeVFichier(fichier,clef,table)
#print('')

# -------- Déchiffrage automatique --------

texte = input("9.\t(a) Entrer un texte codé avec la méthode C : ")
print("\n\t(b) Attaque statistique sur la lettre e :\n")
attaque_stat1(texte,table)
print("\t(c) Attaque statistique complète :",attaque_stat2(texte,table))
print('')



texte = input("10.\t(a) Entrer un texte codé avec la méthode V :")
print("\t(b) Longueur estimée de la clé :",cle(texte,50,table))
print("\t(c) Décodage automatique :",decodage_automatique(texte,50,table))