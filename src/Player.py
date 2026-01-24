from collections import defaultdict
from src.helper_functions.specific_functions import *
from src.Tree import *
from src.colors import which_color

class Player:
    """
    This class defines the characteristics of a Player.
    Each player has:
        - a player_id (for the database)
        - a certain number of cards at each precise moment in time
        - a total number of points at each moment in time


    This class also defines the actions of a Player:
        - enough_cards: if a player has enough cards to pay the cost of a card
        - draw_card: what happens if a player draws a card --> which gets added
        to their cards
     ** - can_pay_card: if a player has enough_cards, they pay to place a card
        in their Plateau, and they have less cards in their hand as a result.
     ** - throw_card: if a player wishes to throw a card in la clairière, they
        have one less card in their hand as a result.
     ** - pickup_card_from_clairiere: if a player wants to pick up a card from
        la clarière, this card then gets added to their hand, and removed
        from la clairière


    """


    def __init__(self, player_id, nb_cards=6):
        self.player_id = player_id
        self.nb_cards = nb_cards
        self.puncts = 0
        self.cards_player = []

        self.num_tilleuls = 0 # not sure -- more so in the Plateau?

    def can_pay_card(self):
        if self.enough_cards(self.cost_card):
            self.nb_cards -= self.cost_card
            # Player pays to place a card in their Plateau,
            # and they have less cards in their hand as a result.
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

    def throw_card_in_clairiere(self, Card):
        self.cards_player.remove(Card)
        # if a player wishes to throw a card in la clairière,
        return self

    def pickup_card_from_clairiere(self, Card):
        pass

    # def play_card_down(self, player_id, Which_tree, Card):
    #     """
    #     """
    #     Which_tree(player_id).down = Card
    #     return True

    # def play_card_up(self, player_id, Which_tree, Card):
    #     """
    #     """
    #     Which_tree(player_id).up = Card
    #     return True

class ElementsAnimal:
    """
    Is it important to know who a card belongs to?
    """

    def __init__(self):
        self.cost_card = 0
        self.category = [None] # attention it has changed
        self.subcategory = None
        self.effect_attr = None
        self.bonuss = None
        self.couleur_feuille = None
        self.position = None

    def choose_color(self):
        return which_color()

class Card:
    def __init__(self, up_down=False, left_right=False):
        self.up_down = up_down
        self.left_right = left_right
        if up_down == True:
            self.up = ElementsAnimal()
            self.down = ElementsAnimal()
        else:
            self.left = ElementsAnimal()
            self.right = ElementsAnimal()

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

    def poser_une_carte(self, Card, on_tree):

        pass

    def how_many_tree_subcat(self, tree):
        # print(Player, end = "")
        return how_many_arbre_subcategory(self.plateau_player, tree)

    def how_many_per_species(self, player_id, subcategory = "papillon"):
        """
        possible subcategories:
            - papillon
            - oiseau
        """
        return how_many_for_one_species(player_id, self.plateau_player, subcategory = subcategory)

class Game:
    def __init__(self, nb_of_players):
        self.nb_of_players = nb_of_players
