import os
import streamlit as st

from pprint import pprint
from src.helper_functions.specific_functions import *
# from src.helper_functions.game_functions import *
from src.Game import *
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

all_categories = {
                # Amphibien
                "crapaud_commun":CrapaudCommun("rouge"),
                "salamandre_tachetée":SalamandreTachetée("jaune"),
                "rainette_verte":RainetteVerte("jaune"),
                "cistude":Cistude("rouge"),

                # CervidéOngulé
                "cerf_élaphe":CerfElaphe("orange"),
                "chevreuil":Chevreuil("jaune"),
                "daim":Daim("jaune"),

                # Champignon
                "amanite_tue_mouches":Amanite("marron"),
                "coulemelle":Coulemelle("orange"),
                "girolle":Girolle("bleu foncé"),
                "cèpe_Bordeaux":CèpeDeBordeaux("bleu clair"),

                # ChauveSouris
                "murin_de_Bechstein":MurinDeBechstein("marron"),
                "grand_rhinolophe":GrandRhinolophe("jaune"),
                "oreillard_roux":OreillardRoux("rouge"),
                "barbastelle_Europe":BarbastelleEurope("orange"),

                # Insecte
                "fourmi_rousse":FourmiRousse("vert foncé"),
                "luciole":Luciole("jaune"),
                "lucane":Lucane("rouge"),
                "moustique":Moustique("orange"),
                "xylocope_violet":XylocopeViolet("bleu clair"),

                #  Oiseau
                "bouvreuil_pivoire":BouvreuilPivoire("bleu foncé"),
                "pinson_des_arbres":PinsonDesArbres("rouge"),
                "geai_des_chênes":GeaiDesChênes("rouge"),
                "autour_des_palombes":AutourDesPalombes("bleu clair"),
                "pic_epeiche":PicEpeiche("jaune"),
                "chouette_hulotte":ChouetteHulotte("rouge"),

                # Ongulé
                "sanglier":Sanglier("rouge"),
                "marcassin":Marcassin("rouge"),

                # Papillon
                "grand_mars_changeant":GrandMarsChangeant("jaune"),
                "paon_du_jour":PaonDuJour("jaune"),
                "morio":Morio("rouge"),
                "grande_tortue":GrandeTortue("rouge"),
                "tabac_Espagne":TabacEspagne("marron"),

                # Plant
                "fougère_arborescente":FougèreArborescente("jaune"),
                "mousse":Mousse("jaune"),
                "mûre":Mûre("bleu foncé"),
                "fraise_des_bois":FraiseDesBois("rouge"),

                # Plantigrade
                "hérisson":Hérisson("orange"),
                "lièvre_Europe":LièvreEurope("marron"),
                "fouine":Fouine("rouge"),
                "loup":Loup("rouge"),
                "renard_roux":RenardRoux("jaune"),
                "taupe":Taupe("rouge"),
                "loir_gris":LoirGris("marron"),
                "écureuil_roux":EcureuilRoux("orange"),
                "blaireau_européen":BlaireauEuropéen("orange"),
                "lynx":Lynx("jaune"),
                "raton_laveur":RatonLaveur("vert clair"),
                "ours_brun":OursBrun("jaune"),

                # Tree
                "chêne":Chêne(),
                "bouleau":Bouleau(),
                "hêtre":Hêtre(),
                "marronnier_commun":Marronnier(),
                "sapin_blanc":SapinBlanc(),
                "sapin_Douglas":SapinDouglas(),
                "tilleul":Tilleul(),
                "érable":Erable()
            }

all_trees = {
                "bouleau":Bouleau(),
                "chêne":Chêne(),
                "hêtre":Hêtre(),
                "marronnier_commun":Marronnier(),
                "sapin_blanc":SapinBlanc(),
                "sapin_Douglas":SapinDouglas(),
                "tilleul":Tilleul(),
                "érable":Erable()
                }

can_place_multiple_cards_same_spot = [
    "lièvre_Europe",
    "crapaud_commun",
]

