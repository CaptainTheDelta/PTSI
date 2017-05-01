import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from math import floor
from random import randint

entree, sortie = "images_entrees/", "images_sorties/"
le = "Lenna.png"
ba = "banana.png"
si = "mystere.png"
my = "myst.png"

# ============================= Fonctions de base ==============================


def image_to_tab(nom_image):
    """Renvoie l'image sous forme de tableau de pixels.

    Args:
        nom_image (str): Nom de l'image.

    Return:
        (array): Tableau de pixel représentant l'image.
    """
    global entree
    
    image = Image.open(entree + nom_image)
    
    return np.array(image)


def tab_to_image(tableau,nom_image_sortie,format):
    """Enregiste le tableau de pixel sous le nom et le format demandés.

    Args:
        tableau (array): Tableau de pixel.
        nom_image_sortie (str): Nom de sortie de l'image.
        format (str): Format de l'image.
    """
    global sortie

    image = Image.fromarray(tableau)
    
    image.save(sortie + nom_image_sortie + "." + format)


def affiche_from_tab(tab):
    """Représente le tableau de pixels sous forme d'image.

    Args:
        tab (array): Tableau de pixels.
    """
    Image.fromarray(tab).show()


# ================================= Essentiel ==================================

def zone(nom_image,h_debut,h_fin,l_debut,l_fin):
    """Renvoie un tableau représentant la zone définie par les 4 dernières
    variables.

    Args:
        nom_image (str): Nom de l'image à utiliser.
        h_debut (int): Indique le début de la hauteur.
        h_fin (int): Indique la fin de la hauteur.
        l_debut (int): Indique le début de la largeur.
        l_fin (int): Indique la fin de la largeur.
    
    Return:
        (array): Tableau représentant la zone.
    """
    tab = image_to_tab(nom_image)
    h,l = len(tab),len(tab[0])

    if(not(0 <= h_debut < h and h_debut < h_fin < h 
        and 0 <= l_debut < l and l_debut < l_fin < l)):
        return None

    return np.uint8(tab[h_debut:h_fin,l_debut:l_fin])


def echange_zone(nom_image,nb_l,nb_c,depart,arrivee):
    """Renvoie le tableau de pixels avec les deux zones échangées.

    Args:
        nom_image (str): Nom de l'image à utiliser.
        nb_l (int): Indique le nombre de lignes des zones à échanger.
        nb_c (int): Indique le nombre de colonnes des zones à échanger.
        depart (tuple): Indique la position du pixel de départ.
        arrivee (tuple): Indique la position du pixel de arrivee.
    
    Return:
        (array): Tableau de pixels.
    """
    tab = image_to_tab(nom_image)
    h,l = len(tab),len(tab[0])

    dx,dy = depart
    ax,ay = arrivee

    if(nb_l <= 0 or nb_c <= 0 or not(
        0 <= dx < h and dx < dx + nb_l < h and
        0 <= dy < l and dy < dy + nb_c < l and
        0 <= ax < h and ax < ax + nb_l < h and
        0 <= ay < l and ay < ay + nb_c < l and
        (abs(dx - ax) >= nb_l or abs(dy - ay) >= nb_c)
        )):
        return None

    d = tab[dx:dx+nb_l,dy:dy+nb_c].copy()
    a = tab[ax:ax+nb_l,ay:ay+nb_c].copy()
    tab[dx:dx+nb_l,dy:dy+nb_c] = a
    tab[ax:ax+nb_l,ay:ay+nb_c] = d

    return np.uint8(tab)


def couleur(nom_image,nb_couleur):
    """Renvoie l'une des couches RGB d'une image.

    Args:
        nom_image (str): Nom de l'image à utiliser.
        nb_couleur (int): R:0, G:1, B:2.
        format (str): Format de l'image.

    Return:
        (array): Tableau de pixels.
    """
    tableau = image_to_tab(nom_image)
    h,l = len(tableau),len(tableau[0])

    tab = np.zeros(h*l*3,dtype=int).reshape(h,l,3)

    for x in range(h):
        for y in range(l):
            tab[x][y][nb_couleur] = tableau[x][y][nb_couleur]

    return np.uint8(tab)


def filtre_couleur(nom_image,couleur):
    """Renvoie l'image passée sous le filtre d'ue couleur.

    Args:
        nom_image (str): Nom de l'image à utiliser.
        couleur (tuple): 3 nombres définissant une couleur.

    Return:
        (array): Tableau de pixels.
    """
    tab = image_to_tab(nom_image)
    h,l = len(tab),len(tab[0])
    
    r,g,b = couleur
    r /= 255
    g /= 255
    b /= 255

    for x in range(h):
        for y in range(l):
            tab[x][y][0] *= r
            tab[x][y][1] *= g
            tab[x][y][2] *= b

    return np.uint8(tab) 


