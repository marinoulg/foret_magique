from src.Tree import *
from src.helper_functions.specific_functions import *

# Initialising game
nb_of_players = 2
game = Game(nb_of_players)
print(game.nb_of_players)

# Marine
marine = Player(player_id=1,nb_cards=6)

marine.draw_cards(Chêne(marine.player_id),
               Tilleul(marine.player_id))

plateau_marine = Plateau(marine.player_id)

print(marine.cards_player)
plateau_marine.poser_un_arbre(Chêne(marine.player_id))
plateau_marine.poser_un_arbre(Tilleul(marine.player_id))

print(plateau_marine.plateau_player)
marine.nb_tilleuls(plateau_marine.plateau_player)


# Victor
victor = Player(player_id=2, nb_cards=6)
victor.draw_cards(Tilleul(victor.player_id),Tilleul(victor.player_id),Tilleul(victor.player_id))

plateau_victor = Plateau(victor.player_id)
plateau_victor.poser_un_arbre(Tilleul(victor.player_id))
plateau_victor.poser_un_arbre(Tilleul(victor.player_id))

print(plateau_victor.plateau_player)
victor.nb_tilleuls(plateau_victor.plateau_player)

print(marine.puncts)
