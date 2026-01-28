from src.Tree import *
from src.Player import *
from src.helper_functions.specific_functions import *
from src.PossibleColors import PossibleColors
from src.helper_functions.all_cards import get_the_deck
from src.helper_functions.game_functions import *
from src.CountPoints import *
from src.Game import *

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

import os
# ---------------------- Initialising .env variables ---------------------
nb_of_players = int(os.getenv("NB_OF_PLAYERS"))
PLAYER_NAMES=["marine", "victor"]
cards_start = os.getenv("CARDS_START")

deck=get_the_deck()
nb_of_cards=len(all_cards)

# ------------------------- Initialising players -------------------------

game = Game(nb_of_players, PLAYER_NAMES)
res, game = initialize_game_and_players(game)

marine = res["marine"]["player"]
marine_plateau = res["marine"]["plateau"]

victor_plateau = res["victor"]["plateau"]


# res, game = Game(nb_players, player_names).initialize_game()

# marine = res["marine"]["player"]
# marine_plateau = res["marine"]["plateau"]

# victor_plateau = res["victor"]["plateau"]
# print(res)
# print(game.player_ids)



"""
User gets handed 6 cards in real life, so they get instantiated in the
virtual version of the game.
"""

chene = Chêne()
marine.cards_player.append(chene)

bouleau = Bouleau()
marine.cards_player.append(bouleau)

marronnier = Marronnier()
hetre = Hêtre()
sap_bl = SapinBlanc()
sap_bl2 = SapinBlanc()
sap_D = SapinDouglas()
tilleul = Tilleul()
erable = Erable()
marine.cards_player.append(marronnier)
marine.cards_player.append(hetre)
marine.cards_player.append(sap_bl)
marine.cards_player.append(sap_D)
marine.cards_player.append(tilleul)
marine.cards_player.append(erable)

xylo_lynx = Card(left_right=True)
xylo_lynx.right = Lynx("vert foncé")
xylo_lynx.left = XylocopeViolet("bleu clair")
marine.cards_player.append(xylo_lynx)

pic_fourmi = Card(up_down=True)
pic_fourmi.up = PicEpeiche("jaune")
pic_fourmi.down = FourmiRousse("vert clair")
marine.cards_player.append(pic_fourmi)

marca_cerf = Card(left_right=True)
marca_cerf.left = Marcassin("orange")
marca_cerf.right = CerfElaphe("marron")
marine.cards_player.append(marca_cerf)

palom_mousse = Card(up_down=True)
palom_mousse.up = AutourDesPalombes()
palom_mousse.down = Mousse("jaune")
marine.cards_player.append(palom_mousse)

fr_chouette = Card(up_down=True)
fr_chouette.up = ChouetteHulotte("vert foncé")
fr_chouette.down = FraiseDesBois("rouge")

mars_rainette = Card(up_down=True)
mars_rainette.up = GrandMarsChangeant("vert clair")
mars_rainette.down = RainetteVerte("marron")

morioluciole = Card(up_down=True)
morioluciole.up = Morio("rouge")
morioluciole.down = Luciole("jaune")
# marine.print_cards()

bouv_rainette = Card(up_down=True)
bouv_rainette.up = BouvreuilPivoire('bleu clair')
bouv_rainette.down = Moustique("orange")

pic_cepe = Card(up_down=True)
pic_cepe.up = PicEpeiche("jaune")
pic_cepe.down = CèpeDeBordeaux("bleu clair")

cist_morio = Card(up_down=True)
cist_morio.up = Morio("rouge")
cist_morio.down = Cistude("vert clair")

tab_mure = Card(up_down=True)
tab_mure.up = TabacEspagne("marron")
tab_mure.down = Mûre("vert foncé")

ecu_salam = Card(up_down=True)
ecu_salam.up = EcureuilRoux("vert foncé")
ecu_salam.down = SalamandreTachetée("jaune")

geai_foug = Card(up_down=True)
geai_foug.up = GeaiDesChênes("vert clair")
geai_foug.down = FougèreArborescente("orange")

