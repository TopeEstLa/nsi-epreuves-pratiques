# Exercice 1
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]


def mini(moyen, annees):
    """
    Retourne la température minimale et l'année correspondante.
    :param moyen:
    :param annees:
    :return: couple (température minimale, année correspondante)
    """
    min_index = 0

    for i in range(1, len(moyen)):
        if moyen[i] < moyen[min_index]:
            min_index = i

    return moyen[min_index], annees[min_index]


assert mini(t_moy, annees) == (12.5, 2016)


# Exercice 2

def inverse_chaine(chaine):
    """
    Retourne la chaine inversée.
    :param chaine:
    :return:
    """
    result = ""
    for caractere in chaine:
        result = caractere + result
    return result


assert inverse_chaine("bac") == "cab"


def est_palindrome(chaine):
    """
    Retourne True si la chaine est un palindrome, False sinon.
    :param chaine:
    :return: booléen
    """
    return chaine == inverse_chaine(chaine)


assert est_palindrome("NSI") == False
assert est_palindrome("ISN-NSI") == True


def est_nbre_palindrome(nbre):
    """
    Retourne True si le nombre est un palindrome, False sinon.
    :param nbre:
    :return:
    """
    return est_palindrome(str(nbre))


assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True
