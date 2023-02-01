# Exercice 1

class ABR():

    def __init__(self, v0, g0=None, d0=None):
        self.cle = v0
        self.gauche = g0
        self.droit = d0

    def __str__(self):
        return "(" + str(self.gauche) + "," + str(self.cle) + "," + str(self.droit) + ")"

    def __repr__(self):
        return self.__str__()


n0 = ABR(0)
n3 = ABR(3)
n2 = ABR(2, d0=n3)
abr1 = ABR(1, n0, n2)

assert abr1.__str__() == "((None,0,None),1,(None,2,(None,3,None)))"


def ajoute(cle, a):
    """
    Ajoute une clé dans un ABR
    :param cle:
    :param a:
    :return:
    """
    if a is None:
        return ABR(cle)
    elif cle == a.cle:
        return a
    elif cle < a.cle:
        a.gauche = ajoute(cle, a.gauche)
    else:
        a.droit = ajoute(cle, a.droit)
    return a


# assert ajoute(4, abr1).__str__() == "((None,0,None),1,(None,2,(None,3,(None,4,None))))"
# assert ajoute(-5, abr1).__str__() == "(((None,-5,None),0,None),1,(None,2,(None,3,None)))"
# assert ajoute(2, abr1).__str__() == "((None,0,None),1,(None,2,(None,3,None)))"

# Exercice 2

def empaqueter(liste_masses, c):
    """
    Empaqueter des masses dans des boites
    :param liste_masses:
    :param c:
    :return: le nombre de boites utilisées
    """
    n = len(liste_masses)
    nb_boites = 0
    boites = [0] * n
    for masses in liste_masses:
        i = 0
        while i <= nb_boites and boites[i] + masses > c:
            i += 1
        if i == nb_boites:
            nb_boites += 1
        boites[i] += masses
    return nb_boites


assert empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11) == 5