palom_fourmi = Card(up_down=True)
palom_fourmi.up = AutourDesPalombes("bleu foncé")
palom_fourmi.down = FourmiRousse("vert foncé")

pinson_fourm = Card(up_down=True)
pinson_fourm.up = PinsonDesArbres("vert clair")
pinson_fourm.down = FourmiRousse("vert foncé")

heris_palom = Card(up_down=True)
heris_palom.up = AutourDesPalombes("bleu foncé")
heris_palom.down = Hérisson("orange")

chouette_lucane = Card(up_down=True)
chouette_lucane.up = ChouetteHulotte("vert foncé")
chouette_lucane.down = Lucane("rouge")

paon_crapaud = Card(up_down=True)
paon_crapaud.up = PaonDuJour("jaune")
paon_crapaud.down = CrapaudCommun("vert foncé")

palom_crapaud = Card(up_down=True)
palom_crapaud.up = AutourDesPalombes("marron")
palom_crapaud.down = CrapaudCommun("rouge")


# ----------------
bat_loir = Card(left_right=True)
bat_loir.left = LoirGris("vert foncé")
bat_loir.right = BarbastelleEurope("marron")

murin_loir = Card(left_right=True)
murin_loir.left = MurinDeBechstein("vert foncé")
murin_loir.right = LoirGris("marron")

oreill_loir = Card(left_right=True)
oreill_loir.left = LoirGris("bleu foncé")
oreill_loir.right = OreillardRoux("vert foncé")

sangl_chev = Card(left_right=True)
sangl_chev.left = Sanglier("rouge")
sangl_chev.right = Chevreuil("orange")

raton_chev = Card(left_right=True)
raton_chev.left = RatonLaveur("bleu foncé")
raton_chev.right = Chevreuil("vert foncé")

blair_daim = Card(left_right=True)
blair_daim.left = BlaireauEuropéen("orange")
blair_daim.right = Daim("vert clair")

chev_marc = Card(left_right=True)
chev_marc.left = Chevreuil("jaune")
chev_marc.right = Marcassin("rouge")

blair_moust = Card(left_right=True)
blair_moust.left = BlaireauEuropéen("orange")
blair_moust.right = Moustique("marron")

xylo_lievre = Card(left_right=True)
xylo_lievre.left = XylocopeViolet("bleu foncé")
xylo_lievre.right = LièvreEurope("rouge")

xylo_lynx = Card(left_right=True)
xylo_lynx.left = XylocopeViolet("bleu clair")
xylo_lynx.right = Lynx("vert foncé")

murin_loup = Card(left_right=True)
murin_loup.left = MurinDeBechstein("marron")
murin_loup.right = Loup("bleu foncé")

renard_loup = Card(left_right=True)
renard_loup.left = RenardRoux("jaune")
renard_loup.right = Loup("bleu foncé")

"""
# User places cards in Plateau
"""
marine_plateau.place_tree(bouleau) # 0
marine_plateau.place_tree(hetre) # 1
marine_plateau.place_tree(chene) # 2
marine_plateau.place_tree(chene) # 3
marine_plateau.place_tree(marronnier) # 4
marine_plateau.place_tree(sap_bl) # 5
marine_plateau.place_tree(chene) # 6
marine_plateau.place_tree(sap_D) # 7
marine_plateau.place_tree(chene) # 8
marine_plateau.place_tree(erable) # 9
marine_plateau.place_tree(chene) # 10
marine_plateau.place_tree(chene) # 11
marine_plateau.place_tree(marronnier) # 12
marine_plateau.place_tree(bouleau) # 13
marine_plateau.place_tree(sap_D) # 14
marine_plateau.place_tree(tilleul) # 15
marine_plateau.place_tree(sap_bl2) # 16
marine_plateau.place_tree(hetre) # 17
marine_plateau.place_tree(hetre) # 1
marine_plateau.place_tree(hetre) # 1
# marine_plateau.place_tree(hetre) # 1