def negatif(nom_image):
    """Renvoie le négatif de l'image

    Args:
        nom_image (str): Nom de l'image à utiliser.

    Return:
        (array): Tableau de pixels.
    """
    tab = image_to_tab(nom_image)
    h,l = len(tab),len(tab[0])

    for x in range(h):
        for y in range(l):
            for p in range(3):
                tab[x][y][p] = 255 - tab[x][y][p]

    return np.uint8(tab)

def negatif_v2(nom_image):
    """Renvoie le négatif de l'image

    Args:
        nom_image (str): Nom de l'image à utiliser.

    Return:
        (array): Tableau de pixels.
    """
    return np.uint8(255 - tab_to_image(nom_image)) 


def niv_gris(nom_image):
    """Renvoie le négatif de l'image.

    Args:
        nom_image (str): Nom de l'image à utiliser.

    Return:
        (array): Tableau de pixels.
    """
    tab = image_to_tab(nom_image)
    h,l = len(tab),len(tab[0])

    for x in range(h):
        for y in range(l):
            g = 0.299 * tab[x][y][0] + 0.587 * tab[x][y][1] + \
                0.114* tab[x][y][2]
            
            for p in range(3):
                tab[x][y][p] = g

    return np.uint8(tab)


def affiche_image_histo(nom_image):
    """Affiche l'histogramme de l'image.

    Args:
        nom_image (str): Nom de l'image à utiliser.
    """
    tab = image_to_tab(nom_image)
    niv = []
    h,l = len(tab),len(tab[0])

    for x in range(h):
        for y in range(l):
            g = 0.299 * tab[x][y][0] + 0.587 * tab[x][y][1] + \
                0.114* tab[x][y][2]
            niv += [floor(g)]

    x = np.linspace(0,256,256)
    data = [niv.count(i) for i in range(256)]

    plt.axis([0,256,0,max(data)+5])
    print(len(x),len(data))

    plt.xlabel("Niveau de gris")
    plt.ylabel("Nombre de pixels")
    plt.title("Histogramme de "+nom_image)

    plt.plot(x,data)
    plt.show()
    plt.close()

def affiche_image_histo_propre(nom_image):
    """Affiche l'histogramme de l'image, en éliminant les valeurs nulles.
    On obtient un résultat plus propre.

    Args:
        nom_image (str): Nom de l'image à utiliser.
    """
    tab = image_to_tab(nom_image)
    niv = []
    h,l = len(tab),len(tab[0])

    for x in range(h):
        for y in range(l):
            g = 0.299 * tab[x][y][0] + 0.587 * tab[x][y][1] + \
                0.114* tab[x][y][2]
            niv += [floor(g)]

    x = np.linspace(0,256,256)
    data = [niv.count(i) for i in range(256)]

    for i in range(1,255):
        if(data[i] == 0):
            data[i] = floor((data[i-1] + data[i+1])/2)

    plt.axis([0,256,0,max(data)+5])
    print(len(x),len(data))

    plt.xlabel("Niveau de gris")
    plt.ylabel("Nombre de pixels")
    plt.title("Histogramme de "+nom_image)

    plt.plot(x,data)
    plt.show()
    plt.close()


def binaire(n):
    """Renvoie l'écriture binaire de n.

    Args:
        n (int): Nombre.

    Return:
        (list): Ecriture binaire.
    """
    b = []
    q = n

    while q != 0:
        q,r = divmod(q,2)
        b += [r]

    b = b[::-1]
    b = [0] * (8 - len(b)) + b

    return b

def binaire_v2(n):
    """Renvoie l'écriture binaire de n.

    Args:
        n (int): Nombre.

    Return:
        (list): Ecriture binaire.
    """
    tab = [n & 128, n & 64, n & 32, n & 16, n & 8, n & 4, n & 2, n & 1]

    return [0 if t == 0 else 1 for t in tab]

def binaire_v3(n):
    """Renvoie l'écriture binaire de n.

    Args:
        n (int): Nombre.

    Return:
        (list): Ecriture binaire.
    """
    binary = str(bin(n))[2:]
    
    return [int(b) for b in binary]


