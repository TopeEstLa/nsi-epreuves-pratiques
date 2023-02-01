# Exercice 1

def recherche_indices_classement(value, tab):
    """
    Retourne les indices des éléments inférieurs, égaux et supérieurs à value.
    :param value:
    :param tab:
    :return: tuple contenant les indices des éléments inférieurs, égaux et supérieurs à value
    """
    inf = []
    equals = []
    sup = []
    for i in range(len(tab)):
        if tab[i] < value:
            inf.append(i)
        elif tab[i] == value:
            equals.append(i)
        else:
            sup.append(i)

    return inf, equals, sup


assert recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]) == ([0, 3, 7], [1, 6], [2, 4, 5])
assert recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]) == ([0, 2, 5], [], [1, 3, 4])
assert recherche_indices_classement(3, [1, 1, 1, 1]) == ([0, 1, 2, 3], [], [])
assert recherche_indices_classement(3, []) == ([], [], [])


# Exercice 2

def moyenne(nom, dico_result):
    """
    Retourne la moyenne de l'élève nom.
    :param nom:
    :param dico_result:
    :return: moyenne de l'élève nom
    """
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return -1


resultats = {'Dupont': {
    'DS1': [15.5, 4],
    'DM1': [14.5, 1],
    'DS2': [13, 4],
    'PROJET1': [16, 3],
    'DS3': [14, 4]
},
    'Durand': {
        'DS1': [6, 4],
        'DM1': [14.5, 1],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [8, 4],
        'DS4': [15, 4]
    }
}

assert moyenne('Dupont', resultats) == 14.1
assert moyenne('Durand', resultats) == 9.3
