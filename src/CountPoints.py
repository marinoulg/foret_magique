import os

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

all_trees = {   "chêne":Chêne(),
                "bouleau":Bouleau(),
                "hêtre":Hêtre(),
                "marronnier_commun":Marronnier(),
                "sapin_blanc":SapinBlanc(),
                "sapin_Douglas":SapinDouglas(),
                "tilleul":Tilleul(),
                "érable":Erable()
                }

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
                        print(an["up"].subcategory, end=", ")
                    if an["down"] != None:
                        print(an["down"].subcategory, end=", ")
                    if an["left"] != None:
                        print(an["left"].subcategory, end=", ")
                    if an["right"] != None:
                        print(an["right"].subcategory, end=", ")
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
                    if an["arbre"] != None:
                        print(f"{i}:", an["arbre"].category, end=": ")
                    if an["up"] != None:
                        print(an["up"].category, end=", ")
                    if an["down"] != None:
                        print(an["down"].category, end=", ")
                    if an["left"] != None:
                        print(an["left"].category, end=", ")
                    if an["right"] != None:
                        print(an["right"].category, end=", ")
                    print(end="\n")

            if index==False:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        print(an["arbre"].category, end=": ")
                    if an["up"] != None:
                        print(an["up"].category, end=", ")
                    if an["down"] != None:
                        print(an["down"].category, end=", ")
                    if an["left"] != None:
                        print(an["left"].category, end=", ")
                    if an["right"] != None:
                        print(an["right"].category, end=", ")
                    print(end="\n")
        elif only_animals==True and category ==True and subcategory == True:
            if index==True:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        print(f"{i}: {an["arbre"].subcategory} - {an["arbre"].category}", end=": ")
                    if an["up"] != None:
                        print(f"{an["up"].subcategory} - {an["up"].category}", end=", ")
                    if an["down"] != None:
                        print(f"{an["down"].subcategory} - {an["down"].category}", end=", ")
                    if an["left"] != None:
                        print(f"{an["left"].subcategory} - {an["left"].category}", end=", ")
                    if an["right"] != None:
                        print(f"{an["right"].subcategory} - {an["right"].category}", end=", ")
                    print(end="\n")

            if index==False:
                for i,an in zip(range(len(self.plateau_player)), self.plateau_player):
                    if an["arbre"] != None:
                        print(an["arbre"].category, end=": ")
                    if an["up"] != None:
                        print(an["up"].category, end=", ")
                    if an["down"] != None:
                        print(an["down"].category, end=", ")
                    if an["left"] != None:
                        print(an["left"].category, end=", ")
                    if an["right"] != None:
                        print(an["right"].category, end=", ")
                    print(end="\n")
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
            tree["up"] = Card.up
        elif down:
            tree["down"] = Card.down
        elif left:
            tree["left"] = Card.left
        elif right:
            tree["right"] = Card.right

        return self

    def how_many_per_subcategory(self, subcategory,
                            up=False,
                            down=False,
                            left=False,
                            right=False,
                            arbre=False,
                            print_=False):
        count = 0
        for elem in self.plateau_player:
            if up == True:
                if elem["up"] != None:
                    if elem["up"].subcategory == subcategory:
                        count += 1

            if down == True:
                if elem["down"] != None:
                    if elem["down"].subcategory == subcategory:
                        count += 1

            if left == True:
                if elem["left"] != None:
                    if elem["left"].subcategory == subcategory:
                        count += 1

            if right == True:
                if elem["right"] != None:
                    if elem["right"].subcategory == subcategory:
                        count += 1

            if arbre == True:
                if elem["arbre"] != None:
                    if elem["arbre"].subcategory == subcategory:
                        count += 1
        if print_==True:
            print(f"Player {self.player_id} has {count} {subcategory}{"s" if count>1 else ""} on Plateau.")
        return count

    def how_many_per_category(self, category,
                            up=False,
                            down=False,
                            left=False,
                            right=False,
                            arbre=False):
        count = 0
        for elem in self.plateau_player:
            if up == True:
                if elem["up"] != None:
                    if elem["up"].category == category:
                        count += 1

            if down == True:
                if elem["down"] != None:
                    if elem["down"].category == category:
                        count += 1

            if left == True:
                if elem["left"] != None:
                    if elem["left"].category == category:
                        count += 1

            if right == True:
                if elem["right"] != None:
                    if elem["right"].category == category:
                        count += 1

            if arbre == True:
                if elem["arbre"] != None:
                    if elem["arbre"].category == category:
                        count += 1
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
            if elem["down"] != None:
                if elem["down"].subcategory == "moustique":
                    c += 1
        return c

    def count_luciole_salamandre(self, subcategory):
        c = 0
        for elem in self.plateau_player:
            if elem["down"] != None:
                if elem["down"].subcategory == subcategory:
                    c += 1
        return c

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
                             ]



        p = (self.count_points_animal(res=res, game=game,animal_string=animal_string))
        animal = all_categories[animal_string]

        if p != None and p!=0:
            if animal_string in points_per_card_up:
                    c = self.how_many_per_subcategory(animal_string, up=True)
                    points_dict[animal_string] = [c*p]

            elif animal_string in points_per_card_down:
                    c = self.how_many_per_subcategory(animal_string, down=True)
                    points_dict[animal_string] = [c*p]

            elif animal_string in points_per_card_arbre:
                    c = self.how_many_per_subcategory(animal_string, arbre=True)
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
                            ):

        points=0
        if animal_string != None:
            animal = all_categories[animal_string]

        else:
            points_dict = defaultdict(list)
            for animal in all_categories:
                    points_dict = self.count_point_all_tmp(res=res,
                                                        game=game,
                                                        animal_string=animal,
                                                        points_dict=points_dict)
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
            for elem in list(dict_.values()):
                if elem != None:
                    if animal.category != "arbre":

                        # Amphibien
                        if animal.subcategory == "crapaud_commun":
                            pass

                        elif animal.subcategory == "salamandre_tachetée":
                            if elem.subcategory == "salamandre_tachetée":
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

                            if elem.subcategory == "rainette_verte":
                                c = self.count_mosquitos()
                                points += c*5

                                return points
                        if animal.subcategory == "cistude":
                            if elem.subcategory == "cistude":
                                points += 5
                                return points

                        # Champignon
                        elif animal.category == "champignon":
                            if elem.category == "champignon":
                                return points

                        # Insecte
                        elif animal.subcategory == "fourmi_rousse":
                            if elem.subcategory == "fourmi_rousse":
                                count = 0
                                for elem in self.plateau_player:
                                    if (elem["down"]) != None:
                                        count += 1
                                points += (count)*2
                                return points
                        elif animal.subcategory == "luciole":
                            if elem.subcategory == "luciole":
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
                                c = self.how_many_per_category(category="plantigrade", down=True, up=True)
                                points += 1*c
                                return points

                        # Oiseau
                        elif animal.subcategory == "bouvreuil_pivoire":
                            if elem.subcategory == "bouvreuil_pivoire":
                                c = self.how_many_per_category(category="insecte", down=True, up=True)
                                points += 2*c
                                return points
                        elif animal.subcategory == "pinson_des_arbres":
                            if elem.subcategory == "pinson_des_arbres":
                                # if (dict_["arbre"].subcategory) == "hêtre":
                                #         points += 5
                                        return points
                            #     points = self.animal_tree(self, elem_plateau=dict_, up=True, animal_subcat="pinson_des_arbres", tree_subcat="hêtre",p=5)
                            # return points
                        elif animal.subcategory == "geai_des_chênes":
                            if elem.subcategory == "geai_des_chênes":
                                points += 3
                                return points
                        elif animal.subcategory == "autour_des_palombes":
                            if elem.subcategory == "autour_des_palombes":
                                    c = self.how_many_per_category("oiseau",
                                                            up=True)
                                    points += (3*c)
                                    return points
                        elif animal.subcategory == "chouette_hulotte":
                            if elem.subcategory == "chouette_hulotte":
                                points += 5
                                return points
                        elif animal.subcategory == "pic_epeiche":
                            if elem.subcategory == "pic_epeiche":
                                names = (game.who_max_trees(res))
                                for name in names:
                                    for elem in res[name]["plateau"].plateau_player:
                                        animal = elem["up"]
                                        if animal != None:
                                            if animal.subcategory == "pic_epeiche":
                                                points += 10
                                                return points

                        # Papillon
                        elif animal.category == "papillon" :
                            if elem.category == "papillon":
                                counting_papillons = 0
                                if counting_papillons==0 and animal.subcategory == "grand_mars_changeant":
                                    points += self.points_papillon(points)
                                    return points
                                elif counting_papillons==0 and animal.subcategory == "paon_du_jour":
                                    points += self.points_papillon(points)
                                    counting_papillons += 1
                                    return points
                                elif counting_papillons==0 and animal.subcategory == "morio":
                                    points += self.points_papillon(points)
                                    counting_papillons += 1
                                    return points
                                elif counting_papillons==0 and animal.subcategory == "grande_tortue":
                                    points += self.points_papillon(points)
                                    counting_papillons += 1
                                    return points
                                elif counting_papillons==0 and animal.subcategory == "tabac_Espagne":
                                    points += self.points_papillon(points)
                                    counting_papillons += 1
                                    return points

                        # Plant
                        elif animal.subcategory == "fougère_arborescente":
                            if elem.subcategory == "fougère_arborescente":
                                total = self.how_many_per_category("amphibien", down=True)
                                points += 6*total
                                return points
                        elif animal.subcategory == "mousse":
                            if elem.subcategory == "mousse":
                                total = self.how_many_per_category("arbre", arbre=True)

                                if total > 9:
                                    points += 10
                                    return points
                        elif animal.subcategory == "mûre":
                            if elem.subcategory == "mûre":
                                total = self.how_many_per_category("plant", down=True)
                                points += 2*total
                                return points
                        elif animal.subcategory == "fraise_des_bois":
                            if elem.subcategory == "fraise_des_bois":
                                if self.at_least_1_tree_per_subcategory():
                                    points += 10
                                    return points

                        # Plantigrade
                        elif animal.subcategory == "écureuil_roux":
                            if elem.subcategory == "écureuil_roux":
                                    # print(dict_)
                                    # if (dict_["arbre"].subcategory) == "chêne":
                                    #     points += 5
                                        return points
                        elif animal.subcategory == "taupe":
                            if elem.subcategory == "taupe":
                                return points

                        elif animal.subcategory == "hérisson":
                            if elem.subcategory == "hérisson":
                                    c = self.how_many_per_category("papillon",up=True)
                                    points += (3*c)
                                    return points
                    elif animal.category == "arbre":
                        # print(dict_)
                        # print()
                        if animal.subcategory == "chêne":
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
                            if elem.subcategory == "bouleau":
                                points += 1
                                return points
                        elif animal.subcategory == "hêtre":
                            if elem.subcategory == "hêtre":
                                pass
                        elif animal.subcategory == "marronnier_commun":
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
                            # print("--------------")
                            # if elem.subcategory == "sapin_blanc":
                            #     count = 0
                            #     print("dictttt:", dict_)
                            #     for k,v in elem.items():
                            #                 if v != None and k != "arbre":
                            #                     count += 1

                            #     points += (count)*2
                                return points
                        elif animal.subcategory == "sapin_Douglas":
                            if elem.subcategory == "sapin_Douglas":
                                points += 5
                                return points
                        elif animal.subcategory == "tilleul":
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
                            if elem.subcategory == "érable":
                                pass

    # def count(self, res, game):
    #     points_dict = defaultdict(list)

    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="bouleau", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="hêtre", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="chêne", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="chouette_hulotte", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="luciole", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="marronnier_commun", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="mûre", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="pic_epeiche", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="pinson_des_arbres", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="sapin_Douglas", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="sapin_blanc", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="tilleul", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="écureuil_roux", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="marcassin", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="rainette_verte", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="morio", points_dict=points_dict)
    #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="fougère_arborescente", points_dict=points_dict)
    #     # points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="pic_epeiche", points_dict=points_dict)
    #     # points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="pic_epeiche", points_dict=points_dict)
    #     # points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="pic_epeiche", points_dict=points_dict)
    #     # points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="pic_epeiche", points_dict=points_dict)
    #     # points_dict = self.count_point_all_tmp(res=res,game=game,animal_string="pic_epeiche", points_dict=points_dict)

    #     # for an in self.plateau_player:
    #     #         pprint(an)
    #     #         print()
    #     #         # Tree is full
    #     #         if an["up"] != None and an["down"] != None and an["left"] != None and an["right"] != None:
    #     #             up = (an["up"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=up, points_dict=points_dict)

    #     #             down = (an["down"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=down, points_dict=points_dict)

    #     #             left = (an["left"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=left, points_dict=points_dict)

    #     #             right = (an["right"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=right, points_dict=points_dict)

    #     #         # Tree missing "right"
    #     #         elif an["up"] != None and an["down"] != None and an["left"] != None and an["right"] == None:
    #     #             up = (an["up"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=up, points_dict=points_dict)

    #     #             down = (an["down"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=down, points_dict=points_dict)

    #     #             left = (an["left"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=left, points_dict=points_dict)

    #     #         # Tree missing left
    #     #         elif an["up"] != None and an["down"] != None and an["left"] == None and an["right"] != None:
    #     #             up = (an["up"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=up, points_dict=points_dict)

    #     #             down = (an["down"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=down, points_dict=points_dict)

    #     #             right = (an["right"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=right, points_dict=points_dict)

    #     #         # Tree missing up
    #     #         if an["up"] == None and an["down"] != None and an["left"] != None and an["right"] != None:
    #     #             down = (an["down"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=down, points_dict=points_dict)

    #     #             left = (an["left"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=left, points_dict=points_dict)

    #     #             right = (an["right"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=right, points_dict=points_dict)

    #     #         # Tree missing down
    #     #         if an["up"] != None and an["down"] == None and an["left"] != None and an["right"] != None:
    #     #             up = (an["up"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=up, points_dict=points_dict)

    #     #             left = (an["left"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=left, points_dict=points_dict)

    #     #             right = (an["right"].subcategory)
    #     #             points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=right, points_dict=points_dict)




    #             # if an["arbre"] != None:
    #             #     """
    #             #     not dealt with yet below
    #             #     """
    #             #     arbre_string = (an["arbre"].subcategory)
    #             #     points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=arbre_string, points_dict=points_dict)

    #     print()
    #     pprint(points_dict)
    #     tmp_list = (list(points_dict.values()))
    #     totals = []
    #     for i in range(len(tmp_list)):
    #         totals.append(sum(tmp_list[i]))
    #     return sum(totals)
    #     # points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=animal_string, points_dict=points_dict)
