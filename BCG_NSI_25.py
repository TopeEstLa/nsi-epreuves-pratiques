# Exercice 1

def enumere(tab):
    """
    Renvoi un dictionnaire avec pour clé l'élément de tab et pour valeur son indice.
    :param tab:
    :return:
    """
    dico = {}
    for i in range(len(tab)):
        if tab[i] not in dico:
            dico[tab[i]] = [i]
        else:
            dico[tab[i]].append(i)
    return dico


assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}


# Exercice 2

class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None


def parcours(arbre, liste):
    if arbre is not None:
        parcours(arbre.fg, liste)
    liste.append(arbre.v)
    parcours(arbre.fd, liste)
    return liste


def insere(arbre, cle):
    """
    Insère la clé dans l'arbre binaire de recherche.
    :param arbre:
    :param cle:
    :return:
    """
    if arbre.v > cle:
        if arbre.fg is not None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd is not None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

