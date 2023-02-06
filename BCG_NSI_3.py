# Exercice 1

def moyenne(tab):
    """
    Retourne la moyenne des éléments du tableau.
    :param tab: tableau d'entiers
    :return: moyenne des éléments du tableau
    """
    somme = 0
    somme_poids = 0
    for element in tab:
        somme += element[0] * element[1]
        somme_poids += element[1]

    if (somme_poids == 0):
        return None

    return somme / somme_poids


assert moyenne([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)]) == 5.5
assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142
assert moyenne([(3, 0), (5, 0)]) is None

# Exercice 2

coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def affiche(dessin):
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def zoomListe(liste_depart, k):
    liste_finale = []
    for elt in liste_depart:
        for i in range(k):
            liste_finale.append(elt)
    return liste_finale


def zoomDessin(grille, k):
    grille_finale = []
    for ligne in grille:
        grille_finale.append(zoomListe(ligne, k))
    return zoomListe(grille_finale, k)


affiche(coeur)
affiche(zoomDessin(coeur, 2))
