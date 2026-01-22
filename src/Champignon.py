from src.Player import Player, Card, Plateau, Game
from src.Tree import *

class Champignon(Card):
    def __init__(self, couleur_feuille, down="down"):
        super().__init__(down)
        self.couleur_feuille = couleur_feuille
        self.position = down
        self.category = "champignon"
        self.cost_card = 2

class Amanite(Champignon):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "amanite tue-mouches"
        """
        couleur_feuille peut être : marron, bleu foncé
        """

    def effet(self, new_card):
        print(f"{self.subcategory} allows you to draw a card chaque fois que vous jouez une carte 'PATTE'.")
        # if new_card.subcategory == "patte":
            # Player(player_id).draw_card()
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class Coulemelle(Champignon):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "coulemelle"
        self.couleur_feuille = "orange"
        """
        couleur_feuille peut être : orange, bleu foncé
        """

    def effet(self, new_card):
        print(f"Chaque fois que vous jouez une carte en dessous d'un Arbre, piochez une carte.")
        # if Player(player_id).play_card_down():
        #     Player(player_id).draw_card()
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class Girolle(Champignon):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "girolle"
        """
        couleur_feuille peut être : bleu foncé, vert clair
        """

    def effet(self):
        print(f"Chaque fois que vous jouez une carte présentant un Arbre, piochez une carte.")
        # if Plateau(player_id).place_tree():
        #     Player(player_id).draw_card()
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class CèpeDeBordeaux(Champignon):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "girolle"
        """
        couleur_feuille peut être : bleu clair
        """

    def effet(self):
        print(f"Chaque fois que vous jouez une carte au dessus d'un Arbre, piochez une carte.")

        # if Player(player_id).play_card_up(player_id):
        #     Player(player_id).draw_card()
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self
