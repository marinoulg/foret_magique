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

print(marine)
marine.print_cards()

"""
User gets handed 6 cards in real life, so they get instantiated in the
virtual version of the game.
"""


chene = Chêne()
marine.cards_player.append(chene)

bouleau = Bouleau()
marine.cards_player.append(bouleau)

xylo_lynx = Card(left_right=True)
xylo_lynx.right = Lynx()
xylo_lynx.left = XylocopeViolet()
marine.cards_player.append(xylo_lynx)

pic_fourmi = Card(up_down=True)
pic_fourmi.up = PinsonDesArbres()
pic_fourmi.down = FourmiRousse()
marine.cards_player.append(pic_fourmi)

marca_cerf = Card(left_right=True)
marca_cerf.left = Marcassin()
marca_cerf.rigth = CerfElaphe()
marine.cards_player.append(marca_cerf)

daim_chevr = Card(left_right=True)
daim_chevr.left = Daim()
daim_chevr.right = Chevreuil()
marine.cards_player.append(daim_chevr)

marine.print_cards()