victor_plateau.place_tree(bouleau) # 0
victor_plateau.place_tree(hetre) # 1
victor_plateau.place_tree(chene) # 2
victor_plateau.place_tree(chene) # 3
victor_plateau.place_tree(marronnier) # 4
victor_plateau.place_tree(sap_bl) # 5
victor_plateau.place_tree(chene) # 6
victor_plateau.place_tree(sap_D) # 7
victor_plateau.place_tree(tilleul) # 8
victor_plateau.place_tree(erable)
# victor_plateau.place_tree(tilleul) # 10

# # I want to place down in Plateau above chene the autour_des_palombes bird
# attention, l'ordre/index de mes arbres EST IMPORTANT
marine_plateau.place_non_tree_card(pinson_fourm, on_tree = "bouleau", up=True, which_tree_idx=0)
marine_plateau.place_non_tree_card(palom_crapaud, on_tree = "bouleau", down=True, which_tree_idx=0)
marine_plateau.place_non_tree_card(palom_crapaud, on_tree = "bouleau", down=True, which_tree_idx=0)
marine_plateau.place_non_tree_card(sangl_chev, on_tree = "bouleau", right=True, which_tree_idx=0)
marine_plateau.place_non_tree_card(sangl_chev, on_tree = "bouleau", left=True, which_tree_idx=0)

marine_plateau.place_non_tree_card(pinson_fourm, on_tree = "hêtre", up=True, which_tree_idx=1)
marine_plateau.place_non_tree_card(chouette_lucane, on_tree = "hêtre", down=True, which_tree_idx=1)
marine_plateau.place_non_tree_card(marca_cerf, on_tree = "hêtre", left=True, which_tree_idx=1)
marine_plateau.place_non_tree_card(marca_cerf, on_tree = "hêtre", right=True, which_tree_idx=1)

marine_plateau.place_non_tree_card(fr_chouette, on_tree = "chêne", up=True, which_tree_idx=2)
marine_plateau.place_non_tree_card(chouette_lucane, on_tree = "chêne", down=True, which_tree_idx=2)
marine_plateau.place_non_tree_card(bat_loir, on_tree = "chêne", right=True, which_tree_idx=2)
marine_plateau.place_non_tree_card(sangl_chev, on_tree = "chêne", left=True, which_tree_idx=2)

marine_plateau.place_non_tree_card(fr_chouette, on_tree = "chêne", down=True, which_tree_idx=3)
marine_plateau.place_non_tree_card(tab_mure, on_tree = "chêne", up=True, which_tree_idx=3)
marine_plateau.place_non_tree_card(oreill_loir, on_tree = "chêne", right=True, which_tree_idx=3)
marine_plateau.place_non_tree_card(murin_loir, on_tree = "chêne", left=True, which_tree_idx=3)

marine_plateau.place_non_tree_card(pinson_fourm, on_tree = "marronnier_commun", up=True, which_tree_idx=4)
marine_plateau.place_non_tree_card(palom_crapaud, on_tree = "marronnier_commun", down=True, which_tree_idx=4)
marine_plateau.place_non_tree_card(palom_crapaud, on_tree = "marronnier_commun", down=True, which_tree_idx=4)
marine_plateau.place_non_tree_card(murin_loir, on_tree = "marronnier_commun", left=True, which_tree_idx=4)
marine_plateau.place_non_tree_card(raton_chev, on_tree = "marronnier_commun", right=True, which_tree_idx=4)

marine_plateau.place_non_tree_card(mars_rainette, on_tree = "sapin_blanc", down=True,which_tree_idx=5)
marine_plateau.place_non_tree_card(ecu_salam, on_tree = "sapin_blanc", up=True,which_tree_idx=5)
marine_plateau.place_non_tree_card(blair_daim, on_tree = "sapin_blanc", left=True,which_tree_idx=5)
marine_plateau.place_non_tree_card(xylo_lievre, on_tree = "sapin_blanc", right=True,which_tree_idx=5)
marine_plateau.place_non_tree_card(xylo_lievre, on_tree = "sapin_blanc", right=True,which_tree_idx=5)

