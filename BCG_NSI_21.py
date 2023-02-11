# Exercice 1

def delta(tab):
    """
    Codage par différences successives.
    :param tab:
    :return:
    """
    if len(tab) == 0:
        return []

    if len(tab) == 1:
        return [tab[0]]

    return [tab[0]] + [tab[i] - tab[i - 1] for i in range(1, len(tab))]


assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]


# Exercice 2

class Noeud:
    """
    Noeud d'un arbre binaire.
    """

    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        return str(self.valeur)

    def est_une_feuille(self):
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    """
    Affiche une expression arithmétique en notation infixe.
    :param e:
    :return:
    """
    s = ''

    if e.est_une_feuille():
        return str(e)

    if e.gauche is not None:
        s += '(' + expression_infixe(e.gauche)
        s += str(e)
    if e.droit is not None:
        s += expression_infixe(e.droit) + ')'

    return s


def expression_infixe_v2(e):
    """
    Affiche une expression arithmétique en notation infixe.
    :param e:
    :return:
    """
    if e is None:
        return ''

    if e.est_une_feuille():
        return str(e)

    return f'({expression_infixe_v2(e.gauche)}{e}{expression_infixe_v2(e.droit)})'


e = Noeud(Noeud(Noeud(None, 3, None),
                '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
          '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))

assert expression_infixe(e) == '((3*(8+7))-(2+1))'
