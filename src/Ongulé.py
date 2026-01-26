from src.Player import Player, ElementsAnimal, Plateau, Game
# from src.Cervidé import *
from src.helper_functions.colors import which_color

class Ongulé(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "ongulé"

class Sanglier(Ongulé):
    subcategory = "sanglier"
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "sanglier"
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.cost_card = 2

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        print(f"{self.subcategory} has no bonus.")
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        return self

    def points(self):
        print(f"10pts si vous avez au moins 1 Marcassin.")
        return self

class Marcassin(Ongulé):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "marcassin"
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.category = "ongulé"
        self.cost_card = 0

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        print(f"{self.subcategory} allows you to draw one card if the cost of the card \
            can be payed entierely in cards whose color is {self.couleur_feuille}.")
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        return self

    def points(self):
        print(f"1pt.")
        return self