def alea_bits_faibles(n):
    """Renvoie un entier présentant les mêmes bits forts que n.

    Args:
        n (int): Nombre.

    Return:
        (int): Autre nombre. Peut-être.
    """
    b = binaire(n)
    l = len(b)
    
    if(l > 8):
        return None
    elif(l < 4):
        b = [0] * (4-l) + b

    for i in range(4):
        b[-1-i] = randint(0,1)

    return sum([b[i] * 2**(l-i-1) for i in range(l)])


def alea_bits_faibles_v2(n):
    """Renvoie un entier présentant les mêmes bits forts que n.

    Args:
        n (int): Nombre.

    Return:
        (int): Autre nombre. Peut-être.
    """
    return (n & 240) | randint(0,15)


def image_alea(nom_image):
    """Renvoie une version modifiée de l'image.

    Args:
        nom_image (str): Nom de l'image à utiliser.
    """
    tab = image_to_tab(nom_image)
    h,l = len(tab),len(tab[0])

    for x in range(h):
        for y in range(l):
            for p in range(3):
                tab[x][y][p] = alea_bits_faibles_v2(tab[x][y][p])

    return np.uint8(tab)


def hide_img(nom_image1,nom_image2):
    """Renvoie l'image1 dissimulée dans l'image2.

    Args:
        nom_image1 (str): Image à cacher.
        nom_image2 (str): Image pour cacher.

    Return:
        (array): Tableau de pixels.
    """
    tab1 = image_to_tab(nom_image1)
    tab2 = image_to_tab(nom_image2)

    h,l = len(tab1),len(tab1[0])

    for x in range(h):
        for y in range(l):
            for p in range(3):
                tab2[x][y][p] = (tab2[x][y][p] & 240) | (tab1[x][y][p] >> 4)

    return np.uint8(tab2)


def find_image(tab):
    """Renvoie l'image dissimulée dans l'image apparente.

    Args:
        tab (array): Tableau de pixels.

    Return:
        (array): Tableau de pixels.
    """
    h,l = len(tab),len(tab[0])

    for x in range(h):
        for y in range(l):
            for p in range(3):
                tab[x][y][p] = ((tab[x][y][p] & 15) << 4) | 8

    return np.uint8(tab)


def find_image_v2(tab):
    """Renvoie l'image dissimulée dans l'image apparente.

    Args:
        tab (array): Tableau de pixels.

    Return:
        (array): Tableau de pixels.
    """
    return np.uint8(((tab & 15) << 4) | 8)


def hide_texte(message,nom_image):
    """Renvoie une image contenant le message caché.

    Args:
        message (str): Message à cacher.
        nom_image (str): Nom de l'image.

    Return:
        (array): Tableau de pixels.
    """
    tab = image_to_tab(nom_image)

    L = len(message)

    for i in range(8):
        tab[0][i][0] = (tab[0][i][0] & (~1)) | ((L >> (7-i)) & 1)

    for l in range(L):
        c = ord(message[l])

        for i in range(8):
            tab[l+1][i][0] = (tab[l+1][i][0] & (~1)) | ((c >> (7-i)) & 1)

    return np.uint8(tab)
 

def reveler_texte(nom_image):
    """Renvoie le texte caché dans une image.

    Args:
        message (str): Message à cacher.
        nom_image (str): Nom de l'image.

    Return:
        (str): message.
    """
    tab = image_to_tab(nom_image)

    L = 0

    for i in range(8):
        L = (L << 1) | (tab[0][i][0] & 1)

    message = ''

    for l in range(1,L+1):
        car = 0

        for i in range(8):
            car = (car << 1) | (tab[l,i,0] & 1)
        
        message += chr(car)

    return message


def read_hide_texte(nom_fichier,nom_image):
    """Renvoie l'image contenant le texte du fichier.
    
    Args:
        nom_fichier (str): Nom du fichier contenant le texte.
        nom_image (str): Nom de l'image.

    Return:
        (array): Tableau de pixels.
    """
    message = ''

    with open(nom_fichier, 'r') as fichier:
        message = fichier.read()

    if(len(message) <= 255):
        return hide_texte(message,nom_image)


def ecrire_reveler_texte(nom_image):
    """Enregistre dans un fichier txt le texte contenu dans l'image.

    Args:
        nom_image (str): Nom de l'image.
    """
    texte = reveler_texte(nom_image)
    nom_fichier = nom_image[:-4] + "_texte_cache.txt"

    with open(nom_fichier, 'w') as fichier:
        fichier.write(texte)


# ================ Affichage & enregistrement (pas intéressant) ================


