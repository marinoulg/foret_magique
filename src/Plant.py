from src.Player import Player, ElementsAnimal, Plateau, Game
from src.Tree import *

class Plant(ElementsAnimal):
    def __init__(self, couleur_feuille, down="down"):
        super().__init__(down)
        self.couleur_feuille = couleur_feuille
        self.position = down
        self.category = "plant"


class FougèreArborescente(Plant):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.cost_card = 1
        self.subcategory = "fougère arborescente"
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
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
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
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
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
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "fraise des bois"
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