# marine_plateau.place_non_tree_card(marca_cerf, on_tree = "chêne", left=True, which_tree_idx=6)
marine_plateau.place_non_tree_card(ecu_salam, on_tree = "chêne", up=True, which_tree_idx=6)
marine_plateau.place_non_tree_card(xylo_lynx, on_tree = "chêne", right=True, which_tree_idx=6)
marine_plateau.place_non_tree_card(renard_loup, on_tree = "chêne", left=True, which_tree_idx=6)

marine_plateau.place_non_tree_card(pic_cepe, on_tree = "sapin_Douglas", up=True, which_tree_idx=7)
marine_plateau.place_non_tree_card(pic_cepe, on_tree = "sapin_Douglas", down=True, which_tree_idx=7)
marine_plateau.place_non_tree_card(blair_daim, on_tree = "sapin_Douglas", left=True, which_tree_idx=7)
marine_plateau.place_non_tree_card(blair_moust, on_tree = "sapin_Douglas", right=True, which_tree_idx=7)

marine_plateau.place_non_tree_card(palom_crapaud, on_tree = "chêne", down=True, which_tree_idx=8)
marine_plateau.place_non_tree_card(ecu_salam, on_tree = "chêne", up=True, which_tree_idx=8)
marine_plateau.place_non_tree_card(blair_moust, on_tree = "chêne", right=True, which_tree_idx=8)

marine_plateau.place_non_tree_card(morioluciole, on_tree = "érable", up=True, which_tree_idx=9)
marine_plateau.place_non_tree_card(bouv_rainette, on_tree = "érable", down=True, which_tree_idx=9)
marine_plateau.place_non_tree_card(xylo_lynx, on_tree = "érable", right=True, which_tree_idx=9)

marine_plateau.place_non_tree_card(geai_foug, on_tree = "chêne", up=True, which_tree_idx=10)
marine_plateau.place_non_tree_card(mars_rainette, on_tree = "chêne", down=True, which_tree_idx=10)
marine_plateau.place_non_tree_card(murin_loup, on_tree = "chêne", right=True, which_tree_idx=10)

marine_plateau.place_non_tree_card(morioluciole, on_tree = "chêne", up=True, which_tree_idx=11)
marine_plateau.place_non_tree_card(geai_foug, on_tree = "chêne", down=True, which_tree_idx=11)
marine_plateau.place_non_tree_card(chev_marc, on_tree = "chêne", left=True, which_tree_idx=11)
marine_plateau.place_non_tree_card(marca_cerf, on_tree = "chêne", right=True, which_tree_idx=11)

marine_plateau.place_non_tree_card(heris_palom, on_tree = "marronnier_commun", up=True, which_tree_idx=12)
marine_plateau.place_non_tree_card(murin_loup, on_tree = "marronnier_commun", right=True, which_tree_idx=12)

marine_plateau.place_non_tree_card(bouv_rainette, on_tree = "bouleau", up=True, which_tree_idx=13)
marine_plateau.place_non_tree_card(morioluciole, on_tree = "bouleau", down=True, which_tree_idx=13)
marine_plateau.place_non_tree_card(renard_loup, on_tree = "bouleau", left=True, which_tree_idx=13)

marine_plateau.place_non_tree_card(pic_cepe, on_tree = "sapin_Douglas", up=True, which_tree_idx=14)
marine_plateau.place_non_tree_card(pic_fourmi, on_tree = "sapin_Douglas", down=True, which_tree_idx=14)

marine_plateau.place_non_tree_card(bouv_rainette, on_tree = "tilleul", up=True, which_tree_idx=15)
marine_plateau.place_non_tree_card(ecu_salam, on_tree = "tilleul", down=True, which_tree_idx=15)

marine_plateau.place_non_tree_card(palom_mousse, on_tree = "sapin_blanc", down=True, which_tree_idx=16)
marine_plateau.place_non_tree_card(cist_morio, on_tree = "sapin_blanc", up=True, which_tree_idx=16)

