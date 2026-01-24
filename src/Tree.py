from src.Player import *

class Tree:
    def __init__(self, left=None, right=None, up=None, down=None):
        # super().__init__()
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.category = "arbre"

class Chêne(Tree):
    def __init__(self, left=None, right=None, up=None, down=None):
        super().__init__(left, right, up, down)
        self.subcategory = "chêne"
        self.cost_card = 2
        self.effect_attr = None
        self.bonuss = None
        self.couleur = "marron"

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, card_throwed_2):
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """

        # if Player(player_id).throw_card(card_throwed_1) and card_throwed_1.couleur_feuille == "marron":
        #     if Player(player_id).throw_card(card_throwed_2) and card_throwed_2.couleur_feuille == "marron":
        #         self.bonuss = "Play again"
        return self

    def points(self, player_id):
        # if Bouleau().subcategory and Hêtre().subcategory and \
        #     Marronier().subcategory and Sapin_blanc().subcategory and \
        #     Sapin_Douglas().subcategory and Tilleul().subcategory and \
        #     Erable().subcategory and Chêne().subcategory \
        #             in Player(player_id).cards_player:
        #     Player(player_id).puncts += 10
        return self

class Bouleau(Tree):
    def __init__(self, left=None, right=None, up=None, down=None):
        super().__init__(left, right, up, down)
        self.subcategory = "bouleau"
        self.cost_card = 0
        # self.effect = Player().draw_cards(Card())
        self.bonuss = None
        self.couleur = "vert clair"

    def effet(self):
        print(f"{self.subcategory} allows you to draw a card.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        # Player(player_id).puncts += 1
        return self

class Hêtre(Tree):
    def __init__(self, left=None, right=None, up=None, down=None):
        super().__init__(left, right, up, down)
        self.subcategory = "hêtre"
        self.cost_card = 1
        # self.effect = Player().draw_cards(Card())
        self.bonuss = None
        self.couleur = "vert foncé"

    def effet(self):
        print(f"{self.subcategory} allows you to draw a card.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        # if Player(player_id).nb_hêtres() >= 4:
        #     Player(player_id).puncts += 5
        return self

class Marronier(Tree):
    def __init__(self, left=None, right=None, up=None, down=None):
        super().__init__(left, right, up, down)
        self.subcategory = "marronnier commun"
        self.cost_card = 1
        self.effect_attr = None
        self.bonuss = None
        self.couleur = "orange"

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        # if Player(player_id).nb_marronniers() == 1:
        #     Player(player_id).puncts += 1
        # elif Player(player_id).nb_marronniers() == 2:
        #     Player(player_id).puncts += 4
        # elif Player(player_id).nb_marronniers() == 3:
        #     Player(player_id).puncts += 9
        # elif Player(player_id).nb_marronniers() == 4:
        #     Player(player_id).puncts += 16
        # elif Player(player_id).nb_marronniers() == 5:
        #     Player(player_id).puncts += 25
        # elif Player(player_id).nb_marronniers() == 6:
        #     Player(player_id).puncts += 36
        # elif Player(player_id).nb_marronniers() >= 7:
        #     Player(player_id).puncts += 49
        return self

class SapinBlanc(Tree):
    def __init__(self, left=None, right=None, up=None, down=None):
        super().__init__(left, right, up, down)
        self.subcategory = "sapin Douglas"
        self.cost_card = 2
        self.effect_attr = None
        self.bonuss = None
        self.couleur = "bleu clair"

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self,  card_throwed_1, card_throwed_2):
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """

        # if Player(player_id).throw_card(card_throwed_1) and card_throwed_1.couleur_feuille == "bleu foncé":
            # if Player(player_id).throw_card(card_throwed_2) and card_throwed_2.couleur_feuille == "bleu foncé":
            #     self.bonuss = Player().place_card_in_clairiere(Card()) if Card().subcategory == "patte" else None
        return self

    def points(self):
        return self
    pass

class SapinDouglas(Tree):
    def __init__(self, left=None, right=None, up=None, down=None):
        super().__init__(left, right, up, down)
        self.subcategory = "tilleul"
        self.cost_card = 2
        self.effect_attr = None
        self.bonuss = None
        self.couleur = "bleu foncé"

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self, card_throwed_1, card_throwed_2):
        """
        to be reviewed
        card_throwed_1 = Card()
        card_throwed_2 = Card()
        """

        # if Player(player_id).throw_card(card_throwed_1) and card_throwed_1.couleur_feuille == "bleu clair":
        #     if Player(player_id).throw_card(card_throwed_2) and card_throwed_2.couleur_feuille == "bleu clair":
        #         self.bonuss = "Play again"
        return self


    def points(self, player_id):
        Player(player_id).puncts += 5
        return self

class Tilleul(Tree):
    def __init__(self, left=None, right=None, up=None, down=None):
        super().__init__(left, right, up, down)
        self.subcategory = "tilleul"
        self.cost_card = 1
        self.effect_attr = None
        self.bonuss = None
        self.couleur = "jaune"

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self,player_id):
        most_tilleuls_list = Player(player_id).who_most_tilleuls()
        if len(most_tilleuls_list) == 1:
            Player(player_id).puncts += 3
        else:
            pass
        # so that we don't do this everytime we get a tilleul

        return self

class Erable(Tree):
    def __init__(self, left=None, right=None, up=None, down=None):
        super().__init__(left, right, up, down)
        self.subcategory = "érable"
        self.cost_card = 2
        self.effect_attr = None
        self.bonuss = None
        self.couleur = "rouge"

    def effet(self):
        print(f"{self.subcategory} has no effect.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

    def points(self):
        # nb_arbres = Player(player_id).nb_hêtres() + Player(player_id).nb_marronniers() \
        #     + Player(player_id).nb_bouleau() + Player(player_id).nb_chênes() \
        #       + Player(player_id).nb_érables() + Player(player_id).nb_tilleuls() \
        #           + Player(player_id).nb_sapin_blanc() + Player(player_id).nb_sapin_douglas()
        # Player(player_id).puncts += nb_arbres
        return self
