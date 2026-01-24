from src.Player import Player, ElementsAnimal, Plateau, Game
# from src.Cervidé import *

class Ongulé(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "ongulé"

class Sanglier(Ongulé):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "sanglier"
        self.cost_card = 2
        """
        Couleurs : rouge, vert clair, marron, bleu clair
        """

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

class CerfElaphe(Ongulé):
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
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        return self

    def points(self):
        print(f"1pt par Plant, and 1pt par Tree.")
        return self

class Chevreuil(Ongulé):
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
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        return self

    def points(self):
        print(f"3pts per {self.couleur_feuille}.")
        return self

class Marcassin(Ongulé):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.category = "ongulé"
        self.subcategory = "marcassin"
        self.cost_card = 0
        """
        Couleurs : marron, rouge, orange
        """

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

class Daim(Ongulé):
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
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        return self

    def points(self):
        print(f"3pts per Ongulé.")
        return self


sang = Sanglier("rouge")
