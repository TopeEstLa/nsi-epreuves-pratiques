# Exercice 1

def convertir(tab):
    """
    Convertit un tableau représentant un nombre binaire en un nombre décimal
    :param tab:
    :return:
    """
    tab.reverse()
    res = 0
    for i in range(len(tab)):
        res += tab[i] * 2 ** i
    return res


assert convertir([1, 0, 1, 0, 0, 1, 1]) == 83
assert convertir([1, 0, 0, 0, 0, 0, 1, 0]) == 130


# Exercice 2

def trie_insertion(tab):
    """
    Trie un tableau par insertion
    :param tab:
    :return:
    """
    for i in range(1, len(tab)):
        j = i
        while j > 0 and tab[j - 1] > tab[j]:
            tab[j - 1], tab[j] = tab[j], tab[j - 1]
            j -= 1


liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]
print(liste)
trie_insertion(liste)
print(liste)
