# Exercice 1

def recherche(tab, value):
    start = 0
    end = len(tab) - 1

    while start <= end:
        midle = (start + end) // 2

        if tab[midle] > value:
            end = midle - 1
        elif tab[midle] < value:
            start = midle + 1
        else:
            return midle
    return -1


assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == -1

# Exercice 2
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def position_alphabet(lettre):
    return ord(lettre) - ord('A')


def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat


assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
