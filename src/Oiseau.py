from src.Player import Player, ElementsAnimal, Plateau, Game
from src.helper_functions.colors import which_color

class Oiseau(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.category = "oiseau"
        self.couleur_feuille = couleur_feuille

class BouvreuilPivoire(Oiseau):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.cost_card = 1

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self, player_id):
        subcategory = "oiseau"
        nb_insectes = Plateau(player_id).how_many_for_one_species(player_id, Plateau(player_id).plateau_player, subcategory = subcategory)
        total_points = 2 * nb_insectes
        Player().puncts += total_points
        return self

class PinsonDesArbres(Oiseau):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "pinson des arbres"
        self.cost_card = 1

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self, player_id):
        """
        5pts si rattaché à un hêtre.
        """
        return self

class GeaiDesChênes(Oiseau):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "geai_des_chênes"
        self.cost_card = 1

    def effet(self):
        print(f"{self.subcategory} allows you to play again.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self, player_id):
        Player(player_id).puncts += 3
        return self

class AutourDesPalombes(Oiseau):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "autour_des_palombes"
        self.couleur_feuille = "bleu clair"
        self.cost_card = 2

    def effet(self):
        print(f"{self.subcategory} allows you to play again.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self, player_id):
        num_oiseaux = Plateau(player_id).how_many_per_species(player_id, subcategory="oiseau")
        Player(player_id).puncts += 3 * num_oiseaux
        return self

class PicEpeiche(Oiseau):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "pic_epeiche"
        self.cost_card = 2
        """
        couleur_feuille peut être : jaune, bleu clair
        """

    def effet(self):
        print(f"{self.subcategory} allows you to draw a card.")
        # Player(player_id).draw_card()
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        # num_arbres = Plateau(player_id).how_many_per_species(player_id, subcategory="arbre")
        # if num_arbres est le max // tous les autres joueurs
        # Player(player_id).puncts += 10
        return self

class ChouetteHulotte(Oiseau):
    def __init__(self, couleur_feuille=None):
        super().__init__(couleur_feuille)
        if couleur_feuille == None:
            couleur_feuille = which_color(self.subcategory)
        self.subcategory = "chouette_hulotte"
        self.cost_card = 2
        """
        couleur_feuille peut être : vert clair, rouge, vert foncé
        """

    def effet(self, player_id):
        print(f"{self.subcategory} allows you to draw a card.")
        Player(player_id).draw_card()
        return self

    def bonus(self):
        print(f"{self.subcategory} allows you to draw 2 card if you pay with {self.cost_card} whose color are {self.couleur_feuille}.")
        return self

    def points(self):
        print(f"5pts.")
        # num_arbres = Plateau(player_id).how_many_per_species(player_id, subcategory="arbre")
        # if num_arbres est le max // tous les autres joueurs
        # Player(player_id).puncts += 10
        return self
