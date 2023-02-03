# Exercice 1

def verifie(tab):
    """
    Vérifie si un tableau est trié.
    :param tab:
    :return: True si le tableau est trié, False sinon
    """
    for i in range(1, len(tab)):
        if tab[i - 1] > tab[i]:
            return False
    return True


assert verifie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
assert verifie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == True
assert verifie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]) == False
assert verifie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == True


# Exercice 2

def depouille(urne):
    """
    Retourne un dictionnaire contenant le nombre de fois où chaque lettre est présente dans l'urne.
    :param urne: tableau de lettres
    :return: dictionnaire contenant le nombre de bulletins pour chaque candidat
    """
    resultat = {}

    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] += 1
        else:
            resultat[bulletin] = 1

    return resultat


assert depouille(['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']) == {'A': 3, 'B': 4, 'C': 3}
assert depouille(['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B', 'D', 'D', 'D', 'D', 'D']) == {'A': 3, 'B': 4,
                                                                                                  'C': 3, 'D': 5}
assert depouille(["A", "A", "B"]) == {'A': 2, 'B': 1}


def vainqueur(election):
    """
    Retourne le vainqueur d'une élection.
    :param election: dictionnaire contenant le nombre de bulletins pour chaque candidat
    :return: le(s) vainqueur(s)
    """
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
        vainqueur = candidat
    list_finale = [nom for nom in election if election[nom] == nmax]

    return list_finale


assert vainqueur({'A': 3, 'B': 4, 'C': 3}) == ['B']
assert vainqueur({'A': 3, 'B': 4, 'C': 3, 'D': 5}) == ['D']
assert vainqueur({'A': 2, 'B': 2}) == ['A', 'B']
assert vainqueur({'A': 1, 'B': 2, "C": 1, "D": 2}) == ['B', 'D']
