from random import choice

from src.Tree import *
from src.Player import *
from src.helper_functions.specific_functions import *

# Initialising game
nb_of_players = 2
game = Game(nb_of_players)
print(game.nb_of_players)

# Marine
marine = Player(player_id=1,nb_cards=6)

plateau_marine = Plateau(marine.player_id)


chêne = Chêne()
tilleul = Tilleul()
plateau_marine.poser_un_arbre(chêne)
plateau_marine.poser_un_arbre(tilleul)

print(plateau_marine.plateau_player)
# # plateau_marine.nb_tilleuls(marine.player_id)

# # print(plateau_marine.nb_tilleuls(plateau_marine.plateau_player))
# print(marine, end = "")
# # n_tilleuls = how_many_arbre_subcategory(plateau_marine.plateau_player, "tilleul")
# n_tilleuls = plateau_marine.how_many_tree_subcat("tilleuls")
# print(n_tilleuls)

# print(amanite.cost_card)
# print(amanite.category)
# print(amanite.subcategory)
# print(amanite.position)




# marine.play_card_down(marine.player_id, chêne, amanite)

# # Victor
# victor = Player(player_id=2, nb_cards=6)
# victor.draw_cards(Tilleul(victor.player_id),Tilleul(victor.player_id),Tilleul(victor.player_id))

# plateau_victor = Plateau(victor.player_id)
# plateau_victor.poser_un_arbre(Tilleul(victor.player_id))
# plateau_victor.poser_un_arbre(Tilleul(victor.player_id))

# print(plateau_victor.plateau_player)
# victor.nb_tilleuls(plateau_victor.plateau_player)

# print(marine.puncts)
