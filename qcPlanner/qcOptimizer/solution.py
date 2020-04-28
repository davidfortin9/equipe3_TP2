import sys

class Solution:

    def __init__(self):
        pass

    def evaluate(self):
        # TODO Ajouter le code pour calculer la valeur de la fonction objectif
        #      dans les classes dérivées
        # Nous supposons que la valeur de l'objetif doit être minimisée.
        # Par défaut, nous retournons donc la plus grande valeur possible pour
        # un nombre à virgule flottante.
        return sys.float_info.max

    def validate(self):
        # TODO Ajouter le code pour vérifier si une solution est réalisable
        #      dans les classes dérivées
        # Pour l'instant, nous avons une solution vide que nous considérons
        # toujour non réalisable.
        return False
