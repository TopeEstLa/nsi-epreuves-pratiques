# Exercice 1

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]


def rangement_valeurs(note):
    tab = [0] * 11
    for i in range(len(note)):
        tab[note[i]] += 1

    return tab


assert rangement_valeurs(notes_eval) == [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]


# Exercice 2

def dec_to_bin(nb_dec):
    """
    Convertit un nombre décimal en binaire.
    :param nb_dec:
    :return:
    """
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)


assert dec_to_bin(25) == '11001'


def bin_to_dec(nb_bin):
    """
    Convertit un nombre binaire en décimal sans utilisation de int().
    :param nb_bin:
    :return:
    """
    if nb_bin == '0':
        return 0
    elif nb_bin == '1':
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return bin_to_dec(nb_bin[:-1]) * 2 + bit_droit


assert bin_to_dec('101010') == 42
