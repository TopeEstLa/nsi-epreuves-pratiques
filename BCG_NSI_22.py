# Exercice 1

def liste_puissances(number, exp):
    """
    Renvoie la liste des puissances de number de 0 à exp.
    :param number:
    :param exp:
    :return: liste des puissances de number de 0 à exp.
    """
    tab = [number]

    for _ in range(exp - 1):
        tab.append(tab[-1] * number)

    return tab


assert liste_puissances(3, 5) == [3, 9, 27, 81, 243]
assert liste_puissances(-2, 4) == [-2, 4, -8, 16]


def liste_puissances_borne(a, borne):
    """
    Renvoie la liste des puissances de a jusqu'à atteindre la borne.
    :param a:
    :param borne:
    :return: liste des puissances de a jusqu'à atteindre la borne.
    """
    tab = [a]

    while tab[-1] < borne:
        tab.append(tab[-1] * a)

    return tab[:-1]


assert liste_puissances_borne(2, 16) == [2, 4, 8]
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16]
assert liste_puissances_borne(5, 5) == []

# Exercice 2

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}


def est_parfait(mot):
    """
    Renvoie le code additionne, le code concatene et si le mot est parfait.
    :param mot:
    :return:
    """
    code_concatene = ""
    code_additionne = [dico[c] for c in mot]
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
    code_additionne = sum(code_additionne)
    code_concatene = int(code_concatene)
    if code_concatene % code_additionne == 0:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait


assert est_parfait("PAUL") == (50, 1612112, False)
assert est_parfait("ALAIN") == (37, 1121914, True)
