# Exercice 1


def ajoute_dictionnaires(d1, d2):
    """
    Ajoute les valeurs des deux dictionnaires.
    :param d1:
    :param d2:
    :return:
    """
    d3 = {}

    for cle in d1:
        d3[cle] = d1[cle]

    for cle in d2:
        if cle in d3:
            d3[cle] += d2[cle]
        else:
            d3[cle] = d2[cle]

    return d3


assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}

# Exercice 2

from random import randint


def nbre_coups():
    """
    Calcule le nombre de coups pour parcourir toutes les cases d'un jeu de l'oie (je suis pas sur que sa soit le bon jeu mais bon osef).
    :return:
    """
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % 12
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n = n + 1
    return n
