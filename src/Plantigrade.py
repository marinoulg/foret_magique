from src.Player import Player, ElementsAnimal, Plateau, Game
from src.helper_functions.colors import which_color

class Plantigrade(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "plantigrade"

class Hérisson(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "hérisson"
        self.cost_card = 1

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        print(f"{self.subcategory} allows you to draw one card if the card's couleur_feuille it costs you is orange.")
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        return self

    def points(self):
        return self

class LièvreEurope(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "lièvre_Europe"
        self.cost_card = 0

    def effet(self):
        print(f"cet emplacement peut recevoir un nombre illimité de {self.subcategory.capitalize()}s.")
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
        print(f"1pt par {self.subcategory}")
        return self

class Fouine(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "fouine"
        self.cost_card = 1

    def effet(self):
        print(f"{self.subcategory} allows you to draw one card.")
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
        print(f"5pts par arbre entièrement occupé.")
        return self

class Loup(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "loup"
        self.cost_card = 3

    def effet(self):
        print(f"{self.subcategory} allows you to draw one card per Cervidé.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        print(f"{self.subcategory} allows you to play again if all {self.cost_card} cards \
            it costs you are of the same color as {self.couleur_feuille}.")
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """

        return self

    def points(self):
        print(f"5pts par Cervidé.")
        return self

class RenardRoux(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "renard_roux"
        self.cost_card = 2

    def effet(self):
        print(f"{self.subcategory} allows you to draw one card per Lièvre d'Europe.")
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
        print(f"2pts par Lièvre d'Europe.")
        return self

class Taupe(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "taupe"
        self.cost_card = 2

    def effet(self):
        print(f"Jouez immédiatement autant de cartes que souhaité en payant leurs coûts.")
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
        print(f"{self.subcategory} earns no points.")
        return self

class LoirGris(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "loir_gris"
        self.cost_card = 1

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
        print(f"15pts s'il y a aussi une {self.subcategory} sur cet Arbre.")
        return self

class EcureuilRoux(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "écureuil_roux"
        self.cost_card = 0

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
        print(f"5pts si rattaché à un Chêne.")
        return self

class BlaireauEuropéen(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "blaireau_européen"
        self.cost_card = 1

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        print(f"{self.subcategory} allows you to place in the Plateau 1 {self.category} card if the cost of \
            this card is payed with cards whose color is {self.couleur_feuille}.")
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        return self

    def points(self):
        print(f"2pts.")
        return self

class Lynx(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "lynx"
        self.cost_card = 1

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
        print(f"10pts si vous avez au moins 1 Chevreuil.")
        return self

class RatonLaveur(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "raton_laveur"
        self.cost_card = 1

    def effet(self):
        print(f"Placez autant de cartes de votre main que vous souhaitez dans votre Grotte, \
            puis piochez le même nombre de cartes du paquet.")
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
        print(f"1pt par {self.subcategory}")
        return self

class OursBrun(Plantigrade):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "ours_brun"
        self.cost_card = 3

    def effet(self):
        print(f"Placez toutes les cartes de la Clairière dans votre Grotte.")
        return self

    def bonus(self, card_throwed_1):
        print(f"{self.subcategory} allows you to draw one card AND play again if you payed \
            the cost of the cards using cards whose color is {self.couleur_feuille}.")
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        return self

    def points(self):
        print(f"1pt par {self.subcategory}")
        return self
