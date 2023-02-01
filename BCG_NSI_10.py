# Exercice 1

def maxliste(tab):
    """
    :param tab: tableau d'entiers
    :return: le plus grand élément du tableau
    """
    if len(tab) == 1:
        return tab[0]

    return max(tab[0], maxliste(tab[1:]))


assert maxliste([98, 12, 104, 23, 131, 9]) == 131
assert maxliste([-27, 24, -3, 15]) == 24


# Exercice 2

class Pile:
    """
    Classe définissant une pile
    """

    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        """
        Renvoie True si la pile est vide, False sinon
        """
        return self.valeurs == []

    def empiler(self, c):
        """
        Place l’élément c au sommet de la pile
        """
        self.valeurs.append(c)

    def depiler(self):
        """
        Supprime l’élément placé au sommet de la pile, à
       condition
        qu’elle soit non vide
        """
        if self.est_vide() == False:
            self.valeurs.pop()


def parenthesage(ch):
    p = Pile()
    for c in ch:
        if c == '(':
            p.empiler(c)
        elif c == ')':
            if p.est_vide():
                return False
            p.depiler()
    return p.est_vide()


assert parenthesage("((()())(()))") == True
assert parenthesage("())(()") == False
assert parenthesage("(())(()") == False
