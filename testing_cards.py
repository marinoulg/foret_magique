from random import choice, randint

from src.Tree import *
from src.Player import *
from src.helper_functions.specific_functions import *
from src.PossibleColors import PossibleColors
from src.all_cards import all_cards

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
print(f"There are a total of {len(all_cards)} cards in the deck.")
print("Because of the rules, we will randomly take out 30 of these cards.")

nb_of_cards = len(all_cards)
for i in range(30):
    idx_to_remove = randint(0,nb_of_cards-1) # I want to choose a card whose index we will take out
    all_cards.pop(idx_to_remove)
    nb_of_cards = len(all_cards)

print(f"There are {len(all_cards)} cards left.")

print("Let us now randomly distribute 6 cards from the deck to Player marine...")
cards_start = 6

marine = Player(player_id=1,nb_cards=cards_start)
marine_plateau = Plateau(marine.player_id)

victor = Player(player_id=2,nb_cards=cards_start)
victor_plateau = Plateau(victor.player_id)

for _ in range(cards_start):
    idx_to_remove = randint(0,nb_of_cards-1)
    item = all_cards.pop(idx_to_remove)
    marine.draw_card(item)
    nb_of_cards = len(all_cards)

# count number of trees
# if player has 1 or more trees --> ok to continue
# else: put cards back and draw again 6 cards

print("... and to Player victor")
for _ in range(cards_start):
    idx_to_remove = randint(0,nb_of_cards-1)
    item = all_cards.pop(idx_to_remove)
    victor.draw_card(item)
    nb_of_cards = len(all_cards)

# count number of trees
# if player has 1 or more trees --> ok to continue
# else: put cards back and draw again 6 cards

print(f"There are {len(all_cards)} cards left.\n")
divided = int(len(all_cards)/3)
print(f"Let's now create the 3 decks of {divided} cards each, or 1 deck of {divided*2} cards, and 1 deck of {divided} cards.")

first_and_second_deck = []
for i in range(divided*2):
    idx_to_remove = randint(0,nb_of_cards-1)
    item = all_cards.pop(idx_to_remove)
    first_and_second_deck.append(item)
    nb_of_cards = len(all_cards)
print(f"First big deck created. There are {len(all_cards)} cards left.")

third_deck = []
for i in range(divided):
    idx_to_remove = randint(0,nb_of_cards-1)
    item = all_cards.pop(idx_to_remove)
    third_deck.append(item)
    nb_of_cards = len(all_cards)
print(f"Third deck created. There are {len(all_cards)} cards left.\n")

print(f"Let us now add the 3 winter cards in the third deck of cards at random positions.")

for i in range(3):
    card_winter = Card(winter=True)
    idx_to_insert_at = randint(0, len(third_deck)-1)
    third_deck.insert(idx_to_insert_at, card_winter)

print(f"There are {len(third_deck)} cards in the third deck.")


for i in range(len(third_deck)):
    first_and_second_deck.append(third_deck[i])

deck = first_and_second_deck
print(f"There are now {len(deck)} cards in the deck (originally the first_and_second_deck) \
randomly distributed, and with winter_cards added to the deck and the 2 player's cards distributed to them.")

print("-"*15)
print(f"Let's print out the 6 cards of Player {marine.player_id}.")
marine.print_cards()

print("-"*15)
print(f"Let's print out the 6 cards of Player {victor.player_id}.")
victor.print_cards()

print()
print("-"*15)
print()
print("We start the game.")

def who_starts(player1, player2, biggest_in=6):
    player1.who_start = randint(1,biggest_in)
    player2.who_start = randint(1,biggest_in)

    pl1_score = player1.who_start
    pl2_score = player2.who_start

    if pl1_score > pl2_score :
        print(f"Player {player1.player_id}'s {pl1_score} is bigger than Player {player2.player_id}'s {pl2_score}, so Player {player1.player_id} starts.")
        return player1
    elif pl1_score < pl2_score :
        print(f"Player {player1.player_id}'s {pl1_score} is smaller than Player {player2.player_id}'s {pl2_score}, so Player {player2.player_id} starts.")
        return player2
    else:
        who_starts(player1, player2)

starting_player = who_starts(marine, victor)

if starting_player == marine:
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

    card = int(input("which card to put in Plateau? "))
    card_played = marine.cards_player[card-1]
    marine_plateau.poser_un_arbre(card_played) # We do (card-1) bc we start at idx0 but here we start at card 1 (not card 0)
    marine.cards_player.pop(card-1)
    nb_cards_owed = card_played.cost_card
    print(f"Player {marine.player_id} owes {card_played.cost_card} cards.")
    print(card_played)

    if card_played.cost_card > 0:
        idx = 0
        while idx != nb_cards_owed:
            card = int(input("which card to put in Clairiere? "))
            marine.throw_card_in_clairiere(card-1)
            idx += 1

    print(marine_plateau.__dict__)
    marine.print_cards()

else:
    print(f"Player {victor.player_id} draws 2 cards from the deck.")
    card = deck.pop(0)
    victor.cards_player.append(card)
    card = deck.pop(0)
    victor.cards_player.append(card)
    victor.print_cards()

    card = int(input("which card to put in Plateau? "))
    card_played = marine.cards_player[card-1]
    victor_plateau.poser_un_arbre(victor.cards_player[card-1])
    victor.cards_player.pop(card-1)
    nb_cards_owed = victor.cards_player[card-1].cost_card

    print(f"Player {victor.player_id} owes {nb_of_cards} cards.")
    print(victor.cards_player[card-1])

    if nb_cards_owed > 0:
        idx = 0
        while idx != nb_cards_owed:
            card = int(input("which card to put in Clairiere? "))
            victor.throw_card_in_clairiere(card-1)
            idx += 1

    print(victor_plateau.__dict__)
    victor.print_cards()


print(f"There are now {len(deck)} cards left in the deck.")



# We put some cards in the Clairière
