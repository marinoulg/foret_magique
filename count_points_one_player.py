from src.Tree import *
from src.Player import *
from src.helper_functions.specific_functions import *
from src.PossibleColors import PossibleColors
from src.helper_functions.all_cards import get_the_deck
from src.helper_functions.game_functions import *

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

palom_crapaud = Card(up_down=True)
palom_crapaud.up = AutourDesPalombes()
palom_crapaud.down = CrapaudCommun("rouge")
marine.cards_player.append(palom_crapaud)

marine.print_cards()

"""
User places cards in Plateau
"""
marine_plateau.place_tree(bouleau)
marine_plateau.place_tree(chene)
marine_plateau.place_tree(chene)

# # I want to place down in Plateau above chene the autour_des_palombes bird
marine_plateau.place_non_tree_card(palom_crapaud, on_tree = "chêne", up=True, which_tree_idx=1)
marine_plateau.place_non_tree_card(palom_crapaud, on_tree = "chêne", up=True, print_=True)

print()
marine_plateau.pprint()

c = marine_plateau.how_many_per_species(palom_crapaud, "autour_des_palombes")
print(c)














# daim_chevr = Card(left_right=True)
# daim_chevr.left = Daim()
# daim_chevr.right = Chevreuil() # problem recognising CervidéOngulé
# marine.cards_player.append(daim_chevr)
