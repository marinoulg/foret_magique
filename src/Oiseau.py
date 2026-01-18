from Player import Player, Card, Plateau, Game

class Oiseau(Card):
    def __init__(self, subcategory, couleur_feuille, player_id):
        super.__init__(subcategory, couleur_feuille, player_id)
        self.category = "champignon"

class Bouvreuil_pivoire(Oiseau):
    def __init__(self, category):
        super().__init__(category)
        self.subcategory = "bouvreuil pivoine"
        self.cost_card = 1
        """
        couleur_feuille peut être : bleu foncé, bleu clair
        """

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

class Pinson_des_arbres(Oiseau):
    def __init__(self, category, subcategory, couleur_feuille, player_id):
        super().__init__(category, subcategory, couleur_feuille, player_id)
        self.subcategory = "pinson des arbres"
        self.cost_card = 1
        """
        couleur_feuille peut être : rouge, vert foncé, vert clair
        """

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

class Geai_des_chênes(Oiseau):
    def __init__(self, category, subcategory, couleur_feuille, player_id):
        super().__init__(category, subcategory, couleur_feuille, player_id)
        self.subcategory = "geai des chênes"
        self.cost_card = 1
        """
        couleur_feuille peut être : orange, vert clair, rouge
        """

    def effet(self):
        print(f"{self.subcategory} allows you to play again.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self, player_id):
        Player(player_id).puncts += 3
        return self

class Autour_des_palombes(Oiseau):
    def __init__(self, category, subcategory, couleur_feuille, player_id):
        super().__init__(category, subcategory, couleur_feuille, player_id)
        self.subcategory = "autour des palombes"
        self.couleur_feuille = "bleu clair"
        """
        couleur_feuille peut être : bleu clair, marron
        """
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

class Pic_épeiche(Oiseau):
    def __init__(self, category, subcategory, couleur_feuille, player_id):
        super().__init__(category, subcategory, couleur_feuille, player_id)
        self.subcategory = "pic épeiche"
        self.cost_card = 2
        """
        couleur_feuille peut être : jaune, bleu clair
        """

    def effet(self, player_id):
        print(f"{self.subcategory} allows you to draw a card.")
        Player(player_id).draw_card()
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self, player_id):
        num_arbres = Plateau(player_id).how_many_per_species(player_id, subcategory="arbre")
        # if num_arbres est le max // tous les autres joueurs
        Player(player_id).puncts += 10
        return self
