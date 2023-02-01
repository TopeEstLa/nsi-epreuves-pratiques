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
    if a is None:
        return ABR(cle)
    if cle < a.cle:
        a.gauche = ajoute(cle, a.gauche)
    else:
        a.droit = ajoute(cle, a.droit)
    return a

#assert ajoute(4, abr1).__str__() == "((None,0,None),1,(None,2,(None,3,(None,4,None))))"
#assert ajoute(-5, abr1).__str__() == "(((None,-5,None),0,None),1,(None,2,(None,3,None)))"
#assert ajoute(2, abr1).__str__() == "((None,0,None),1,(None,2,(None,3,None)))"

# Exercice 2

