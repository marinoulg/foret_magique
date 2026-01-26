from collections import defaultdict
import sys
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

    def how_many_tree_subcat(self, tree="tilleul", print_=False):
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
                            elem["down"] = Card.down
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
            # print(elem)
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

            # print()
        return count

    def at_least_1_tree_per_subcategory(self):
        boul = self.how_many_tree_subcat("bouleau")
        ch = self.how_many_tree_subcat("chêne")
        ht = self.how_many_tree_subcat("hêtre")
        marr = self.how_many_tree_subcat("marronnier_commun")
        sbl = self.how_many_tree_subcat("sapin_blanc")
        spD = self.how_many_tree_subcat("sapin_Douglas")
        tll = self.how_many_tree_subcat("tilleul")
        er = self.how_many_tree_subcat("érable")

        if boul > 0 and ch > 0 and ht > 0 and marr > 0 and sbl > 0 and spD > 0 and tll > 0 and er > 0:
            return True
        else: return False

    def count_papillons(self):
        papillons_dict = {
            "grand_mars_changeant":0,
            "paon_du_jour":0,
            "morio":0,
            "grande_tortue":0,
            "tabac_Espagne":0
            }

        for elem in self.plateau_player:
            if elem["up"] != None:
                if elem["up"].category == "papillon":
                    papillons_dict[(elem["up"].subcategory)] += 1
        return papillons_dict

    def points_papillon(self, points):
        pap_dict = (self.count_papillons())
        how_many_difft = 0
        for k in pap_dict.keys():
            if pap_dict[k] > 0:
                how_many_difft += 1

        if how_many_difft == 1:
            points += 0
        elif how_many_difft == 2:
            points += 3
        elif how_many_difft == 3:
            points += 6
        elif how_many_difft == 4:
            points += 12
        elif how_many_difft == 5:
            points += 20

        return points

    def count_mosquitos(self):
        c = 0
        for elem in self.plateau_player:
            if elem["up"] != None:
                if elem["up"].subcategory == "moustique":
                    c += 1
        return c

    def count_luciole(self):
        c = 0
        for elem in self.plateau_player:
            if elem["down"] != None:
                print(elem["down"])
                if elem["down"].subcategory == "luciole":
                    c += 1
        return c

    def count_points_animal(self,
                    # Amphibien
                    crapaud_commun=False,
                    salamandre_tachetée=False,
                    rainette_verte=False,
                    cistude=False,

                    # CervidéOngulé
                    cerf_élaphe=False,
                    chevreuil=False,
                    daim=False,

                    # Champignon
                    amanite_tue_mouches=False,
                    coulemelle=False,
                    girolle=False,
                    cèpe_Bordeaux=False,

                    # ChauveSouris
                    murin_de_Bechstein=False,
                    grand_rhinolophe=False,
                    oreillard_roux=False,
                    barbastelle_Europe=False,

                    # Insecte
                    fourmi_rousse=False,
                    luciole=False,
                    lucane=False,
                    moustique=False,
                    xylocope_violet=False,

                    #  Oiseau
                    bouvreuil_pivoire=False,
                    pinson_des_arbres=False,
                    geai_des_chênes=False,
                    autour_des_palombes=False,
                    pic_epeiche=False,
                    chouette_hulotte=False,

                    # Ongulé
                    sanglier=False,
                    marcassin=False,

                    # Papillon
                    grand_mars_changeant=False,
                    paon_du_jour=False,
                    morio=False,
                    grande_tortue=False,
                    tabac_Espagne=False,

                    # Plant
                    fougère_arborescente=False,
                    mousse=False,
                    mûre=False,
                    fraise_des_bois=False,

                    # Plantigrade
                    hérisson=False,
                    lièvre_Europe=False,
                    fouine=False,
                    loup=False,
                    renard_roux=False,
                    taupe=False,
                    loir_gris=False,
                    écureuil_roux=False,
                    blaireau_européen=False,
                    lynx=False,
                    raton_laveur=False,
                    ours_brun=False,

                     points=0):

        for dict_ in self.plateau_player:
            for elem in list(dict_.values()):
                if elem != None:
                    # Amphibien
                    if crapaud_commun:
                        pass

                    elif rainette_verte:
                        if elem.subcategory == "rainette_verte":
                            c = self.count_mosquitos()
                            points += c*5



                    # Insecte
                    elif luciole:
                        luciole_counted = 0
                        if elem.subcategory == "luciole":
                            c = self.count_luciole()
                            if c == 1 and luciole_counted == 0:
                                points += 0
                                luciole_counted += 1
                                return points
                            elif c == 2 and luciole_counted == 0:
                                points += 10
                                luciole_counted += 1
                                return points
                            elif c == 3 and luciole_counted == 0:
                                points += 15
                                luciole_counted += 1
                                return points
                            elif c == 5 and luciole_counted == 0:
                                points += 20
                                luciole_counted += 1
                                return points

                    # Oiseau
                    elif autour_des_palombes:
                        palom = Card(up_down=True)
                        palom.up = AutourDesPalombes()
                        try:
                            if elem.subcategory == "autour_des_palombes":
                                c = self.how_many_per_category(palom,
                                                        palom.up.category,
                                                        up=True)
                                points += (3*c)
                        except AttributeError:
                            next

                    elif chouette_hulotte:
                        if elem.subcategory == "chouette_hulotte":
                            points += 5



                    # Papillon
                    elif grand_mars_changeant or paon_du_jour or morio or grande_tortue or tabac_Espagne:
                        counting_papillons = 0
                        if elem.subcategory == "grand_mars_changeant" and counting_papillons==0 and grand_mars_changeant:
                            points += self.points_papillon(points)
                            print(points, counting_papillons)
                            break
                        elif elem.subcategory =="paon_du_jour" and counting_papillons==0 and paon_du_jour:
                            points += self.points_papillon(points)
                            counting_papillons += 1
                            break
                        elif elem.subcategory =="morio" and counting_papillons==0 and morio:
                            print(points, counting_papillons)
                            points += self.points_papillon(points)
                            counting_papillons += 1
                            break
                        elif elem.subcategory =="grande_tortue" and counting_papillons==0 and grande_tortue:
                            print(points, counting_papillons)
                            points += self.points_papillon(points)
                            counting_papillons += 1
                            break
                        elif elem.subcategory =="tabac_Espagne" and counting_papillons==0 and tabac_Espagne:
                            print(points, counting_papillons)
                            points += self.points_papillon(points)
                            counting_papillons += 1
                            break

                    # Plant
                    elif mousse:
                        if elem.subcategory == "mousse":
                            chene = Chêne()
                            total = self.how_many_per_category(chene, chene.category)

                            if total > 9:
                                points += 10

                    elif fraise_des_bois:
                        if elem.subcategory == "fraise_des_bois":
                            if self.at_least_1_tree_per_subcategory():
                                points += 10


        return points
