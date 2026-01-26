from src.Player import Player, ElementsAnimal, Game
from src.helper_functions.colors import which_color

class Cervidé(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "cervidé"
