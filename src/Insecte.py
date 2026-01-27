from src.Player import *
from src.Tree import *
from src.helper_functions.colors import which_color

class Insecte(ElementsAnimal):
    def __init__(self, couleur_feuille, position="left" or "right"):
        self.couleur_feuille = couleur_feuille
        self.position = position
        self.category = "insecte"

class FourmiRousse(Insecte):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "fourmi_rousse"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 1

    def effet(self, new_card):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        print(f"2pts par carte en-dessous d'un arbre.")
        return self

class Luciole(Insecte):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "luciole"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 0

    def effet(self, new_card):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        print(f"0pt si 1 {self.subcategory}; \n10pts si 2 {self.subcategory}s; \
              \n15pts si 3 {self.subcategory}s; \n20pt si 4 {self.subcategory}s.")
        return self

class Lucane(Insecte):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "lucane"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 2

    def effet(self, new_card):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} allows you to place 1 card in the Plateau if you pay the cost of \
            the card in cards whose color is {self.couleur_feuille}.")
        return self

    def points(self):
        print(f"1pt par Plantigrade.")
        return self

class Moustique(Insecte):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "moustique"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 0

    def effet(self, new_card):
        print(f"Vous pouvez jouer autant de Chauves-souris de votre main sans en payer le coût.")
        return self

    def bonus(self):
        print(f"{self.subcategory} allows you to place 1 card in the Plateau if you pay the cost of \
            the card in cards whose color is {self.couleur_feuille}.")
        return self

    def points(self):
        print(f"Chaque {self.subcategory} vaut 1pt par Chauve-souris sur votre Plateau.")
        return self

class XylocopeViolet(Insecte):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        self.subcategory = "xylocope_violet"
        if couleur_feuille == None:
            self.couleur_feuille = which_color(self.subcategory)
        self.cost_card = 1

    def effet(self, new_card):
        print(f"Ne vaut aucun point, mais augment de 1 le nombre d'Arbres de \
            l'espèce qu'il occupe.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        print(f"{self.subcategory} earns no point.")
        return self
