# Exercice 1

def moyenne(tab):
    """
    Calcule la moyenne des éléments d'un tableau.
    :param tab:
    :return:
    """
    somme = 0
    for element in tab:
        somme += element
    return somme / len(tab)


assert moyenne([1.0, 2.0, 4.0]) == 2.3333333333333335


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


assert binaire(83) == '1010011'
assert binaire(127) == '1111111'
assert binaire(0) == '0'
