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

animals = {
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
                "ours_brun":OursBrun("jaune")
            }

class Plateau:
    def __init__(self, player_id):
        self.player_id = player_id
        self.plateau_player = list()

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

            elif down == True:
                if elem["down"] != None:
                    if elem["down"].subcategory == subcategory:
                        count += 1

            elif left == True:
                if elem["left"] != None:
                    if elem["left"].subcategory == subcategory:
                        count += 1

            elif right == True:
                if elem["right"] != None:
                    if elem["right"].subcategory == subcategory:
                        count += 1

            elif arbre == True:
                if elem["arbre"] != None:
                    if elem["arbre"].subcategory == subcategory:
                        count += 1
        if print_==True:
            print(f"{subcategory} has {count} number of cards on Plateau.")
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

            elif down == True:
                if elem["down"] != None:
                    if elem["down"].category == category:
                        count += 1

            elif left == True:
                if elem["left"] != None:
                    if elem["left"].category == category:
                        count += 1

            elif right == True:
                if elem["right"] != None:
                    if elem["right"].category == category:
                        count += 1

            elif arbre == True:
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
            if elem["up"] != None:
                if elem["up"].subcategory == "moustique":
                    c += 1
        return c

    def count_luciole(self):
        c = 0
        for elem in self.plateau_player:
            if elem["down"] != None:
                if elem["down"].subcategory == "luciole":
                    c += 1
        return c

    def count_point_all_tmp(self,res, game, animal_string, points_dict):
        can_only_be_counted_once_subcat = [
                                               "luciole",
                                               "amanite_tue_mouches", "coulemelle", "girolle", "cèpe_Bordeaux",
                                               "grand_mars_changeant", "paon_du_jour", "morio", "grande_tortue", "tabac_Espagne"
                                               ]

        p = (self.count_points_animal(res=res, game=game,animal_string=animal_string))
        animal = animals[animal_string]

        if p != None and p!=0:
            # print(animal_string)
            if animal_string not in can_only_be_counted_once_subcat:
                    points_dict[animal_string].append(int(p))

            else:
                if animal.category == "papillon":
                    points_dict["papillon"] = [p]
                elif animal.subcategory == "luciole":
                    points_dict["luciole"] = [p]

        return points_dict

    def count_points_animal(self, res, game,
                            animal_string=None,
                            ):
        points=0
        if animal_string != None:
            animal = animals[animal_string]

        else:
            points_dict = defaultdict(list)

            for an in self.plateau_player:
                if an["up"] != None:
                    animal_string = (an["up"].subcategory)
                    points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=animal_string, points_dict=points_dict)
                if an["down"] != None:
                    animal_string = (an["down"].subcategory)
                    points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=animal_string, points_dict=points_dict)
                if an["left"] != None:
                    animal_string = (an["left"].subcategory)
                    points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=animal_string, points_dict=points_dict)
                if an["right"] != None:
                    animal_string = (an["right"].subcategory)
                    points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=animal_string, points_dict=points_dict)


                if an["arbre"] != None:
                    """
                    not dealt with yet below
                    """
                    animal_string = (an["arbre"].subcategory)
                    # print(animal_string)
                    # points_dict = self.count_point_all_tmp(res=res,game=game,animal_string=animal_string, points_dict=points_dict)
                else:
                    print(an)


            print()
            pprint(points_dict)
            tmp_list = (list(points_dict.values()))
            totals = []
            for i in range(len(tmp_list)):
                totals.append(sum(tmp_list[i]))

            return sum(totals)

        for dict_ in self.plateau_player:
            for elem in list(dict_.values()):
                try:
                    if elem.category != "arbre":
                        # Amphibien
                        if animal.subcategory == "crapaud_commun":
                            # return points
                            pass

                        elif animal.subcategory == "rainette_verte":
                            if elem.subcategory == "rainette_verte":
                                c = self.count_mosquitos()
                                points += c*5
                                print(f"{animal.subcategory} += {points} points.")
                                return points

                        if animal.subcategory == "cistude":
                            points += 5
                            return points
                        # Champignon
                        elif animal.category == "champignon":
                            return points

                        # Insecte
                        elif animal.subcategory == "luciole":
                            luciole_counted = 0
                            if elem.subcategory == "luciole":
                                c = self.count_luciole()
                                if c == 1 and luciole_counted == 0:
                                    print(f"{animal.subcategory} += {points} points.")
                                    points += 0
                                    luciole_counted += 1
                                    return points
                                elif c == 2 and luciole_counted == 0:
                                    points += 10
                                    luciole_counted += 1
                                    print(f"{animal.subcategory} += {points} points.")
                                    return points
                                elif c == 3 and luciole_counted == 0:
                                    points += 15
                                    print(f"{animal.subcategory} += {points} points.")
                                    luciole_counted += 1
                                    return points
                                elif c == 5 and luciole_counted == 0:
                                    points += 20
                                    print(f"{animal.subcategory} += {points} points.")
                                    luciole_counted += 1
                                    return points

                        # Oiseau
                        elif animal.subcategory == "autour_des_palombes":
                            try:
                                if elem.subcategory == "autour_des_palombes":
                                    c = self.how_many_per_category("oiseau",
                                                            up=True)
                                    points += (3*c)
                                    print(f"{animal.subcategory} += {points} points.")
                                    return points
                            except AttributeError:
                                next

                        elif animal.subcategory == "chouette_hulotte":
                            if elem.subcategory == "chouette_hulotte":
                                points += 5
                                print(f"{animal.subcategory} += {points} points.")
                                return points

                        elif animal.subcategory == "pic_epeiche":
                            names = (game.who_max_trees(res))
                            for name in names:
                                for elem in res[name]["plateau"].plateau_player:
                                    animal = elem["up"]
                                    if animal != None:
                                        if animal.subcategory == "pic_epeiche":
                                            points += 10
                                            print(f"{animal.subcategory} += {points} points.")
                                            return points

                        # Papillon
                        elif animal.category == "papillon" :
                            counting_papillons = 0
                            if elem.subcategory == "grand_mars_changeant" and counting_papillons==0 and animal.subcategory == "grand_mars_changeant":
                                points += self.points_papillon(points)
                                print(f"{animal.subcategory} += {points} points.")
                                return points
                            elif elem.subcategory =="paon_du_jour" and counting_papillons==0 and animal.subcategory == "paon_du_jour":
                                points += self.points_papillon(points)
                                print(f"{animal.subcategory} += {points} points.")
                                counting_papillons += 1
                                return points
                            elif elem.subcategory =="morio" and counting_papillons==0 and animal.subcategory == "morio":
                                points += self.points_papillon(points)
                                print(f"{animal.subcategory} += {points} points.")
                                counting_papillons += 1
                                return points
                            elif elem.subcategory =="grande_tortue" and counting_papillons==0 and animal.subcategory == "grande_tortue":
                                points += self.points_papillon(points)
                                print(f"{animal.subcategory} += {points} points.")
                                counting_papillons += 1
                                return points
                            elif elem.subcategory =="tabac_Espagne" and counting_papillons==0 and animal.subcategory == "tabac_Espagne":
                                points += self.points_papillon(points)
                                print(f"{animal.subcategory} += {points} points.")
                                counting_papillons += 1
                                return points

                        # Plant
                        elif animal.subcategory == "mousse":
                            if elem.subcategory == "mousse":
                                total = self.how_many_per_category("arbre", arbre=True)

                                if total > 9:
                                    points += 10
                                    print(f"{animal.subcategory} += {points} points.")
                                    return points

                        elif animal.subcategory == "mûre":
                            if elem.subcategory == "mûre":
                                total = self.how_many_per_category("plant", down=True)
                                points += 2*total
                                print(f"{animal.subcategory} += {points} points.")
                                return points

                        elif animal.subcategory == "fraise_des_bois":
                            if elem.subcategory == "fraise_des_bois":
                                if self.at_least_1_tree_per_subcategory():
                                    points += 10
                                    print(f"{animal.subcategory} += {points} points.")
                                    return points
                    elif elem.category == "arbre":
                        pass
                except AttributeError:
                    next

    # def count_all_points(self):
    #     points=0
    #     self.count_points_animal(animal)
    #     if animal == None:
    #         for anim in animals:
    #             print(anim)
    #             points = self.count_points_animal(anim, points)
