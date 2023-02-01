# Exercice 1

def recherche(a, tab):
    """
    Recherche le nombre d'occurences d'un élément dans un tableau
    :param a:
    :param tab:
    :return: le nombre d'occurences de a dans tab
    """
    nb = 0
    for elt in tab:
        if elt == a:
            nb += 1
    return nb


assert recherche(5, []) == 0
assert recherche(5, [-2, 3, 4, 8]) == 0
assert recherche(5, [-2, 3, 1, 5, 3, 7, 4]) == 1
assert recherche(5, [-2, 5, 3, 5, 4, 5]) == 3

# Exercice 2
pieces = [1, 2, 5, 10, 20, 50, 100, 200]


def rendu_monnaie(somme_due, somme_versee):
    """
    Renvoie le rendu de monnaie
    :param somme_due:
    :param somme_versee:
    :return: liste des pièces à rendre
    """
    rendu = somme_versee - somme_due
    a_rendre = []
    i = len(pieces) - 1
    while rendu > 0:
        if rendu >= pieces[i]:
            rendu -= pieces[i]
            a_rendre.append(pieces[i])
        else:
            i -= 1
    return a_rendre


assert rendu_monnaie(700, 700) == []
assert rendu_monnaie(102, 500) == [200, 100, 50, 20, 20, 5, 2, 1]
