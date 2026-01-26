from src.Player import Player, ElementsAnimal, Plateau, Game
from src.Ongulé import Ongulé
from src.Cervidé import Cervidé
from src.helper_functions.colors import which_color

class CerfElaphe(Cervidé, Ongulé):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "cerf_élaphe"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.category = "cervidé" and "ongulé"
        self.cost_card = 2

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        print(f"{self.subcategory} allows you to place one Cervidé card in the Plateau if \
            the cost of the card can be payed entierely in cards whose color is {self.couleur_feuille}.")
        """
        to be reviewed
        card_throwed_1 = ElementsAnimal()
        card_throwed_2 = ElementsAnimal()
        """
        return self

    def points(self):
        print(f"1pt par Plant, and 1pt par Tree.")
        return self

class Chevreuil(Cervidé, Ongulé):
    subcategory = "chevreuil"
    def __init__(self, couleur_feuille=None):
        self.subcategory = "chevreuil"
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.category = "cervidé" and "ongulé"
        self.cost_card = 2

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        print(f"{self.subcategory} allows you to draw one card if the cost of the card \
            can be payed entierely in cards whose color is {self.couleur_feuille}.")
        """
        to be reviewed
        card_throwed_1 = ElementsAnimal()
        card_throwed_2 = ElementsAnimal()
        """
        return self

    def points(self):
        print(f"3pts per {self.couleur_feuille}.")
        return self

class Daim(Cervidé):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "daim"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.category = "cervidé" and "ongulé"
        self.cost_card = 2

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        print(f"{self.subcategory} allows you to draw two cards if the cost of the card \
            can be payed entierely in cards whose color is {self.couleur_feuille}.")
        """
        to be reviewed
        card_throwed_1 = ElementsAnimal()
        card_throwed_2 = ElementsAnimal()
        """
        return self

    def points(self):
        print(f"3pts per Ongulé.")
        return self
