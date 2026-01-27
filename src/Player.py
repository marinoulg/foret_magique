# from src.CountPoints import Plateau
# from src.helper_functions.game_functions import initialize_game_and_players
from src.helper_functions.colors import which_color
from random import randint

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

    def __init__(self, nb_cards=6, player_id=None):
        if player_id == None:
            self.player_id = randint(1,1000)
        else:
            self.player_id = player_id
        self.nb_cards = nb_cards
        self.puncts = 0
        self.cards_player = []
        self.who_start = 0

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

    def throw_card(self, card_idx):
        card = self.cards_player.pop(card_idx)
        # if a player wishes to throw a card in la clairière,
        return card

    def pickup_card_from_clairiere(self, Card):
        pass

    def print_cards(self, cat=False,
                    subcat=True,
                    color_leaf=True,
                    cost_card=False,
                    effect_attr = False):
        idx = 1
        for c in (self.cards_player):
            print(f"carte {idx}: ", end="")
            try:
                c_up = c.__dict__["up"]
                c_down = c.__dict__["down"]
                if cat==True:
                    print(c_up.category, end=" / ")
                    print(c_down.category, end = " - ")
                if subcat==True:
                    print(c_up.subcategory, end=" / ")
                    print(c_down.subcategory, end = " - ")
                if color_leaf==True:
                    print(c_up.couleur_feuille, end = " / ")
                    print(c_down.couleur_feuille, end = " - ")
                if cost_card==True:
                    print("cost_card: ", end="")
                    print(c_up.cost_card, end = " / ")
                    print(c_down.cost_card, end = " - ")
                # if effect_attr==True:
                #     print(c_up.effect_attr, end = " / ")
                #     print(c_down.effect_attr, end = " - ")

                else: next
            except KeyError:
                try:
                    if cat==True:
                        print(c.category, end=" - ")
                    if subcat==True:
                        print(c.subcategory, end=" - ")
                    if color_leaf==True:
                        print(c.couleur_feuille, end = " - ")
                    if cost_card==True:
                        print(c.cost_card, end = " - ")
                    else: next
                except AttributeError:
                    try:
                        c_left = c.__dict__["left"]
                        c_right = c.__dict__["right"]
                        if cat==True:
                            print(c_left.category, end=" / ")
                            print(c_right.category, end = " - ")
                        if subcat==True:
                            print(c_left.subcategory, end=" / ")
                            print(c_right.subcategory, end = " - ")
                        if color_leaf==True:
                            print(c_left.couleur_feuille, end = " / ")
                            print(c_right.couleur_feuille, end = " - ")
                        if cost_card==True:
                            print(c_left.cost_card, end = " / ")
                            print(c_right.cost_card, end = " - ")
                        else: next
                    except AttributeError:
                        next
            idx += 1
            print()

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
        self.cost_card = None

    def choose_color(self):
        return which_color()

class Card(ElementsAnimal):
    def __init__(self, up_down=False, left_right=False,
                 tree=False, left=None, right=None, up=None, down=None,
                 winter=False, grotte=False,
                #  cost_card=None
                 ):
        # super().__init__(cost_card)
        if up_down == True:
            self.up_down = up_down
            self.up = ElementsAnimal()
            self.down = ElementsAnimal()
        elif left_right == True:
            self.left_right = left_right
            self.left = ElementsAnimal()
            self.right = ElementsAnimal()
        elif tree == True:
            self.left = ElementsAnimal()
            self.right = ElementsAnimal()
            self.up = ElementsAnimal()
            self.down = ElementsAnimal()
        elif winter == True:
            self.winter_is_coming = 0
            # card_winter = Card(winter=True)
            # card_winter.winter_is_coming += 1
        elif grotte == True:
            self.grotte = []


class Clairiere:
    def __init__(self):
        self.cards_clairiere = list()

    def throw_card_in_clairiere(self, Player, card_idx_in_list):
        Card = Player.throw_card(card_idx_in_list)
        self.cards_clairiere.append(Card)
        return self

    def print_cards(self, cat=False,
                    subcat=True,
                    color_leaf=True,
                    cost_card=False,
                    effect_attr = False):
        idx = 1
        for c in (self.cards_clairiere):
            print(f"carte {idx}: ", end="")
            try:
                c_up = c.__dict__["up"]
                c_down = c.__dict__["down"]
                if cat==True:
                    print(c_up.category, end=" / ")
                    print(c_down.category, end = " - ")
                if subcat==True:
                    print(c_up.subcategory, end=" / ")
                    print(c_down.subcategory, end = " - ")
                if color_leaf==True:
                    print(c_up.couleur_feuille, end = " / ")
                    print(c_down.couleur_feuille, end = " - ")
                if cost_card==True:
                    print("cost_card: ", end="")
                    print(c_up.cost_card, end = " / ")
                    print(c_down.cost_card, end = " - ")
                # if effect_attr==True:
                #     print(c_up.effect_attr, end = " / ")
                #     print(c_down.effect_attr, end = " - ")

                else: next
            except KeyError:
                try:
                    if cat==True:
                        print(c.category, end=" - ")
                    if subcat==True:
                        print(c.subcategory, end=" - ")
                    if color_leaf==True:
                        print(c.couleur_feuille, end = " - ")
                    if cost_card==True:
                        print(c.cost_card, end = " - ")
                    else: next
                except AttributeError:
                    try:
                        c_left = c.__dict__["left"]
                        c_right = c.__dict__["right"]
                        if cat==True:
                            print(c_left.category, end=" / ")
                            print(c_right.category, end = " - ")
                        if subcat==True:
                            print(c_left.subcategory, end=" / ")
                            print(c_right.subcategory, end = " - ")
                        if color_leaf==True:
                            print(c_left.couleur_feuille, end = " / ")
                            print(c_right.couleur_feuille, end = " - ")
                        if cost_card==True:
                            print(c_left.cost_card, end = " / ")
                            print(c_right.cost_card, end = " - ")
                        else: next
                    except AttributeError:
                        next
            idx += 1
            print()