def affiche_zone(nom_image,h_debut,h_fin,l_debut,l_fin):
    """Affiche la zone définie par les 4 dernières variables.

    Args:
        nom_image (str): Nom de l'image à utiliser.
        h_debut (int): Indique le début de la hauteur.
        h_fin (int): Indique la fin de la hauteur.
        l_debut (int): Indique le début de la largeur.
        l_fin (int): Indique la fin de la largeur.
    """
    tab = zone(nom_image,h_debut,h_fin,l_debut,l_fin)

    if tab == None: return None

    affiche_from_tab(tab)


def affiche_echange_zones(nom_image,nb_l,nb_c,depart,arrivee):
    """Affiche l'image avec les deux zones échangées.

    Args:
        nom_image (str): Nom de l'image à utiliser.
        nb_l (int): Indique le nombre de lignes des zones à échanger.
        nb_c (int): Indique le nombre de colonnes des zones à échanger.
        depart (tuple): Indique la position du pixel de départ.
        arrivee (tuple): Indique la position du pixel de arrivee.
    """
    tab = echange_zone(nom_image,nb_l,nb_c,depart,arrivee)

    if tab == None: return None

    affiche_from_tab(tab)


def couche_couleur(nom_image,nb_couleur,format):
    """Enregistre l'une des couches RGB d'une image.

    Args:
        nom_image (str): Nom de l'image à utiliser.
        nb_couleur (int): R:0, G:1, B:2.
        format (str): Format de l'image.
    """
    tab = couleur(nom_image,nb_couleur)

    tab_to_image(tab,nom_image[:-4] + '_' + str(nb_couleur),format)


def affiche_couche(nom_image,nb_couleur):
    """Affiche l'une des couches RGB d'une image.

    Args:
        nom_image (str): Nom de l'image à utiliser.
        nb_couleur (int): R:0, G:1, B:2.
        format (str): Format de l'image.
    """
    tab = couleur(nom_image,nb_couleur)

    affiche_from_tab(tab)


def affiche_filtre_couleur(nom_image,couleur):
    """Enregistre l'une des couches RGB d'une image.

    Args:
        nom_image (str): Nom de l'image à utiliser.
        couleur (tuple): 3 nombres définissant une couleur.
    """
    tab = filtre_couleur(nom_image,couleur)

    affiche_from_tab(tab)


def affiche_negatif(nom_image):
    """Affiche le négatif de l'image

    Args:
        nom_image (str): Nom de l'image à utiliser.
    """
    tab = negatif(nom_image)

    affiche_from_tab(tab)


def niveau_gris(nom_image):
    """Affiche le négatif de l'image.

    Args:
        nom_image (str): Nom de l'image à utiliser.
    """
    tab = niv_gris(nom_image)
    
    tab_to_image(tab,nom_image[:-4] + "_niv_gris",'png')


def affiche_image_alea(nom_image):
    """Affiche une version modifiée de l'image.

    Args:
        nom_image (str): Nom de l'image à utiliser.
    """
    tab = image_alea(nom_image)

    affiche_from_tab(tab)


def cacher_image(nom_image1,nom_image2,nom_image_sortie,format_sortie):
    """Enregistre l'image1 dissimulée dans l'image2.

    Args:
        nom_image1 (str): Image à cacher.
        nom_image2 (str): Image pour cacher.
        nom_image_sortie (str): Nom sous lequel enregistrer.
        format_sortie (str): Format de la sortie.
    """
    tab = hide_img(nom_image1,nom_image2)

    tab_to_image(tab,nom_image_sortie,format_sortie)


def reveler_image(nom_image,nom_image_sortie,format_sortie):
    """Enregistre l'image dissimulée dans l'image apparente.

    Args:
        nom_image (str): Image à analyser.
        nom_image_sortie (str): Nom sous lequel enregistrer.
        format_sortie (str): Format de la sortie.
    """
    tab = find_image(image_to_tab(nom_image))

    tab_to_image(tab,nom_image_sortie,format_sortie)


def cacher_texte(message,nom_image):
    """Enregistre une image contenant le message caché.

    Args:
        message (str): Message à cacher.
        nom_image (str): Nom de l'image.
    """
    tab = hide_texte(message,nom_image)

    tab_to_image(tab,nom_image[:-4] + "_codee",'png')


def lire_cacher_texte(nom_fichier,nom_image):
    """Enregistre l'image contenant le texte du fichier.

    Args:
        nom_fichier (str): Nom du fichier contenant le texte.
        nom_image (str): Nom de l'image.
    """
    tab = read_hide_texte(nom_fichier,nom_image)

    if tab == None: return None
    
    tab_to_image(tab,nom_image[:-4] + '_codee','png')