marine_plateau.place_non_tree_card(pinson_fourm, on_tree = "hêtre", up=True, which_tree_idx=17)


print(marine_plateau.name, end = "\n\n")
marine_plateau.pprint(index=True, only_animals=True, subcategory=True, category=False)
print()

# print(marca_cerf.right.category)
# print(xylo_lynx.right.category)
# , animal_string="écureuil_roux"
print(marine_plateau.count_all_subcategories_on_plateau()["lièvre_Europe"])
# print()
print(marine_plateau.count_points_animal(res=res, game=game
                                        #  , animal_string="chevreuil"
                                        ))


# print(marine_plateau.how_many_per_subcategory(subcategory="écureuil_roux",
#                                               subcategory2="chêne",
#                                               up=True,
#                                               arbre=True))

# print()
# print(marine_plateau.count_crapaud_sup1())
# # print(marine_plateau.how_many_per_category("insecte",down=True, up=True))
# for animal_string in all_categories:
#     animal = all_categories[animal_string]
#     print(animal.subcategory)
# points_dict = defaultdict(list)
# print("---"*10)
# print(victor_plateau.name, end = "\n\n")
# victor_plateau.pprint(index=False, only_animals=True, subcategory=True, category=False)
# print()
# print(victor_plateau.count_points_animal(res=res, game=game))
# print()

# print(marine_plateau.all_trees_player())

points =0
# count = 0
# for elem in marine_plateau.plateau_player:
#     print(elem)
#     print()
    # if (elem["down"]) != None:
    #     count += 1
#         # if elem["down"].subcategory == "fourmi_rousse":
#             # print(elem["down"])
#             # if (elem["arbre"].subcategory) == "chêne":
#             #     points += 5
#         #     for k,v in elem.items():
#         #         if v != None and k == "arbre":
#         #             count += 1
#         #             print(v)

# points += (count)*2
# print(points)
# total_points = []
# # # écureuil_roux

# print(marine_plateau.count_all_categories_on_plateau()["arbre"])
# print(marine_plateau.count_all_categories_on_plateau()["plant"])
#     print()
#     for elem in list(dict_.values()):
#         if elem !=None:
#             if elem.subcategory=="pinson_des_arbres":
#                 if (dict_["arbre"].subcategory) == "hêtre":
#                     print(elem)
    #     if elem != None:
    #         print(elem)

# print()
# print(marine_plateau.count_couleur_feuille())
# print()
#     # tmp = []

# for dict_ in marine_plateau.plateau_player:
#     if dict_["left"] != None:
#         if (dict_["left"][0].subcategory) == "chevreuil":
#             print(dict_["left"][0].couleur_feuille)
#     if dict_["right"] != None:
#         if (dict_["right"][0].subcategory) == "chevreuil":
#             print(dict_["right"][0].couleur_feuille)


#         if dict_["up"] != None:
#             for elem in (dict_["up"]):
#                 if color == (elem.couleur_feuille):
#                     # tmp.append(elem.subcategory)
#                     count += 1
#         if dict_["down"] != None:
#             for elem in (dict_["down"]):
#                 if color == (elem.couleur_feuille):
#                     # tmp.append(elem.subcategory)
#                     count += 1
#         if dict_["left"] != None:
#             for elem in (dict_["left"]):
#                 if color == (elem.couleur_feuille):
#                     # tmp.append(elem.subcategory)
#                     count += 1
#         if dict_["right"] != None:
#             for elem in (dict_["right"]):
#                 if color == (elem.couleur_feuille):
#                     # tmp.append(elem.subcategory)
#                     count += 1
#         if dict_["arbre"] != None:
#             if color == (dict_["arbre"].couleur_feuille):
#                 # tmp.append(dict_["arbre"].subcategory)
#                 count += 1

#     dict_colors[color] = count #(count,tmp)

# print(sum(list(dict_colors.values())))
# print(dict_colors)
