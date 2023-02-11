# Exercice 1

def nbr_occurrences(chaine):
    """
    Renvoi un dict avec le nombre d'occurrences de chaque caractère.
    :param chaine:
    :return:
    """
    dico = {}
    for char in chaine:
        if char in dico:
            dico[char] += 1
        else:
            dico[char] = 1
    return dico


assert nbr_occurrences("Hello world !") == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1,
                                            'r': 1, 'd': 1, '!': 1}


# Exercice 2

def fusion(lst1, lst2):
    """
    Renvoi une liste triée contenant les éléments de lst1 et lst2.
    :param lst1:
    :param lst2:
    :return:
    """
    lst = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    while i < len(lst1):
        lst.append(lst1[i])
        i += 1
    while j < len(lst2):
        lst.append(lst2[j])
        j += 1
    return lst


assert fusion([1, 6, 10], [0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]
