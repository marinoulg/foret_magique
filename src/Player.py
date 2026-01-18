from collections import defaultdict
from src.helper_functions.specific_functions import *
from src.Tree import *

class Player():
    def __init__(self, player_id, nb_cards=6):
        self.player_id = player_id
        self.nb_cards = nb_cards
        self.puncts = 0

        self.cards_player = []

        self.num_tilleuls = 0

    def can_pay_card(self):
        if self.enough_cards(self.cost_card):
            self.nb_cards -= self.cost_card
        return self

    def draw_card(self, card):
        # Card.subcategory = input("Sous-catégorie (chêne pour arbre etc.): ")
        # Card.cost_card = int(input("Cost card: "))
        # Card.category = input("Choose category among Tree (...): ") - automatic
        # Card().effect will be automatically attributed // category of card ?
        # Card().bonuss will be automatically attributed // category of card ?
        # Card.couleur_feuille = input("Couleur feuille: ")
        self.cards_player.append(card)
        return self

    def enough_cards(self, one_move):
        if self.nb_cards > one_move:
            self.nb_cards -= one_move
        return one_move

    def throw_card(self, Card):
        self.cards_player.remove(Card)
        return self


    def pickup_card_from_clairiere(self, Card):
        pass

    def place_card_in_clairiere(self, Card):
        pass

    def play_card_down(self, player_id, Which_tree, Card):
        """
        """
        Which_tree(player_id).down = Card
        return True

    def play_card_up(self, player_id, Which_tree, Card):
        """
        """
        Which_tree(player_id).up = Card
        return True


class Card():
    def __init__(self, player_id):
        # super().__init__(player_id)
        self.cost_card = 0
        self.category = [None] # attention it has changed
        self.subcategory = None
        self.effect = None
        self.bonuss = None
        self.couleur_feuille = None
        self.player_id = player_id


class Clairiere:
    def __init__(self):
        if Player.throw_card(Card):
            self.cards_clairiere = list()
            self.cards_clairiere.append(Card)


class Plateau(Player):
    def __init__(self, player_id):
        super().__init__(player_id)
        self.plateau_player = list()

    def place_tree(self):
        """
        answer is True or False
        """
        return True

    def poser_un_arbre(self, Card):
        temp_dict = {}
        if Card.category == "arbre":
            temp_dict[Card.subcategory] = {
                "up":Card.up,
                "down":Card.down,
                "left":Card.left,
                "right":Card.right
            }
            self.plateau_player.append(temp_dict)
        else:
            temp_dict["Pousse d'arbre"] = {
                "up":Card.up,
                "down":Card.down,
                "left":Card.left,
                "right":Card.right
            }
            self.plateau_player.append(temp_dict)
        return self

    def poser_une_carte(self, Card):
        pass

        # Specific to certain cards
    def nb_tilleuls(player_id, plateau_qqn_pt_arbre):
        return how_many_arbre_subcategory(player_id, plateau_qqn_pt_arbre, subcategory="tilleuls")
    def nb_hêtres(player_id, plateau_qqn_pt_arbre):
        return how_many_arbre_subcategory(player_id, plateau_qqn_pt_arbre, subcategory="hêtres")
    def nb_marronniers(player_id, plateau_qqn_pt_arbre):
        return how_many_arbre_subcategory(player_id, plateau_qqn_pt_arbre, subcategory="marronnier commun")
    def nb_érables(player_id, plateau_qqn_pt_arbre):
        return how_many_arbre_subcategory(player_id, plateau_qqn_pt_arbre, subcategory="marronnier commun")
    def nb_sapin_douglas(player_id, plateau_qqn_pt_arbre):
        return how_many_arbre_subcategory(player_id, plateau_qqn_pt_arbre, subcategory="marronnier commun")
    def nb_sapin_blanc(player_id, plateau_qqn_pt_arbre):
        return how_many_arbre_subcategory(player_id, plateau_qqn_pt_arbre, subcategory="marronnier commun")
    def nb_chênes(player_id, plateau_qqn_pt_arbre):
        return how_many_arbre_subcategory(player_id, plateau_qqn_pt_arbre, subcategory="marronnier commun")
    def nb_bouleau(player_id, plateau_qqn_pt_arbre):
        return how_many_arbre_subcategory(player_id, plateau_qqn_pt_arbre, subcategory="marronnier commun")

    def how_many_per_species(self, player_id, subcategory = "papillon"):
        """
        possible subcategories:
            - papillon
            - oiseau
        """
        return how_many_for_one_species(player_id, self.plateau_player, subcategory = subcategory)

class Game():
    def __init__(self, nb_of_players):
        self.nb_of_players = nb_of_players
