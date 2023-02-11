# Exercice 1

def nombre_de_mots(phrase):
    """
    Calcule le nombre de mots dans une phrase.
    :param phrase:
    :return:
    """
    nb_mots = 0
    for i in range(len(phrase)):
        if phrase[i] == ' ':
            if phrase[i + 1] != '?' or phrase[i + 1] != '!':
                nb_mots += 1
        elif phrase[i] == '.':
            nb_mots += 1

    return nb_mots


assert nombre_de_mots('Cet exercice est simple.') == 4
assert nombre_de_mots('Le point d exclamation est separe !') == 6
assert nombre_de_mots('Combien de mots y a t il dans cette phrase ?') == 10


# Exercice 2


class Noeud:

    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def getValeur(self):
        return self.valeur

    def droitExiste(self):
        return (self.droit is not None)

    def gaucheExiste(self):
        return (self.gauche is not None)

    def inserer(self, cle):
        """
        Insère une clé dans l'arbre binaire de recherche.
        :param cle:
        :return:
        """
        if cle < self.valeur:
            if self.gaucheExiste():
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droitExiste():
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)


arbre = Noeud(7)

for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

assert arbre.gauche.getValeur() == 3
assert arbre.droit.getValeur() == 9

assert arbre.gauche.gauche.getValeur() == 1
assert arbre.gauche.droit.getValeur() == 6
