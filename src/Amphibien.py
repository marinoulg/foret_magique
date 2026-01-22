from src.Player import Player, Card, Plateau, Game

class Amphibien(Card):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "amphibien"

class CrapaudCommun(Amphibien):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "crapaud commun"
        self.cost_card = 0
        possible_colors = ["vert foncé", "bleu foncé", "rouge", "marron", "orange", "bleu clair"]
        if self.couleur_feuille not in possible_colors:
            raise ValueError(f"Couleur of {self.subcategory} is not possible, please choose among {possible_colors}")
        """
        Couleurs : vert foncé, bleu foncé, rouge, marron, orange, bleu clair
        """

    def effet(self):
        print(f"Cet emplacement peut recevoir jusqu'à 2 {self.subcategory}s.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        """
        5pts si 2 crapauds partagent cet emplacement.
        """
        # Player(player_id).puncts += 1
        return self

class SalamandreTachetée(Amphibien):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "salamandre tachetée"
        self.cost_card = 1
        """
        couleur_feuille peut être : jaune, bleu clair, orange
        """

    def effet(self):
        print(f"Cet emplacement peut recevoir jusqu'à 2 {self.subcategory[0]}s.")
        return self

    def bonus(self, card_throwed_1):
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        print(f"{self.subcategory} allows you to freely place one card whose subcategory is 'PATTES'.")

        # if Player(player_id).throw_card(card_throwed_1) and card_throwed_1.couleur_feuille == "jaune":
        #     self.bonuss = Player().place_card_in_clairiere(Card()) if Card().subcategory == "patte" else None
        return self

    def points(self):
        """
        """
        # how_many = Plateau(player_id).how_many_per_species(self, player_id, subcategory = self.subcategory)
        # if how_many == 1:
        #    Player(player_id).puncts += 5
        # elif how_many == 2:
        #    Player(player_id).puncts += 15
        # elif how_many == 3:
        #    Player(player_id).puncts += 25
        return self

class RainetteVerte(Amphibien):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "rainette verte"
        self.cost_card = 0
        """
        couleur_feuille peut être : jaune, marron
        """

    def effet(self):
        print(f"Cet emplacement peut recevoir jusqu'à 2 {self.subcategory[0]}s.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """
        print(f"{self.subcategory} allows you to freely place one card whose subcategory is 'PATTES'.")

        # if Player(player_id).throw_card(card_throwed_1) and card_throwed_1.couleur_feuille == couleur_feuille:
        #     self.bonuss = Player().place_card_in_clairiere(Card()) if Card().subcategory == "patte" else None
        return self

    def points(self):
        """
        """
        # how_many_moustiques = Plateau(player_id).how_many_per_species(self, player_id, subcategory = "moustique")
        # Player(player_id).puncts += 5 * how_many_moustiques
        return self

class Cistude(Amphibien):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "cistude"
        self.cost_card = 2
        """
        couleur_feuille peut être : rouge, vert clair
        """

    def effet(self, player_id):
        print(f"{self.subcategory} allows you to draw one card form the deck.")
        Player(player_id).draw_card()
        return self

    def bonus(self):
        """
        """
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self, player_id):
        """
        """
        Player(player_id).puncts += 5
        return self
