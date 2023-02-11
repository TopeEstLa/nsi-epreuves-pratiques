# Exercice 1

def correspond(mot, mot_a_trous):
    mot_trouve = ''
    for i in range(len(mot_a_trous)):
        if mot_a_trous[i] == '*':
            mot_trouve += mot[i]
        else:
            mot_trouve += mot_a_trous[i]
    return mot_trouve == mot


assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False
assert correspond('STOP', 'S*') == False
assert correspond('AUTO', '*UT*') == True


# Exercice 2

def est_cyclique(plan):
    """
    Détermine si un plan est cyclique.
    :param plan:
    :return:
    """

    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinataires = 1
    while destinataire != 'A':
        destinataire = plan[destinataire]
        nb_destinataires += 1
    return nb_destinataires == len(plan)


assert est_cyclique({'A': 'E', 'F': 'A', 'C': 'D', 'E': 'B', 'B': 'F',
                     'D': 'C'}) == False
assert est_cyclique({'A': 'E', 'F': 'C', 'C': 'D', 'E': 'B', 'B': 'F',
                     'D': 'A'}) == True
assert est_cyclique({'A': 'B', 'F': 'C', 'C': 'D', 'E': 'A', 'B': 'F',
                     'D': 'E'}) == True
assert est_cyclique({'A': 'B', 'F': 'A', 'C': 'D', 'E': 'C', 'B': 'F',
                     'D': 'E'}) == False
