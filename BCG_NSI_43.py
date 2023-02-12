# Exercice 1

def ecriture_binaire_entier_positif(n):
    """
    Ecrit l'écriture binaire d'un entier positif.
    :param n:
    :return tableau d'entiers correspondant à l'écriture binaire de n:
    """
    if n == 0:
        return [0]
    if n == 1:
        return [1, 0]

    tab = []
    while n > 0:
        tab.append(n % 2)
        n //= 2
    return tab[::-1]


assert ecriture_binaire_entier_positif(0) == [0]
assert ecriture_binaire_entier_positif(2) == [1, 0]
assert ecriture_binaire_entier_positif(105) == [1, 1, 0, 1, 0, 0, 1]


# Exercice 2

def tri_bulles(tab):
    """
    Trie un tableau par tri à bulles.
    :param tab:
    :return:
    """
    for i in range(len(tab)):
        for j in range(len(tab) - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab


assert tri_bulles([]) == []
assert tri_bulles([7]) == [7]
assert tri_bulles([9, 3, 7, 2, 3, 1, 6]) == [1, 2, 3, 3, 6, 7, 9]
assert tri_bulles([9, 7, 4, 3]) == [3, 4, 7, 9]
