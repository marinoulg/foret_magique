
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
from src.Plant import *
from src.ChauveSouris import *


# This is the start of a game (distributing cards) for 2 Players

# ---------------------- Initialising .env variables ---------------------
deck = all_cards
cards_start = 6
nb_of_cards = len(all_cards)
clairiere = Clairiere()

# ------------------------- Initialising players -------------------------
marine = Player(player_id=1,nb_cards=cards_start)
marine_plateau = Plateau(marine.player_id)

victor = Player(player_id=2,nb_cards=cards_start)
victor_plateau = Plateau(victor.player_id)

# ------------------------ Initialising the game -------------------------
take_out_cards_from_deck(deck, 30)

distribute_and_verify_player_has_tree_in_distribution(marine, deck, cards_start)
distribute_and_verify_player_has_tree_in_distribution(victor, deck, cards_start)

deck = mix_cards_and_place_winter_cards(deck)
# --------------------------------- DONE ---------------------------------
print(len(deck))
# c = deck.pop(0)
# print(c)
print()
print("-"*15)
print()
print("We start the game.")

starting_player = who_starts(marine, victor)

if starting_player == marine:
    other_player = victor
    player_plays_a_turn(marine)
else:
    other_player = marine
    player_plays_a_turn(victor)


"""
if starting_player == marine:
    other_player = victor
    print(f"Player {marine.player_id} draws 2 cards from the deck.")
    card = deck.pop(0)
    marine.cards_player.append(card)
    card = deck.pop(0)
    marine.cards_player.append(card)
    marine.print_cards(cost_card=True)

    # count number of trees
    # if starting_player has 1 tree: --> place Tree in Plateau
    # elif starting_player has more thah 1 tree: player decides --> which one to place Tree in Plateau
    # else

    card_idx = int(input("which card to put in Plateau? "))
    card_played = marine.cards_player[card_idx-1]
    marine_plateau.poser_un_arbre(card_played) # We do (card-1) bc we start at idx0 but here we start at card 1 (not card 0)
    # marine.cards_player.pop(card-1)
    nb_cards_owed = card_played.cost_card
    print(f"Player {marine.player_id} owes {card_played.cost_card} cards.")
    print(card_played)

    # We get rid of cards
    if card_played.cost_card > 0:
        idx = 0
        while idx != nb_cards_owed:
            card = int(input("which card to put in Clairiere? "))
            clairiere.throw_card_in_clairiere(card_idx, Player=marine)
            idx += 1
    # We put some cards in the Clairière

    print(marine_plateau.__dict__)
    marine.print_cards()

elif starting_player == victor:
    other_player = marine
    print(f"Player {victor.player_id} draws 2 cards from the deck.")
    card = deck.pop(0)
    victor.cards_player.append(card)
    card = deck.pop(0)
    victor.cards_player.append(card)
    victor.print_cards()

    card_idx = int(input("which card to put in Plateau? "))
    card_played = victor.cards_player[card_idx-1]
    # victor_plateau.poser_un_arbre(card_played)
    nb_cards_owed = card_played[card-1].cost_card

    print(f"Player {victor.player_id} owes {nb_of_cards} cards.")

    # We get rid of cards
    if nb_cards_owed > 0:
        idx = 0
        while idx != nb_cards_owed:
            card = int(input("which card to put in Clairiere? "))
            clairiere.throw_card_in_clairiere(card_idx, Player=marine)
            idx += 1
    # We put some cards in the Clairière

    print(victor_plateau.__dict__)
    victor.print_cards()


print(f"There are now {len(deck)} cards left in the deck.")


# Turn of other player
print()
print(f"Turn of Player {other_player.player_id} to play.")
print(f"Player {other_player.player_id} draws 2 cards\
either from the deck, or from the Clairière.")
"""
