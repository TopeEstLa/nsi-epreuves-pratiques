# Exercice 1

def min_et_max(tab):
    if tab is None:
        raise ValueError("tab is None")

    if len(tab) == 0:
        raise ValueError("tab is empty")

    dict = {'min': tab[0], 'max': tab[0]}
    for element in tab:
        if element < dict['min']:
            dict['min'] = element
        if element > dict['max']:
            dict['max'] = element
    return dict


assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert min_et_max([0, 1, 2, 3]) == {'min': 0, 'max': 3}
assert min_et_max([3]) == {'min': 3, 'max': 3}
assert min_et_max([1, 3, 2, 1, 3]) == {'min': 1, 'max': 3}
assert min_et_max([-1, -1, -1, -1, -1]) == {'min': -1, 'max': -1}


# Exercice 2

class Carte:
    def __init__(self, c, v):
        self.couleur = c
        self.valeur = v

    def get_valeur(self):
        valeurs = ['As', '2', '3', '4', '5', '6', '7', '8', '9',
                   '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def get_couleur(self):
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]


class Paquet_de_cartes:
    def __init__(self):
        self.paquet = []
        for c in range(1, 5):
            for v in range(1, 14):
                self.paquet.append(Carte(c, v))

    def get_carte(self, pos):
        assert 0 <= pos < len(self.paquet), "pos doit être compris entre 0 et 52"
        return self.paquet[pos]


jeu = Paquet_de_cartes()

assert jeu.get_carte(20).get_valeur() == '8'
assert jeu.get_carte(20).get_couleur() == 'coeur'

assert jeu.get_carte(0).get_valeur() == 'As'
assert jeu.get_carte(0).get_couleur() == 'pique'

assert jeu.get_carte(52).get_valeur() == 'Roi'