# Exercice 1

def recherche(carractere, chaine):
    """
    Recherche un élément dans un tableau.
    :param elt:
    :param tab:
    :return:
    """
    occurence = 0
    for elt in chaine:
        if elt == carractere:
            occurence += 1
    return occurence


assert recherche('e', "sciences") == 2
assert recherche('i', "mississippi") == 4
assert recherche('a', "mississippi") == 0

# Exercice 2

valeurs = [100, 50, 20, 10, 5, 2, 1]


def rendu_glouton(a_rendre, rang):
    """
    Calcule le rendu glouton d'un montant.
    :param a_rendre:
    :param rang:
    :return:
    """
    if a_rendre == 0:
        return 0
    v = valeurs[rang]
    if v <= a_rendre:
        return 1 + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang + 1)


assert rendu_glouton(67, 0) == [50, 10, 5, 2]
assert rendu_glouton(291, 0) == [100, 100, 50, 20, 20, 1]
