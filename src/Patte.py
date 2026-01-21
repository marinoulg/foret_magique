from src.Player import Player, Card, Plateau, Game

class Patte(Card):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = "patte"

class Hérisson(Patte):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "hérisson"
        # self.couleur_feuille = "orange"
        self.cost_card = 1
        """
        Couleurs : vert foncé, orange, marron
        """

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, couleur_feuille):
        print(f"{self.subcategory} allows you to draw one card if the card's couleur_feuille it costs you is orange.")
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """

        # if Player(player_id).throw_card(card_throwed_1) and card_throwed_1.couleur_feuille == couleur_feuille:
        #     self.bonuss = Player(player_id).draw_card()
        return self

    def points(self):
        # num_papillons = Plateau(player_id).how_many_per_species(player_id, subcategory="papillon")
        # Player(player_id).puncts += 2 * num_papillons
        return self
