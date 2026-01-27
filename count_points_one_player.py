from src.Tree import *
from src.Player import *
from src.helper_functions.specific_functions import *
from src.PossibleColors import PossibleColors
from src.helper_functions.all_cards import get_the_deck
from src.helper_functions.game_functions import *
from src.CountPoints import *

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

# ---------------------- Initialising .env variables ---------------------
deck = all_cards
cards_start = 6
nb_of_cards = len(all_cards)
clairiere = Clairiere()

# ------------------------- Initialising players -------------------------
marine = Player(player_id=1,nb_cards=cards_start)
marine_plateau = Plateau(marine.player_id)

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

card = Card(up_down=True)
card.up = BouvreuilPivoire('bleu clair')
card.down = Moustique("orange")


"""
User places cards in Plateau
"""
marine_plateau.place_tree(bouleau) # 0
marine_plateau.place_tree(hetre) # 1
marine_plateau.place_tree(chene) # 2
marine_plateau.place_tree(chene) # 3
marine_plateau.place_tree(marronnier) # 4
marine_plateau.place_tree(sap_bl) # 5
marine_plateau.place_tree(chene) # 6
marine_plateau.place_tree(sap_D) # 7
marine_plateau.place_tree(tilleul) # 8
marine_plateau.place_tree(erable) # 9
# marine_plateau.place_tree(chene) # 10
# marine_plateau.place_tree(chene) # 11

# # I want to place down in Plateau above chene the autour_des_palombes bird
# attention, l'ordre/index de mes arbres EST IMPORTANT
marine_plateau.place_non_tree_card(morioluciole, on_tree = "chêne", down=True, which_tree_idx=2)
marine_plateau.place_non_tree_card(fr_chouette, on_tree = "chêne", up=True, which_tree_idx=3)
marine_plateau.place_non_tree_card(fr_chouette, on_tree = "chêne", down=True, which_tree_idx=3)
marine_plateau.place_non_tree_card(marca_cerf, on_tree = "chêne", left=True, which_tree_idx=6)

marine_plateau.place_non_tree_card(morioluciole, on_tree = "érable", up=True)
marine_plateau.place_non_tree_card(mars_rainette, on_tree = "sapin_blanc", up=True)
marine_plateau.place_non_tree_card(morioluciole, on_tree = "hêtre", down=True, which_tree_idx=6)
# marine_plateau.place_non_tree_card(card, on_tree = "chêne", down=True, which_tree_idx=2)


# print()
marine_plateau.pprint()
# print(marine_plateau.how_many_per_category(chene, chene.category))

# c = marine_plateau.how_many_per_subcategory(palom_mousse, palom_mousse.down.subcategory, down=True)
# print(c)

# print(how_many_arbre_subcategory(marine_plateau.plateau_player))
# print(marine_plateau.how_many_tree_subcat("chêne"))
# print(marine_plate(bouleau))
print()
print(marine_plateau.count_points_animal())
# print(marine_plateau.how_many_tree_subcat(bouleau))


# pap_dict = (marine_plateau.count_papillons())
# how_many_difft = 0
# for k,v in pap_dict.items():
#     if pap_dict[k] > 0:
#         how_many_difft += 1

# pprint(pap_dict)




# daim_chevr = Card(left_right=True)
# daim_chevr.left = Daim()
# daim_chevr.right = Chevreuil() # problem recognising CervidéOngulé
# marine.cards_player.append(daim_chevr)
