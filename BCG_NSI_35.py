# Exercice 1

a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]


def ou_exclusif(tab1, tab2):
    """
    Calcule le OU exclusif de deux tableaux de bits.
    :param tab1:
    :param tab2:
    :return:
    """
    tab = []
    for i in range(len(tab1)):
        if tab1[i] == tab2[i]:
            tab.append(0)
        else:
            tab.append(1)
    return tab


assert ou_exclusif(a, b) == [1, 1, 0, 1, 1, 0, 0, 1]
assert ou_exclusif(c, d) == [1, 1, 1, 0]


# Exercice 2

class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for
                        j in range(n)]

    def affiche(self):
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)

        for i in range(self.ordre):
            if self.somme_ligne(i) != s:
                return False
            if self.somme_col(i) != s:
                return False
        return True


listc1 = (1, 7, 7, 1)
liste = (3, 4, 5, 4, 4, 4, 5, 4, 3)
liste3bis = (2, 9, 4, 7, 0, 3, 6, 1, 8)

c2 = Carre(listc1, 2)
c3 = Carre(liste, 3)
c3Bis = Carre(liste3bis, 3)

assert c2.est_semimagique() == True
assert c3.est_semimagique() == True
assert c3Bis.est_semimagique() == False
