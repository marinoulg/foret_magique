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

# distribute_and_verify_player_has_tree_in_distribution(marine, deck, cards_start)

"""
User gets handed 6 cards in real life, so they get instantiated in the
virtual version of the game.
"""
chene = Chêne()
marine.cards_player.append(chene)

bouleau = Bouleau()
marine.cards_player.append(bouleau)

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

# marine.print_cards()

"""
User places cards in Plateau
"""
marine_plateau.place_tree(bouleau)
marine_plateau.place_tree(bouleau)
marine_plateau.place_tree(chene)
marine_plateau.place_tree(chene)
marine_plateau.place_tree(bouleau)
marine_plateau.place_tree(bouleau)
marine_plateau.place_tree(chene)
marine_plateau.place_tree(chene)
marine_plateau.place_tree(bouleau)
marine_plateau.place_tree(bouleau)
marine_plateau.place_tree(chene)
marine_plateau.place_tree(chene)

# # I want to place down in Plateau above chene the autour_des_palombes bird
# attention, l'ordre/index de mes arbres EST IMPORTANT
marine_plateau.place_non_tree_card(palom_mousse, on_tree = "chêne", down=True, which_tree_idx=3)
marine_plateau.place_non_tree_card(palom_mousse, on_tree = "chêne", down=True, which_tree_idx=2)
marine_plateau.place_non_tree_card(marca_cerf, on_tree = "chêne", left=True, which_tree_idx=6)

# print()
# marine_plateau.pprint()
print(marine_plateau.how_many_per_category(chene, chene.category))

# c = marine_plateau.how_many_per_subcategory(palom_mousse, palom_mousse.down.subcategory, down=True)
# print(c)



print(marine_plateau.count_points_animal(mousse=True))
# print(marine_plateau.how_many_tree_subcat(chene))







# daim_chevr = Card(left_right=True)
# daim_chevr.left = Daim()
# daim_chevr.right = Chevreuil() # problem recognising CervidéOngulé
# marine.cards_player.append(daim_chevr)
