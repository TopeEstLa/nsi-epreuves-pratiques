# Exercice 1

def fusion(tab1, tab2):
    """
    Fusionne deux tableaux triés en un seul tableau trié.
    :param tab1:
    :param tab2:
    :return: tableau trié
    """
    tab = []
    i = 0
    j = 0

    while i < len(tab1) and j < len(tab2):
        if tab1[i] < tab2[j]:
            tab.append(tab1[i])
            i += 1
        else:
            tab.append(tab2[j])
            j += 1

    while i < len(tab1):
        tab.append(tab1[i])
        i += 1

    while j < len(tab2):
        tab.append(tab2[j])
        j += 1

    return tab


assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]


def fusion_recur(tab1, tab2):
    """
    Fusionne deux tableaux triés en un seul tableau trié.
    :param tab1:
    :param tab2:
    :return: tableau trié
    """
    if len(tab1) == 0:
        return tab2
    elif len(tab2) == 0:
        return tab1
    elif tab1[0] < tab2[0]:
        return [tab1[0]] + fusion_recur(tab1[1:], tab2)
    else:
        return [tab2[0]] + fusion_recur(tab1, tab2[1:])


assert fusion_recur([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion_recur([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion_recur([4], [2, 6]) == [2, 4, 6]

# Exercice 2
romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def traduire_romain(nombre):
    """
    Traduit un nombre romain en décimal.
    :param nombre:
    :return: nombre en decimal
    """
    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]


assert traduire_romain("XIV") == 14
assert traduire_romain("CXLII") == 142
assert traduire_romain("MMXXIII") == 2023
