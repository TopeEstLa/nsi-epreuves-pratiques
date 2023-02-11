# Exercice 1

a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'], \
     'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'], \
     'H': ['', '']}


def taille(arb, lettre):
    """
    Calcule la taille d'un arbre implémenté sous forme de dictionnaire.
    :param arb:
    :return:
    """
    if arb[lettre][0] == '' and arb[lettre][1] == '':
        return 1
    if arb[lettre][0] == '':
        return 1 + taille(arb, arb[lettre][1])
    if arb[lettre][1] == '':
        return 1 + taille(arb, arb[lettre][0])
    return 1 + taille(arb, arb[lettre][0]) + taille(arb, arb[lettre][1])


assert taille(a, 'F') == 9


# Exercice 2

def tri_selection(tab):
    N = len(tab)
    for k in range(N - 1):
        i_min = k
        for i in range(k + 1, N):
            if tab[i] < tab[i_min]:
                i_min = i
        tab[i_min], tab[k] = tab[k], tab[i_min]


liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
assert liste == [6, 12, 18, 21, 25, 41, 55]