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
marca_cerf.rigth = CerfElaphe("marron")
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

bouv_moust = Card(up_down=True)
bouv_moust.up = BouvreuilPivoire('bleu clair')
bouv_moust.down = Moustique("orange")

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
marine_plateau.place_non_tree_card(morioluciole, on_tree = "bouleau", down=True, which_tree_idx=1)

marine_plateau.place_non_tree_card(fr_chouette, on_tree = "hêtre", up=True, which_tree_idx=2)
marine_plateau.place_non_tree_card(tab_mure, on_tree = "hêtre", down=True, which_tree_idx=2)

marine_plateau.place_non_tree_card(fr_chouette, on_tree = "chêne", up=True, which_tree_idx=3)

marine_plateau.place_non_tree_card(morioluciole, on_tree = "marronnier_commun", down=True, which_tree_idx=4)

marine_plateau.place_non_tree_card(mars_rainette, on_tree = "sapin_blanc", down=True, which_tree_idx=5)
marine_plateau.place_non_tree_card(palom_mousse, on_tree = "sapin_blanc", up=True, which_tree_idx=5)

marine_plateau.place_non_tree_card(marca_cerf, on_tree = "chêne", left=True, which_tree_idx=6)

marine_plateau.place_non_tree_card(pic_cepe, on_tree = "sapin_Douglas", up=True, which_tree_idx=7)

marine_plateau.place_non_tree_card(morioluciole, on_tree = "chêne", down=True, which_tree_idx=8)
marine_plateau.place_non_tree_card(ecu_salam, on_tree = "chêne", up=True, which_tree_idx=8)

marine_plateau.place_non_tree_card(morioluciole, on_tree = "érable", up=True, which_tree_idx=9)
marine_plateau.place_non_tree_card(geai_foug, on_tree = "chêne", down=True, which_tree_idx=10)
marine_plateau.place_non_tree_card(morioluciole, on_tree = "chêne", down=True, which_tree_idx=11)
marine_plateau.place_non_tree_card(morioluciole, on_tree = "marronnier_commun", down=True, which_tree_idx=12)
marine_plateau.place_non_tree_card(morioluciole, on_tree = "bouleau", down=True, which_tree_idx=13)
marine_plateau.place_non_tree_card(pic_cepe, on_tree = "sapin_Douglas", up=True, which_tree_idx=14)

marine_plateau.place_non_tree_card(ecu_salam, on_tree = "tilleul", down=True, which_tree_idx=15)

print(marine_plateau.name, end = "\n\n")
marine_plateau.pprint(index=False, only_animals=True, subcategory=True, category=False)
print()
print(marine_plateau.count_points_animal(res=res, game=game))

# print("---"*10)
# print(victor_plateau.name, end = "\n\n")
# victor_plateau.pprint(index=False, only_animals=True, subcategory=True, category=False)
# print()
# print(victor_plateau.count_points_animal(res=res, game=game))
# print()

# print(marine_plateau.all_trees_player())

# points =0
# for elem in marine_plateau.plateau_player:
#     if (elem["up"]) != None:
#         if elem["up"].subcategory == "écureuil_roux":
#             if (elem["arbre"].subcategory) == "chêne":
#                 points += 5
        #     for k,v in elem.items():
        #         if v != None and k == "arbre":
        #             count += 1
        #             print(v)

# points += (count)*2
# print(points)
