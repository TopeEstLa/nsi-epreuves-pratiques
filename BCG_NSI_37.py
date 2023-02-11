# Exercice 1

def recherche(elt, tab):
    """
    Recherche un élément dans un tableau.
    :param elt:
    :param tab:
    :return:
    """
    last_index = -1
    for i in range(len(tab)):
        if tab[i] == elt:
            last_index = i

    return last_index


assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 0, 42, 7]) == 0
assert recherche(1, [1, 50, 1]) == 2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5

# Exercice 2

class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octet(self):
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        return self.adresse == "192.168.0.0" or self.adresse == "192.168.0.255"

    def adresse_suivante(self):
        """
        Calcule l'adresse IP suivante.
        :return:
        """
        if self.liste_octet()[3] < 254:
            octet_nouveau = self.liste_octet()[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

    def __str__(self):
        return self.adresse


adresse1 = AdresseIP("192.168.0.1")
adresse2 = AdresseIP("192.168.0.2")
adresse3 = AdresseIP("192.168.0.0")

assert adresse1.est_reservee() == False
assert adresse2.est_reservee() == False
assert adresse3.est_reservee() == True

assert adresse2.adresse_suivante().__str__() == "192.168.0.3"