class Plateau:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.plateau_player = list()
        self.name = name

    def pprint(self, index=False, only_animals=False, subcategory=True, category=False):
        if only_animals == False and category ==False and subcategory == False:
            if index == True:
                for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                    pprint({i:elem})
            elif index == False:
                for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                    pprint(elem)
        elif only_animals==True and category ==False and subcategory == True:
            if index==True:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        print(f"{i}:", an["arbre"].subcategory, end=": ")
                    if an["up"] != None:
                        for element_card in an["up"]:
                            print(element_card.subcategory, end=", ")
                    if an["down"] != None:
                        for element_card in an["down"]:
                            print(element_card.subcategory, end=", ")
                    if an["left"] != None:
                        for element_card in an["left"]:
                            print(element_card.subcategory, end=", ")
                    if an["right"] != None:
                        for element_card in an["right"]:
                            print(element_card.subcategory, end=", ")
                    print(end="\n")

            if index==False:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        print(an["arbre"].subcategory, end=": ")
                    if an["up"] != None:
                        print(an["up"].subcategory, end=", ")
                    if an["down"] != None:
                        print(an["down"].subcategory, end=", ")
                    if an["left"] != None:
                        print(an["left"].subcategory, end=", ")
                    if an["right"] != None:
                        print(an["right"].subcategory, end=", ")
                    print(end="\n")
        elif only_animals==True and category ==True and subcategory == False:
            if index==True:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"]!= None:
                        print(f"{i}:", an["arbre"].category, end=": ")
                    if an["up"] != None:
                        print(an["up"][0].category, end=", ")
                    if an["down"] != None:
                        print(an["down"][0].category, end=", ")
                    if an["left"] != None:
                        print(an["left"][0].category, end=", ")
                    if an["right"] != None:
                        print(an["right"][0].category, end=", ")
                    print(end="\n")

            if index==False:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        print(an["arbre"].category, end=": ")
                    if an["up"] != None:
                        print(an["up"][0].category, end=", ")
                    if an["down"] != None:
                        print(an["down"][0].category, end=", ")
                    if an["left"] != None:
                        print(an["left"][0].category, end=", ")
                    if an["right"] != None:
                        print(an["right"][0].category, end=", ")
                    print(end="\n")
        elif only_animals==True and category ==True and subcategory == True:
            if index==True:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        print(f"{i}: {an["arbre"].subcategory} - {an["arbre"].category}", end=": ")
                    if an["up"] != None:
                        print(f"{an["up"][0].subcategory} - {an["up"][0].category}", end=", ")
                    if an["down"] != None:
                        print(f"{an["down"][0].subcategory} - {an["down"][0].category}", end=", ")
                    if an["left"] != None:
                        print(f"{an["left"][0].subcategory} - {an["left"][0].category}", end=", ")
                    if an["right"] != None:
                        print(f"{an["right"][0].subcategory} - {an["right"][0].category}", end=", ")
                    print(end="\n")

            if index==False:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        print(an["arbre"].category, end=": ")
                    if an["up"] != None:
                        print(an["up"][0].category, end=", ")
                    if an["down"] != None:
                        print(an["down"][0].category, end=", ")
                    if an["left"] != None:
                        print(an["left"][0].category, end=", ")
                    if an["right"] != None:
                        print(an["right"][0].category, end=", ")
                    print(end="\n")
        # elif only_animals==False and subcategory==True and category==False:
        #     pass

    def st_write(self, index=False, only_animals=False, subcategory=True, category=False):


        if only_animals == False and category ==False and subcategory == False:
            if index == True:
                for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                    st.write({i:elem})
            elif index == False:
                for i, elem in zip(range(len(self.plateau_player)),self.plateau_player):
                    st.write(elem)
        elif only_animals==True and category ==False and subcategory == True:
            if index==True:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        st.write(f"{i}:", an["arbre"].subcategory, )
                    if an["up"] != None:
                        for element_card in an["up"]:
                            st.write(element_card.subcategory, )
                    if an["down"] != None:
                        for element_card in an["down"]:
                            st.write(element_card.subcategory, )
                    if an["left"] != None:
                        for element_card in an["left"]:
                            st.write(element_card.subcategory, )
                    if an["right"] != None:
                        for element_card in an["right"]:
                            st.write(element_card.subcategory, )
                    st.write()

            if index==False:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        st.write(an["arbre"].subcategory, )
                    if an["up"] != None:
                        st.write(an["up"].subcategory, )
                    if an["down"] != None:
                        st.write(an["down"].subcategory, )
                    if an["left"] != None:
                        st.write(an["left"].subcategory, )
                    if an["right"] != None:
                        st.write(an["right"].subcategory, )
                    st.write()
        elif only_animals==True and category ==True and subcategory == False:
            if index==True:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"]!= None:
                        st.write(f"{i}:", an["arbre"].category, )
                    if an["up"] != None:
                        st.write(an["up"][0].category, )
                    if an["down"] != None:
                        st.write(an["down"][0].category, )
                    if an["left"] != None:
                        st.write(an["left"][0].category, )
                    if an["right"] != None:
                        st.write(an["right"][0].category, )
                    st.write()

            if index==False:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        st.write(an["arbre"].category, )
                    if an["up"] != None:
                        st.write(an["up"][0].category, )
                    if an["down"] != None:
                        st.write(an["down"][0].category, )
                    if an["left"] != None:
                        st.write(an["left"][0].category, )
                    if an["right"] != None:
                        st.write(an["right"][0].category, )
                    st.write()
        elif only_animals==True and category ==True and subcategory == True:
            if index==True:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        st.write(f"{i}: {an["arbre"].subcategory} - {an["arbre"].category}", )
                    if an["up"] != None:
                        st.write(f"{an["up"][0].subcategory} - {an["up"][0].category}", )
                    if an["down"] != None:
                        st.write(f"{an["down"][0].subcategory} - {an["down"][0].category}", )
                    if an["left"] != None:
                        st.write(f"{an["left"][0].subcategory} - {an["left"][0].category}", )
                    if an["right"] != None:
                        st.write(f"{an["right"][0].subcategory} - {an["right"][0].category}", )
                    st.write()

            if index==False:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        st.write(an["arbre"].category, )
                    if an["up"] != None:
                        st.write(an["up"][0].category, )
                    if an["down"] != None:
                        st.write(an["down"][0].category, )
                    if an["left"] != None:
                        st.write(an["left"][0].category, )
                    if an["right"] != None:
                        st.write(an["right"][0].category, )
                    st.write()
        # elif only_animals==False and subcategory==True and category==False:
        #     pass

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

    def place_non_tree_card(self,
                        Card,
                        on_tree,
                        which_tree_idx=None,
                        up=False,
                        down=False,
                        left=False,
                        right=False,
                        print_=False):

        # Check direction
        directions = [up, down, left, right]
        if sum(directions) != 1:
            raise ValueError(f"You can only place the card at 1 specific place, not {directions}.")

        if directions == 0:
            raise ValueError("You need to say where you want to place the card.")

        # Find all trees of the specified subcategory
        matching_trees = [
            (i, elem) for i, elem in enumerate(self.plateau_player)
            if elem["arbre"].subcategory == on_tree
        ]

        if not matching_trees:
            raise ValueError(f"No tree of subcategory '{on_tree}' found.")

        # Determine which tree to use
        if which_tree_idx is not None:
            # Use the provided index
            tree_index, tree = next(
                ((i, elem) for i, elem in matching_trees if i == which_tree_idx),
                (None, None)
            )
            if tree_index is None:
                raise ValueError(f"No tree of subcategory '{on_tree}' at index {which_tree_idx}.")
        else:
            # If no index provided, use the first match if only one, else ask
            if len(matching_trees) == 1:
                tree_index, tree = matching_trees[0]
            else:
                if print_:
                    for i, (idx, elem) in enumerate(matching_trees):
                        print(f"{i}. {elem}")
                num = int(input("Choose the index of the tree on which you want to put your card: "))
                tree_index, tree = matching_trees[num]

        # Place the card
        if up:
            if tree["up"] ==None :
                tree["up"] = [Card.up]
            else:
                tree["up"].append(Card.up)

        elif down:
            if tree["down"]==None:
                tree["down"] = [Card.down]
            else:
                tree["down"].append(Card.down)
        elif left:
            if tree["left"]==None :
                tree["left"] = [Card.left]
            else:
                tree["left"].append(Card.left)
        elif right:
            if tree["right"]==None :
                tree["right"] = [Card.right]
            else:
                tree["right"].append(Card.right)

        return self

    def how_many_per_subcategory(self, subcategory, subcategory2=None, category2=None,
                            up=False,
                            down=False,
                            left=False,
                            right=False,
                            arbre=False,
                            print_=False):
        count = 0
        for elem in self.plateau_player:
            if up == True and arbre ==True and down == False and left == False and right == False:
                if elem["arbre"].subcategory == subcategory2:
                        if elem["up"] != None:
                            if (elem["up"][0].subcategory) == subcategory:
                                count += 1
            # elif left == True and right ==True and down == False and arbre == False and up == False:
            #     if isinstance(elem["right"], list):
            #         if elem["right"][0].category == category2:
            #                 if elem["left"] != None:
            #                     if (elem["left"][0].subcategory) == subcategory:
            #                         count += 1
            # elif left == True and right ==True and down == False and arbre == False and up == False:
            #     if isinstance(elem["left"], list):
            #         if elem["left"][0].category == category2:
            #             if elem["right"] != None:
            #                 print(elem)
            #                 if (elem["right"][0].subcategory) == subcategory:
            #                     print(elem)
            #                     count += 1
            else:
                if subcategory in self.count_all_subcategories_on_plateau():
                    count = self.count_all_subcategories_on_plateau()[subcategory]

        if print_==True:
            print(f"Player {self.player_id} has {count} {subcategory}{"s" if count>1 else ""} on Plateau.")
        return count

    def how_many_per_category(self, category,
                            print_=False):
        if category in self.count_all_categories_on_plateau():
            count = self.count_all_categories_on_plateau()[category]

        if print_==True:
            print(f"Player {self.player_id} has {count} {category}{"s" if count>1 else ""} on Plateau.")
        return count

    def all_trees_player(self):
        boul = self.how_many_tree_subcat("bouleau")
        ch = self.how_many_tree_subcat("chêne")
        ht = self.how_many_tree_subcat("hêtre")
        marr = self.how_many_tree_subcat("marronnier_commun")
        sbl = self.how_many_tree_subcat("sapin_blanc")
        spD = self.how_many_tree_subcat("sapin_Douglas")
        tll = self.how_many_tree_subcat("tilleul")
        er = self.how_many_tree_subcat("érable")
        return {
            "bouleau":boul,
            "chêne":ch,
            "hêtre":ht,
            "marronnier_commun":marr,
            "sapin_blanc":sbl,
            "sapin_Douglas":spD,
            "tilleul":tll,
            "érable":er
        }

    def count_trees_per_player(self):
        my_dict = self.all_trees_player()
        return sum(list(my_dict.values()))

    def at_least_1_tree_per_subcategory(self):
        my_dict = self.all_trees_player()
        for elem in my_dict:
            if my_dict[elem] > 0:
                next
            else: return False
        return True

        # if boul > 0 and ch > 0 and ht > 0 and marr > 0 and sbl > 0 and spD > 0 and tll > 0 and er > 0:
        #     return True
        # else: return False

    def count_bats(self):
        bats_dict = {
            "murin_de_Bechstein":0,
            "grand_rhinolophe":0,
            "oreillard_roux":0,
            "barbastelle_Europe":0
        }

        for elem in self.plateau_player:
            if elem["left"] != None:
                if isinstance(elem["left"], list):
                    if elem["left"][0] not in can_place_multiple_cards_same_spot:
                        if elem["left"][0].category == "chauve_souris":
                            bats_dict[(elem["left"][0].subcategory)] += 1

            if elem["right"] != None:
                if isinstance(elem["right"], list):
                    if elem["right"][0] not in can_place_multiple_cards_same_spot:
                        if elem["right"][0].category == "chauve_souris":
                            bats_dict[(elem["right"][0].subcategory)] += 1

        return bats_dict

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
                if isinstance(elem["up"], list):
                    if elem["up"][0] not in can_place_multiple_cards_same_spot:
                        if elem["up"][0].category == "papillon":
                            papillons_dict[(elem["up"][0].subcategory)] += 1
        return papillons_dict

    def points_bats(self, points):
        bats_dict = self.count_bats()
        how_many_difft = 0
        for k in bats_dict.keys():
            if bats_dict[k] > 0:
                how_many_difft += 1

        if how_many_difft == 3:
            points += 5

        return points

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

    def count_crapaud_sup1(self):
        count=0
        for dict_ in self.plateau_player:
            for elem in list(dict_.values()):
                if elem != None:
                    if isinstance(elem, list):
                        if elem[0].subcategory in can_place_multiple_cards_same_spot:
                            if elem[0].subcategory == "crapaud_commun":
                                if len(elem) >=2:
                                    count += 1

        return count

    def count_mosquitos(self):
        c = 0
        for elem in self.plateau_player:
            if elem["down"] != None:
                if isinstance(elem["down"], list):
                    if elem["down"][0].subcategory == "moustique":
                        c += 1
        return c

    def count_luciole_salamandre(self, subcategory):
        c = 0
        for elem in self.plateau_player:
            if elem["down"] != None:
                if isinstance(elem["down"], list):
                    if elem["down"][0].subcategory == subcategory:
                        c += 1
        return c

    def count_couleur_feuille(self):
        dict_colors = {
                    "vert clair":0,
                    "vert foncé":0,
                    "marron":0,
                    "orange":0,
                    "bleu clair":0,
                    "bleu foncé":0,
                    "jaune":0,
                    "rouge":0
                    }

        for color in dict_colors:
            count = 0
            # tmp = []

            for dict_ in self.plateau_player:
                if dict_["up"] != None:
                    for elem in (dict_["up"]):
                        if color == (elem.couleur_feuille):
                            # tmp.append(elem.subcategory)
                            count += 1
                if dict_["down"] != None:
                    for elem in (dict_["down"]):
                        if color == (elem.couleur_feuille):
                            # tmp.append(elem.subcategory)
                            count += 1
                if dict_["left"] != None:
                    for elem in (dict_["left"]):
                        if color == (elem.couleur_feuille):
                            # tmp.append(elem.subcategory)
                            count += 1
                if dict_["right"] != None:
                    for elem in (dict_["right"]):
                        if color == (elem.couleur_feuille):
                            # tmp.append(elem.subcategory)
                            count += 1
                if dict_["arbre"] != None:
                    if color == (dict_["arbre"].couleur_feuille):
                        # tmp.append(dict_["arbre"].subcategory)
                        count += 1

            dict_colors[color] = count #(count,tmp)

        # print(sum(list(dict_colors.values())))
        return (dict_colors)

    def count_trees_full(self):
        c = 0
        for dict_ in self.plateau_player:
            if None not in (dict_.values()):
                c += 1
        return c

    def count_pairs_loir_gris_chauve_souris(self):
        c = 0
        for dict_ in self.plateau_player:
            if dict_["left"] != None:
                if (dict_["left"][0].subcategory) == "loir_gris":
                    if (dict_["right"][0].category) == "chauve_souris":
                        c += 1
            if dict_["right"] != None:
                if (dict_["right"][0].subcategory) == "loir_gris":
                    if (dict_["left"][0].category) == "chauve_souris":
                        c += 1
        return c

    def count_all_categories_on_plateau(self):
        all_categories_on_plateau = {}
        for dict_ in self.plateau_player:
            if dict_["arbre"] !=None:
                if (dict_["arbre"].category) in all_categories_on_plateau:
                    all_categories_on_plateau[(dict_["arbre"].category)] += 1
                else:
                    all_categories_on_plateau[(dict_["arbre"].category)] = 1
            if dict_["up"] != None:
                for elem in dict_["up"]:
                    if isinstance(elem.category, str):
                        if (elem.category) in all_categories_on_plateau:
                            all_categories_on_plateau[(elem.category)] += 1
                        else:
                            all_categories_on_plateau[(elem.category)] = 1
                    else:
                        for cat in elem.category:
                            if cat in all_categories_on_plateau:
                                all_categories_on_plateau[cat] += 1
                            else:
                                all_categories_on_plateau[(cat)] = 1
            if dict_["down"] != None:
                for elem in dict_["down"]:
                    if isinstance(elem.category, str):
                        if (elem.category) in all_categories_on_plateau:
                            all_categories_on_plateau[(elem.category)] += 1
                        else:
                            all_categories_on_plateau[(elem.category)] = 1
                    else:
                        for cat in elem.category:
                            if cat in all_categories_on_plateau:
                                all_categories_on_plateau[cat] += 1
                            else:
                                all_categories_on_plateau[(cat)] = 1
            if dict_["left"] != None:
                for elem in dict_["left"]:
                    if isinstance(elem.category, str):
                        if (elem.category) in all_categories_on_plateau:
                            all_categories_on_plateau[(elem.category)] += 1
                        else:
                            all_categories_on_plateau[(elem.category)] = 1
                    else:
                        for cat in elem.category:
                            if cat in all_categories_on_plateau:
                                all_categories_on_plateau[cat] += 1
                            else:
                                all_categories_on_plateau[(cat)] = 1
            if dict_["right"] != None:
                for elem in dict_["right"]:
                    if isinstance(elem.category, str):
                        if (elem.category) in all_categories_on_plateau:
                            all_categories_on_plateau[(elem.category)] += 1
                        else:
                            all_categories_on_plateau[(elem.category)] = 1
                    else:
                        for cat in elem.category:
                            if cat in all_categories_on_plateau:
                                all_categories_on_plateau[cat] += 1
                            else:
                                all_categories_on_plateau[(cat)] = 1

        return all_categories_on_plateau

    def count_all_subcategories_on_plateau(self):
        all_subcategories_on_plateau = {}
        for dict_ in self.plateau_player:
            if dict_["arbre"] !=None:
                if (dict_["arbre"].subcategory) in all_subcategories_on_plateau:
                    all_subcategories_on_plateau[(dict_["arbre"].subcategory)] += 1
                else:
                    all_subcategories_on_plateau[(dict_["arbre"].subcategory)] = 1
            if dict_["up"] != None:
                for elem in dict_["up"]:
                    if isinstance(elem.subcategory, str):
                        if (elem.subcategory) in all_subcategories_on_plateau:
                            all_subcategories_on_plateau[(elem.subcategory)] += 1
                        else:
                            all_subcategories_on_plateau[(elem.subcategory)] = 1
                    else:
                        for cat in elem.subcategory:
                            if cat in all_subcategories_on_plateau:
                                all_subcategories_on_plateau[cat] += 1
                            else:
                                all_subcategories_on_plateau[(cat)] = 1
            if dict_["down"] != None:
                for elem in dict_["down"]:
                    if isinstance(elem.subcategory, str):
                        if (elem.subcategory) in all_subcategories_on_plateau:
                            all_subcategories_on_plateau[(elem.subcategory)] += 1
                        else:
                            all_subcategories_on_plateau[(elem.subcategory)] = 1
                    else:
                        for cat in elem.subcategory:
                            if cat in all_subcategories_on_plateau:
                                all_subcategories_on_plateau[cat] += 1
                            else:
                                all_subcategories_on_plateau[(cat)] = 1
            if dict_["left"] != None:
                for elem in dict_["left"]:
                    if isinstance(elem.subcategory, str):
                        if (elem.subcategory) in all_subcategories_on_plateau:
                            all_subcategories_on_plateau[(elem.subcategory)] += 1
                        else:
                            all_subcategories_on_plateau[(elem.subcategory)] = 1
                    else:
                        for cat in elem.subcategory:
                            if cat in all_subcategories_on_plateau:
                                all_subcategories_on_plateau[cat] += 1
                            else:
                                all_subcategories_on_plateau[(cat)] = 1
            if dict_["right"] != None:
                for elem in dict_["right"]:
                    if isinstance(elem.subcategory, str):
                        if (elem.subcategory) in all_subcategories_on_plateau:
                            all_subcategories_on_plateau[(elem.subcategory)] += 1
                        else:
                            all_subcategories_on_plateau[(elem.subcategory)] = 1
                    else:
                        for cat in elem.subcategory:
                            if cat in all_subcategories_on_plateau:
                                all_subcategories_on_plateau[cat] += 1
                            else:
                                all_subcategories_on_plateau[(cat)] = 1

        return all_subcategories_on_plateau

    def count_all_subcategories_down(self):
        all_subcategories_down = {}
        for dict_ in self.plateau_player:
            if dict_["down"] != None:
                for elem in dict_["down"]:
                    if isinstance(elem.subcategory, str):
                        if (elem.subcategory) in all_subcategories_down:
                            all_subcategories_down[(elem.subcategory)] += 1
                        else:
                            all_subcategories_down[(elem.subcategory)] = 1
                    else:
                        for cat in elem.subcategory:
                            if cat in all_subcategories_down:
                                all_subcategories_down[cat] += 1
                            else:
                                all_subcategories_down[(cat)] = 1

        return (all_subcategories_down)

    def count_cards_around_sapin_blanc(self):
        total_points = []
        for dict_ in self.plateau_player:
            points = 0
            if dict_["arbre"].subcategory == "sapin_blanc":
                # pprint(dict_)
                if dict_["up"] != None:
                    points += (len(dict_["up"]))
                if dict_["down"] != None:
                    points += (len(dict_["down"]))
                if dict_["left"] != None:
                    points += (len(dict_["left"]))
                if dict_["right"] != None:
                    points += (len(dict_["right"]))
                total_points.append(points)

        return sum(total_points)

    def count_point_all_tmp(self,res, game, animal_string, points_dict):
        can_only_be_counted_once_subcat = [
                                               "luciole",
                                               "amanite_tue_mouches", "coulemelle", "girolle", "cèpe_Bordeaux",
                                               "grand_mars_changeant", "paon_du_jour", "morio", "grande_tortue", "tabac_Espagne",

                                               "marronnier_commun",
                                               "salamandre_tachetée",
                                               ]

        points_per_card_up = [
                            "chouette_hulotte",
                            "autour_des_palombes",
                            "pic_epeiche",
                            "geai_des_chênes",
                            "bouvreuil_pivoire",
                             ]

        points_per_card_down = [
                            "fraise_des_bois",
                            "rainette_verte",
                            "mousse",
                            "fougère_arborescente",
                            "mûre",
                            "fourmi_rousse",
                            "cistude",
                            "hérisson",
                            "lucane",
                             ]

        points_per_card_arbre = [
                            "tilleul",
                            "chêne",
                            "sapin_Douglas",
                            "bouleau",
                            "hêtre",
                            "érable",
                             ]

        points_per_card_left_and_right = [
                            "barbastelle_Europe",
                            "murin_de_Bechstein",
                            "oreillard_roux",
                            "grand_rhinolophe",
                            "sanglier",
                            "blaireau_européen",
                            "marcassin",
                            "moustique",
                            "lynx",
                            "cerf_élaphe",
                            "loup",
                            "renard_roux",
                            "daim",
                            "fouine",
                             ]



        p = (self.count_points_animal(res=res, game=game,animal_string=animal_string))
        animal = all_categories[animal_string]

        if p != None and p!=0:
            if animal_string in points_per_card_up:
                    c = self.how_many_per_subcategory(animal_string, up=True, arbre="chêne")
                    points_dict[animal_string] = [c*p]

            elif animal_string in points_per_card_down:
                    c = self.how_many_per_subcategory(animal_string, down=True)
                    points_dict[animal_string] = [c*p]

            elif animal_string in points_per_card_arbre:
                    c = self.how_many_per_subcategory(animal_string, arbre=True)
                    points_dict[animal_string] = [c*p]

            elif animal_string in points_per_card_left_and_right:
                    c = self.how_many_per_subcategory(animal_string, right=True, left=True)
                    points_dict[animal_string] = [c*p]




            elif animal_string in can_only_be_counted_once_subcat:
                if animal.category == "papillon":
                    points_dict["papillon"] = [p]
                elif animal.subcategory == "luciole":
                    points_dict["luciole"] = [p]
                elif animal.subcategory == "marronnier_commun":
                    points_dict["marronnier_commun"] = [p]
                elif animal.subcategory == "salamandre_tachetée":
                    points_dict["salamandre_tachetée"] = [p]


            # this should be the last one
            else:
                    points_dict[animal_string].append(int(p))


        return points_dict

    def count_points_animal(self, res, game,
                            animal_string=None,
                            print_dict=False,
                            ):

        if animal_string != None:
            animal = all_categories[animal_string]

        else:
            points_dict = defaultdict(list)
            for animal in all_categories:
                    points_dict = self.count_point_all_tmp(res=res,
                                                        game=game,
                                                        animal_string=animal,
                                                        points_dict=points_dict)
            if print_dict:
                print()
                pprint(points_dict)

            for animal in points_dict:
                print(f"{animal} += {points_dict[animal][0]} points.")
            tmp_list = (list(points_dict.values()))
            totals = []
            for i in range(len(tmp_list)):
                totals.append(sum(tmp_list[i]))

            return sum(totals)

        for dict_ in self.plateau_player:
            points=0
            for elem in list(dict_.values()):
                if elem != None:
                    if animal.category != "arbre":

                        # Amphibien
                        if animal.subcategory == "crapaud_commun":
                            if isinstance(elem, list):
                                if elem[0].subcategory in can_place_multiple_cards_same_spot:
                                    if elem[0].subcategory == "crapaud_commun":
                                        c = self.count_crapaud_sup1()
                                        points += c*5
                                        return points
                        elif animal.subcategory == "salamandre_tachetée":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "salamandre_tachetée":
                                    c = self.count_luciole_salamandre(subcategory="salamandre_tachetée")
                                    if c == 1:
                                        points += 5
                                        return points
                                    elif c == 2:
                                        points += 15
                                        return points
                                    elif c == 3:
                                        points += 25
                                        return points
                        elif animal_string == "rainette_verte":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "rainette_verte":
                                    c = self.count_mosquitos()
                                    points += c*5

                                    return points
                        elif animal.subcategory == "cistude":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "cistude":
                                    points += 5
                                    return points

                        # CervidéOngulé
                        elif animal.subcategory == "cerf_élaphe":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "cerf_élaphe":
                                    if "arbre" in self.count_all_categories_on_plateau():
                                        c_arbre = self.count_all_categories_on_plateau()["arbre"]
                                    else: c_arbre = 0
                                    if "plant" in self.count_all_categories_on_plateau():
                                        c_plant = self.count_all_categories_on_plateau()["plant"]
                                    else: c_plant = 0
                                    points += (1*c_plant) + (1*c_arbre)
                                    return points
                        elif animal.subcategory == "chevreuil":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "chevreuil":

                                    possible_couleurs = []
                                    for dict_ in self.plateau_player:
                                        if dict_["left"] != None:
                                            if (dict_["left"][0].subcategory) == "chevreuil":
                                                possible_couleurs.append(dict_["left"][0].couleur_feuille)
                                        if dict_["right"] != None:
                                            if (dict_["right"][0].subcategory) == "chevreuil":
                                                possible_couleurs.append(dict_["right"][0].couleur_feuille)

                                    p = []
                                    for couleur in possible_couleurs:
                                        c = self.count_couleur_feuille()[couleur]
                                        points = 3*c
                                        print(f"chevreuil_{couleur.replace(" ", "_")} += {points} points.")
                                        p.append(points)
                                    return sum(p)
                        elif animal.subcategory == "daim":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "daim":
                                    if "ongulé" in self.count_all_categories_on_plateau():
                                        c_ongulé = self.count_all_categories_on_plateau()["ongulé"]
                                        points += 3*c_ongulé
                                    return points


                        # Champignon
                        elif animal.category == "champignon":
                            if isinstance(elem, list):
                                if elem[0].category == "champignon":
                                    return points

                        # ChauveSouris
                        elif animal.category == "chauve_souris":
                            if isinstance(elem, list):
                                if elem[0].category == "chauve_souris":
                                    if animal.subcategory == "barbastelle_Europe":
                                        points += self.points_bats(points)
                                        return points
                                    elif animal.subcategory == "oreillard_roux":
                                        points += self.points_bats(points)
                                        return points
                                    elif animal.subcategory == "grand_rhinolophe":
                                        points += self.points_bats(points)
                                        return points
                                    elif animal.subcategory == "murin_de_Bechstein":
                                        points += self.points_bats(points)
                                        return points

                        # Insecte
                        elif animal.subcategory == "fourmi_rousse":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "fourmi_rousse":
                                    c = sum(list(self.count_all_subcategories_down().values()))
                                    points += c*2
                                    return points
                        elif animal.subcategory == "luciole":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "luciole":
                                    c = self.count_luciole_salamandre(subcategory="luciole")
                                    if c == 1:
                                        points += 0
                                        return points
                                    elif c == 2:
                                        points += 10
                                        return points
                                    elif c == 3:
                                        points += 15
                                        return points
                                    elif c == 4:
                                        points += 20
                                        return points
                            elif animal.subcategory == "lucane":
                                if elem.subcategory == "lucane":
                                    c = self.how_many_per_category(category="plantigrade")
                                    points += 1*c
                                    return points
                        elif animal.subcategory == "moustique":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "moustique":
                                    c = self.how_many_per_category("chauve_souris")
                                    points += c * 1
                                    return points
                        elif animal.subcategory == "xylocope_violet":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "xylocope_violet":
                                    return points

                        # Oiseau
                        elif animal.subcategory == "bouvreuil_pivoire":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "bouvreuil_pivoire":
                                    c = self.how_many_per_category(category="insecte")
                                    points += 2*c
                                    return points
                        elif animal.subcategory == "pinson_des_arbres":
                            if isinstance(elem, list):
                                if (elem[0].subcategory) == "pinson_des_arbres":
                                    c = self.how_many_per_subcategory(subcategory="pinson_des_arbres",
                                              subcategory2="hêtre",
                                              up=True,
                                              arbre=True)
                                    points += c*5
                                    return points
                        elif animal.subcategory == "geai_des_chênes":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "geai_des_chênes":
                                    points += 3
                                    return points
                        elif animal.subcategory == "autour_des_palombes":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "autour_des_palombes":
                                        c = self.how_many_per_category("oiseau")
                                        points += (3*c)
                                        return points
                        elif animal.subcategory == "chouette_hulotte":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "chouette_hulotte":
                                    points += 5
                                    return points
                        elif animal.subcategory == "pic_epeiche":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "pic_epeiche":
                                    names = (game.who_max_trees(res))
                                    for name in names:
                                        for elem in res[name]["plateau"].plateau_player:
                                            animal = elem["up"]
                                            if animal != None:
                                                if animal[0].subcategory == "pic_epeiche":
                                                    points += 10
                                                    return points

                        # Ongulé
                        elif animal.subcategory == "sanglier":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "sanglier":
                                    c = self.how_many_per_subcategory("marcassin", left=True, right=True)
                                    if c > 0:
                                        points += 10
                                        return points
                        elif animal.subcategory == "marcassin":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "marcassin":
                                    points += 1
                                    return points

                        # Papillon
                        elif animal.category == "papillon" :
                            if isinstance(elem, list):
                                if elem[0].category == "papillon":
                                    if animal.subcategory == "grand_mars_changeant":
                                        points += self.points_papillon(points)
                                        return points
                                    elif animal.subcategory == "paon_du_jour":
                                        points += self.points_papillon(points)
                                        return points
                                    elif animal.subcategory == "morio":
                                        points += self.points_papillon(points)
                                        return points
                                    elif animal.subcategory == "grande_tortue":
                                        points += self.points_papillon(points)
                                        return points
                                    elif animal.subcategory == "tabac_Espagne":
                                        points += self.points_papillon(points)
                                        return points

                        # Plant
                        elif animal.subcategory == "fougère_arborescente":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "fougère_arborescente":
                                    total = self.how_many_per_category("amphibien")
                                    points += 6*total
                                    return points
                        elif animal.subcategory == "mousse":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "mousse":
                                    total = self.how_many_per_category("arbre")
                                    if total > 9:
                                        points += 10
                                        return points
                        elif animal.subcategory == "mûre":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "mûre":
                                    total = self.how_many_per_category("plant")
                                    points += 2*total
                                    return points
                        elif animal.subcategory == "fraise_des_bois":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "fraise_des_bois":
                                    if self.at_least_1_tree_per_subcategory():
                                        points += 10
                                        return points

                        # Plantigrade
                        elif animal.subcategory == "hérisson":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "hérisson":
                                        c = self.how_many_per_category("papillon")
                                        points += (3*c)
                                        return points
                        elif animal.subcategory == "lièvre_Europe":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "lièvre_Europe":
                                    if "lièvre_Europe" in self.count_all_subcategories_on_plateau():
                                        c = self.count_all_subcategories_on_plateau()["lièvre_Europe"]
                                        points += 1*c
                                    return points
                        elif animal.subcategory == "fouine":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "fouine":
                                    c = self.count_trees_full()
                                    points += 5*c
                                    return points
                        elif animal.subcategory == "loup":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "loup":
                                    if "cervidé" in self.count_all_categories_on_plateau():
                                        c_cervidé = self.count_all_categories_on_plateau()["cervidé"]
                                        points += c_cervidé*5
                                    return points
                        elif animal.subcategory == "renard_roux":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "renard_roux":
                                    if "lièvre_Europe" in self.count_all_subcategories_on_plateau():
                                        c_lievre = self.count_all_subcategories_on_plateau()["lièvre_Europe"]
                                        points += c_lievre*2
                                    return points
                        elif animal.subcategory == "taupe":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "taupe":
                                    return points
                        elif animal.subcategory == "loir_gris":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "loir_gris":
                                    c = self.count_pairs_loir_gris_chauve_souris()
                                    points += 15*c
                                    return points
                        elif animal.subcategory == "écureuil_roux":
                            if isinstance(elem, list):
                                if (elem[0].subcategory) == "écureuil_roux":
                                    c = self.how_many_per_subcategory(subcategory="écureuil_roux",
                                              subcategory2="chêne",
                                              up=True,
                                              arbre=True)
                                    points += c*5
                                    return points
                        elif animal.subcategory == "blaireau_européen":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "blaireau_européen":
                                    points += 2
                                    return points
                        elif animal.subcategory == "lynx":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "lynx":
                                    c = self.how_many_per_subcategory("chevreuil",left=True, right=True)
                                    if c > 0:
                                        points += 10
                                        return points
                        elif animal.subcategory == "raton_laveur":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "raton_laveur":
                                            return points
                        elif animal.subcategory == "ours_brun":
                            if isinstance(elem, list):
                                if elem[0].subcategory == "ours_brun":
                                            return points

                    elif animal.category == "arbre":
                        if animal.subcategory == "chêne":
                            if not isinstance(elem, list):
                                if elem.subcategory == "chêne":
                                    temp_dict = self.all_trees_player()

                                    missing = []
                                    for k,v in temp_dict.items():
                                        if k in list(all_trees.keys()):
                                            if v > 0:
                                                next
                                            else:
                                                print()
                                                missing.append(k)
                                    if len(missing) > 0:
                                        print(f"You are missing {"a " + missing[0] if len(missing)==1 else missing} to have all 8 categories of trees.")
                                        points += 0
                                        return points
                                    else:
                                        points += 10
                                        return points
                        elif animal.subcategory == "bouleau":
                            if not isinstance(elem, list):
                                if elem.subcategory == "bouleau":
                                    points += 1
                                return points
                        elif animal.subcategory == "hêtre":
                            if not isinstance(elem, list):
                                if elem.subcategory == "hêtre":
                                    c = self.how_many_tree_subcat(tree="hêtre")
                                    if c > 3:
                                        points += 5
                                        return points
                                    else:
                                        points += 0
                                        return points
                        elif animal.subcategory == "marronnier_commun":
                            if not isinstance(elem, list):
                                if elem.subcategory == "marronnier_commun":
                                    marronnier_counted = 0
                                    c = self.how_many_per_subcategory("marronnier_commun", arbre=True)
                                    if c == 1 and marronnier_counted == 0:
                                            points += 1
                                            print(f"{animal.subcategory} += {points} point.")
                                            marronnier_counted += 1
                                            return points
                                    elif c == 2 and marronnier_counted == 0:
                                        points += 4
                                        marronnier_counted += 1
                                        return points
                                    elif c == 3 and marronnier_counted == 0:
                                        points += 9
                                        marronnier_counted += 1
                                        return points
                                    elif c == 4 and marronnier_counted == 0:
                                        points += 16
                                        marronnier_counted += 1
                                        return points
                                    elif c == 5 and marronnier_counted == 0:
                                        points += 25
                                        marronnier_counted += 1
                                        return points
                                    elif c == 6 and marronnier_counted == 0:
                                        points += 36
                                        marronnier_counted += 1
                                        return points
                                    elif c >= 7 and marronnier_counted == 0:
                                        points += 49
                                        marronnier_counted += 1
                                        return points
                        elif animal.subcategory == "sapin_blanc":
                            if not isinstance(elem, list):
                                if elem.subcategory == "sapin_blanc":
                                    c = self.count_cards_around_sapin_blanc()
                                    points += 2*c
                                    return points
                        elif animal.subcategory == "sapin_Douglas":
                            if not isinstance(elem, list):
                                if elem.subcategory == "sapin_Douglas":
                                    points += 5
                                    return points
                        elif animal.subcategory == "tilleul":
                            if not isinstance(elem, list):
                                if elem.subcategory == "tilleul":
                                    names = (game.who_max_tilleuls(res))

                                    for name in names:
                                        if name == self.name:
                                            for elem in res[name]["plateau"].plateau_player:
                                                animal = elem["arbre"]
                                                if animal != None:
                                                    if animal.subcategory == "tilleul":
                                                        points += 3
                                                        return points
                                    else:
                                        points += 1
                                        return points
                        elif animal.subcategory == "érable":
                            if not isinstance(elem, list):
                                if elem.subcategory == "érable":
                                    c = self.how_many_per_category(category="arbre")
                                    points += 1*c
                                    return points
