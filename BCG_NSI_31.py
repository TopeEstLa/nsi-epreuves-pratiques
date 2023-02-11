# Exercice 1


def nb_repetitions(nbr, tab):
    """
    Calcule le nombre de répétitions d'un nombre dans un tableau.
    :param nbr:
    :param tab:
    :return:
    """
    nb = 0
    for element in tab:
        if element == nbr:
            nb += 1
    return nb


assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(5, [2, 3, 6, 9]) == 0


# Exercice 2

def binaire(a):
    """
    Convertit un nombre décimal en binaire.
    :param a:
    :return:
    """
    bin_a = str(a % 2)
    a = a // 2
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a


assert binaire(0) == '0'
assert binaire(77) == '1001101'
