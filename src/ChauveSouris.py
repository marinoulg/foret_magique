from src.Player import Player, ElementsAnimal, Plateau, Game
from src.Tree import *
from src.helper_functions.colors import which_color

class ChauveSouris(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "chauve_souris"
        self.cost_card = 1

    def effet(self, new_card):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        f"""
        5pts si vous avez au mois 3 {self.subcategory}s.
        """
        return self

class MurinDeBechstein(ChauveSouris):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "murin_de_Bechstein"

class GrandRhinolophe(ChauveSouris):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "grand_rhinolophe"

class OreillardRoux(ChauveSouris):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "oreillard_roux"

class BarbastelleEurope(ChauveSouris):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "barbastelle_Europe"
