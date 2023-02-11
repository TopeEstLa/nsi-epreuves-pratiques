# Exercice 1

def fibonacci(u):
    """
    Calcule le terme u de la suite de Fibonacci.
    :param u:
    :return:
    """
    if u == 0:
        return 0
    elif u == 1:
        return 1
    else:
        return fibonacci(u - 1) + fibonacci(u - 2)


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025


# assert fibonacci(45) == 1134903170

# Exercice 2

def pantheon(eleves, notes):
    """
    Calcule le panthéon des élèves.
    :param eleves:
    :param notes:
    :return:
    """
    note_maxi = 0
    meilleur_eleves = []
    for i in range(len(eleves)):
        if notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleur_eleves = [eleves[i]]
        elif notes[i] == note_maxi:
            meilleur_eleves.append(eleves[i])

    return note_maxi, meilleur_eleves


eleves_nsi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]

assert pantheon(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h'])
assert pantheon([], []) == (0, [])
