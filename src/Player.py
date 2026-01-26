from collections import defaultdict
from pprint import pprint
from src.helper_functions.specific_functions import *
from src.Tree import *
from src.helper_functions.colors import which_color

class Plateau:
    def __init__(self, player_id):
        self.player_id = player_id
        self.plateau_player = list()

    def pprint(self, index=True):
        if index == True:
            for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                pprint({i:elem})
        else:
            for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                pprint(elem)

    def place_tree(self, Card):
        temp_dict = {}
        try:
            if Card.category == "arbre":
                temp_dict = {
                        "arbre":Card.subcategory,
                        "up":None,
                        "down":None,
                        "left":None,
                        "right":None
                    }
        except AttributeError:
            temp_dict = {
                "arbre":"Pousse d'arbre",
                "up":None,
                "down":None,
                "left":None,
                "right":None
            }
        self.plateau_player.append(temp_dict)

        return self

    def how_many_tree_subcat(self, tree, print_=False):
        print(self, end = "")
        return how_many_arbre_subcategory(self.plateau_player, tree, print_=print)

    def place_non_tree_card(self, Card, on_tree,
                            which_tree_idx = None,
                            up=False,
                            down=False,
                            left=False,
                            right=False,
                            print_=False):
        count = 0
        for elem in [up, down, left, right]:
            if elem == True:
                count += 1

        if count == 0:
            raise ValueError("You need to say where you want to place the card.")
        elif count > 1:
            raise ValueError(f"You can only place the card at 1 specific place, not {count}.")
        else:
            if self.how_many_tree_subcat(on_tree, print_) == 1:
                for elem in self.plateau_player:
                    if elem["arbre"] == on_tree:
                        if up == True:
                            elem["up"] = Card.up
                        elif down == True:
                            elem["up"] = Card.up
                        elif left == True:
                            elem["left"] = Card.left
                        elif right == True:
                            elem["right"] = Card.right
            else:
                count = 0
                for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                    if elem["arbre"] == on_tree:
                        if up == True and elem["up"] == None:
                            count += 1
                            print(f"{i}. {elem}")
                        if down == True and elem["down"] == None:
                            count += 1
                            print(f"{i}. {elem}")
                        if left == True and elem["left"] == None:
                            count += 1
                            print(f"{i}. {elem}")
                        if right == True and elem["right"] == None:
                            count += 1
                            print(f"{i}. {elem}")
                print()
                if count > 1 and which_tree_idx == None:
                    num = int(input("Choose the index of the tree on which you want to put your card, eg type in 1, 2 etc.: \n"))
                    for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                        print(i, type(i))
                        if elem["arbre"] == on_tree and i == num:
                            if up == True:
                                elem["up"] = Card.up
                            elif down == True:
                                elem["up"] = Card.up
                            elif left == True:
                                elem["left"] = Card.left
                            elif right == True:
                                elem["right"] = Card.right
                elif count > 1 and which_tree_idx:
                    for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                        if elem["arbre"] == on_tree and i == which_tree_idx:
                            if up == True:
                                elem["up"] = Card.up
                            elif down == True:
                                elem["up"] = Card.up
                            elif left == True:
                                elem["left"] = Card.left
                            elif right == True:
                                elem["right"] = Card.right
                else:
                    for elem in self.plateau_player:
                        if elem["arbre"] == on_tree:
                            if up == True:
                                elem["up"] = Card.up
                            elif down == True:
                                elem["up"] = Card.up
                            elif left == True:
                                elem["left"] = Card.left
                            elif right == True:
                                elem["right"] = Card.right

        return self

    def how_many_per_species(self, Card, subcategory,
                            up=False,
                            down=False,
                            left=False,
                            right=False):

        count = 0
        for elem in self.plateau_player:
            print(elem)
            if Card.up_down == True:
                C = elem["up"]
                try:
                    if C.subcategory == subcategory:
                        count += 1
                    elif C.subcategory == subcategory:
                        count += 1
                except AttributeError:
                    next
            elif Card.left_right == True:
                try:
                    if C.subcategory == subcategory:
                        count += 1
                    elif C.subcategory == subcategory:
                        count += 1
                except AttributeError:
                    next

        """
        possible subcategories: toutes mes sous-catégories d'animaux.
        """
        return count

class Player(Plateau):
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
        super().__init__(player_id)
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


class Game:
    def __init__(self, nb_of_players):
        self.nb_of_players = nb_of_players
