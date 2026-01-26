from src.Player import Player, ElementsAnimal, Plateau, Game
from src.Tree import *
from src.helper_functions.colors import which_color

class Plant(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "plant"

class FougèreArborescente(Plant):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.cost_card = 1
        self.subcategory = "fougère_arborescente"
        """
        couleur_feuille peut être : jaune, bleu foncé, orange
        """

    def effet(self, new_card):
        print(f"{self.subcategory} allows you to draw a card.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        """
        6pts par lézard.
        """
        return self

class Mousse(Plant):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "mousse"
        self.cost_card = 0
        """
        couleur_feuille peut être : bleu clair, jaune
        """

    def effet(self, new_card):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        """
        10pts si vous avez au moins 10 arbres.
        """
        return self

class Mûre(Plant):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "mûre"
        self.cost_card = 0
        """
        couleur_feuille peut être : bleu foncé, vert foncé, vert clair
        """

    def effet(self, new_card):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        f"""
        2pts par {self.category}.
        """
        return self

class FraiseDesBois(Plant):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "fraise_des_bois"
        self.cost_card = 0
        """
        couleur_feuille peut être : vert clair, rouge
        """

    def effet(self, new_card):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        f"""
        10pts si vous avez chacune des 8 espèces d'Arbres différentes sur \
            votre Plateau.
        """
        return self
