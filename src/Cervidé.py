from src.Player import Player, ElementsAnimal, Plateau, Game
# from src.Ongulé import *

class Cervidé(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "cervidé"

class CerfElaphe(Cervidé):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.category = "cervidé" and "ongulé"
        self.subcategory = "cerf élaphe"
        self.cost_card = 2
        """
        Couleurs : orange, jaune, marron
        """

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

class Chevreuil(Cervidé):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.category = "cervidé" and "ongulé"
        self.subcategory = "chevreuil"
        self.cost_card = 2
        """
        Couleurs : bleu foncé, jaune, vert foncé, orange, vert clair
        """

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
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.category = "cervidé" and "ongulé"
        self.subcategory = "daim"
        self.cost_card = 2
        """
        Couleurs : rouge, jaune, vert clair
        """

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
