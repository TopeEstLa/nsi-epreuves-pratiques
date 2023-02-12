# Exercice 1

def tri_selection(tab):
    """
    Tri par sélection.
    :param tab:
    :return:
    """
    for i in range(len(tab)):
        min = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        tab[i], tab[min] = tab[min], tab[i]

    return tab


assert tri_selection([1, 52, 6, -9, 12]) == [-9, 1, 6, 12, 52]

# Exercice 2

from random import randint


def plus_ou_moins():
    """
    Jeu du plus ou moins.
    :return:
    """
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1
    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre était ", nb_test)

plus_ou_moins()