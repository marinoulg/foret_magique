from src.Player import Player, ElementsAnimal, Plateau, Game
from src.Tree import *

class ChauveSouris(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "chauve-souris"
        self.cost_card = 1
        if self.position not in ["left", "right"]:
            raise ValueError(f"Position of {self.subcategory} is not possible, please choose among 'left' or 'right'")

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
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "murin de Bechstein"
        """
        couleur_feuille peut être : marron, vert clair, vert foncé
        Position : left or right
        """

class GrandRhinolophe(ChauveSouris):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "grand rhinolophe"
        """
        couleur_feuille peut être : jaune
        Position : left or right
        """

class OreillardRoux(ChauveSouris):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "oreillard roux"
        """
        couleur_feuille peut être : rouge, vert foncé
        Position : left or right
        """

class BarbastelleEurope(ChauveSouris):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "barbastelle d'Europe"
        """
        couleur_feuille peut être : orange, marron, bleu foncé
        Position : left or right
        """
