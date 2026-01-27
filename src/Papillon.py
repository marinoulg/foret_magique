from src.Player import *
from src.helper_functions.colors import which_color

class Papillon(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "papillon"

    def points(self):
        # how_many = Plateau().how_many_per_species(self, subcategory = self.subcategory[0])
        # if how_many == 1:
        #    Player(player_id).puncts += 0
        # elif how_many == 2:
        #    Player(player_id).puncts += 3
        # elif how_many == 3:
        #    Player(player_id).puncts += 6
        # elif how_many == 4:
        #    Player(player_id).puncts += 12
        # elif how_many == 5:
        #    Player(player_id).puncts += 20
        return self

class GrandMarsChangeant(Papillon):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "grand_mars_changeant"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 0

    def effet(self):
        print(f"{self.subcategory} allows you to draw a card.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class PaonDuJour(Papillon):
    def __init__(self,  couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "paon_du_jour"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 0

    def effet(self):
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class Morio(Papillon):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "morio"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 0

    def effet(self):
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class GrandeTortue(Papillon):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "grande_tortue"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 0

    def effet(self):
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class TabacEspagne(Papillon):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "tabac_Espagne"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 0

    def effet(self):
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self
