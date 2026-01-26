from collections import defaultdict
from pprint import pprint
from src.helper_functions.specific_functions import *
from src.helper_functions.colors import which_color

from src.Tree import *
from src.Champignon import *
from src.Oiseau import *
from src.Plantigrade import *
from src.Papillon import *
from src.Amphibien import *
from src.Insecte import *
from src.Cervidé import *
from src.Ongulé import *
from src.CervidéOngulé import *
from src.Plant import *
from src.ChauveSouris import *




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
                        "arbre":Card,
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
        if print_: print("Player", self.player_id, end = "")
        return how_many_arbre_subcategory(self.plateau_player, tree, print_=print_)

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
                    if elem["arbre"].subcategory == on_tree:
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
                    if elem["arbre"].subcategory == on_tree:
                        if up == True and elem["up"] == None:
                            count += 1
                            if print_ == True:
                                print(f"{i}. {elem}")
                        if down == True and elem["down"] == None:
                            count += 1
                            if print_ == True:
                                print(f"{i}. {elem}")
                        if left == True and elem["left"] == None:
                            count += 1
                            if print_ == True:
                                print(f"{i}. {elem}")
                        if right == True and elem["right"] == None:
                            count += 1
                            if print_ == True:
                                print(f"{i}. {elem}")

                if print_ == True: print()

                if count > 1 and which_tree_idx == None:
                    num = int(input("Choose the index of the tree on which you want to put your card, eg type in 1, 2 etc.: \n"))
                    for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):

                        if elem["arbre"].subcategory == on_tree and i == num:
                            if up == True:
                                elem["up"] = Card.up
                            elif down == True:
                                elem["down"] = Card.down
                            elif left == True:
                                elem["left"] = Card.left
                            elif right == True:
                                elem["right"] = Card.right
                elif count > 1 and which_tree_idx:
                    for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                        if elem["arbre"].subcategory == on_tree and i == which_tree_idx:
                            if up == True:
                                elem["up"] = Card.up
                            elif down == True:
                                elem["down"] = Card.down
                            elif left == True:
                                elem["left"] = Card.left
                            elif right == True:
                                elem["right"] = Card.right
                else:
                    for elem in self.plateau_player:
                        if elem["arbre"].subcategory == on_tree:
                            if up == True:
                                elem["up"] = Card.up
                            elif down == True:
                                elem["down"] = Card.down
                            elif left == True:
                                elem["left"] = Card.left
                            elif right == True:
                                elem["right"] = Card.right

        return self

    def how_many_per_subcategory(self, Card, subcategory,
                            up=False,
                            down=False,
                            left=False,
                            right=False):

        count = 0
        for i, elem in zip(range(len(self.plateau_player)), self.plateau_player):
            try:
                if Card.up_down == True:
                    if up == True:
                        C = elem["up"]
                        try:
                            if C.subcategory == subcategory:
                                count += 1
                        except AttributeError:
                            next
                    else:
                        C = elem["down"]
                        try:

                            if C.subcategory == subcategory:
                                print(i, elem)
                                count += 1
                        except AttributeError:
                            next
            except AttributeError:
            # elif Card.left_right == True:
                if left == True:
                    C = elem["left"]
                    try:
                        if C.subcategory == subcategory:
                            count += 1
                    except AttributeError:
                        next
                else:
                    C = elem["right"]
                    try:
                        if C.subcategory == subcategory:
                            count += 1
                    except AttributeError:
                        next

        """
        possible subcategories: toutes mes sous-catégories d'animaux.
        """
        return count

    def how_many_per_category(self, Card, category,
                            up=False,
                            down=False,
                            left=False,
                            right=False):
        count = 0
        for elem in self.plateau_player:
            print(elem)
            try:
                if Card.up_down == True:
                    if up == True:
                        C = elem["up"]

                        try:
                            if C.category == category:
                                count += 1
                        except AttributeError:
                            next
                    elif down == True:
                        C = elem["down"]
                        try:
                            if C.category == category:
                                count += 1
                        except AttributeError:
                            next
            except AttributeError:
                try:
                    if Card.left_right == True:
                        if left == True:
                            C = elem["left"]
                            try:
                                if C.category == category:
                                    count += 1
                            except AttributeError:
                                next
                        elif right == True:
                            C = elem["right"]
                            try:
                                if C.category == category:
                                    count += 1
                            except AttributeError:
                                next
                except AttributeError:
                    C = elem["arbre"]
                    try:
                        if C.category == category:
                            count += 1
                    except AttributeError:
                        next

            print()
        return count

    def count_points_animal(self,
                     autour_des_palombes=False,
                     mousse=False,
                     points=0):

        for elem in self.plateau_player:
            for animal in list(elem.values()):
                if autour_des_palombes == True:
                    palom = Card(up_down=True)
                    palom.up = AutourDesPalombes()
                    try:
                        if animal.subcategory == "autour_des_palombes":
                            c = self.how_many_per_category(palom,
                                                    palom.up.category,
                                                    up=True)
                            # print(c)
                            points += (3*c)

                            break
                    except AttributeError:
                        next

                elif mousse == True:
                    chene = Chêne()
                    total = self.how_many_per_category(chene, chene.category)

                    if total > 9:
                        points += 10
                        break

        # points += (3*c) # pour autour_des_palombes == True

        return points
