from random import choice, randint
from src.helper_functions.all_cards import all_cards
from src.Player import *
from src.CountPoints import *

# Initialising variables
deck = all_cards
clairiere = Clairiere()

def initialize_game_and_players(nb_of_players = 0,
                                names = [],
                                cards_start=6):

    game = Game(nb_of_players=nb_of_players)

    if nb_of_players == 0:
        nb_of_players = int(input("Enter the number of players: "))
    if names == []:
        names = [input(f"Enter the name of player {i+1}: ") for i in range(nb_of_players)]

    else:
        player_names = [name for name in names]

    res = {}
    for i,name in zip(range(1,(nb_of_players+1)),player_names):
        player = Player(nb_cards=cards_start, player_id=i)
        plateau = Plateau(player.player_id)

        res[name] = {"player":player,
                     "plateau":plateau,
                     "player_id":player.player_id}
        game.player_ids.append(player.player_id)
    return res, game


def take_out_cards_from_deck(deck, nb_cards_to_take_out=30):
    nb_of_cards = len(deck)
    print(f"There are a total of {len(deck)} cards in the deck.")
    print(f"Because of the rules, we will randomly take out {nb_cards_to_take_out} of these cards.")

    for i in range(nb_cards_to_take_out):
        idx_to_remove = randint(0,nb_of_cards-1) # I want to choose a card whose index we will take out
        deck.pop(idx_to_remove)
        nb_of_cards = len(deck)

    print(f"There are {len(deck)} cards left.")

def distribute_cards_to_player(Player, deck, cards_start=6):
    nb_of_cards = len(deck)
    for _ in range(cards_start):
        idx_to_remove = randint(0,nb_of_cards-1)
        card = deck.pop(idx_to_remove)
        Player.cards_player.append(card)
        nb_of_cards = len(deck)

def distribute_and_verify_player_has_tree_in_distribution(Player, deck, cards_start):
    print(f"Let's now randomly distribute {cards_start} cards from the deck to Player {Player.player_id}...")

    distribute_cards_to_player(Player, deck, cards_start)

    print("-"*15)
    print(f"Let's print out the {cards_start} cards of Player {Player.player_id}.")
    Player.print_cards()

    arbre = 0
    for card in Player.cards_player:
        try:
            print(card.subcategory)
            arbre += 1
        except:
            next

    if arbre == 0:
        for _ in range(cards_start):
            card = Player.cards_player.pop(0)
            random_int = randint(0,len(deck))
            deck.insert(random_int, card)

        print(Player.cards_player)
        print(f"We re-distribute cards to player {Player.player_id}.")
        distribute_cards_to_player(Player, deck, cards_start)
        print(Player.cards_player)

def create_first_second_deck(deck, divided):
    nb_of_cards = len(deck)
    print(f"There are {len(deck)} cards left.\n")
    print(f"Let's now create the 3 decks of {divided} cards each, or 1 deck of {divided*2} cards, and 1 deck of {divided} cards.")

    first_and_second_deck = []
    for i in range(divided*2):
        idx_to_remove = randint(0,nb_of_cards-1)
        item = deck.pop(idx_to_remove)
        first_and_second_deck.append(item)
        nb_of_cards = len(deck)
    print(f"First big deck created. There are {len(deck)} cards left.")
    return first_and_second_deck

def create_third_deck(deck, divided):
    nb_of_cards = len(deck)
    third_deck = []
    for i in range(divided):
        idx_to_remove = randint(0,nb_of_cards-1)
        item = deck.pop(idx_to_remove)
        third_deck.append(item)
        nb_of_cards = len(deck)
    print(f"Third deck created. There are {len(deck)} cards left.\n")
    return third_deck

def add_winter_cards(deck, first_and_second_deck, third_deck):
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
    return deck

def mix_cards_and_place_winter_cards(deck):
    divided = int(len(deck)/3)
    first_and_second_deck = create_first_second_deck(deck, divided)
    third_deck = create_third_deck(deck, divided)
    deck = add_winter_cards(deck, first_and_second_deck, third_deck)
    return deck




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

def player_picks_card_from_deck(Player, deck):
    card = deck.pop(0)
    Player.cards_player.append(card)
    return Player

def player_picks_card_from_Clairière(Player, deck):
    pass

def player_draws_2_cards(Player, deck):
    print(f"Player {Player.player_id} draws 2 cards \
either from the deck, or from the Clairière.")

    bool = input("Draw 1 card from deck or Clairière?. Type in D for deck or C for Clairière: ")
    if bool== "C":
        player_picks_card_from_Clairière(Player,deck)
    elif bool=="D":
        player_picks_card_from_deck(Player, deck)
    else:
        print("TypeError. Please input your answer again.")
        bool = input("Draw 1 card from deck or Clairière?. Type in D for deck or C for Clairière: ")


def player_plays_a_turn(Player):
    """
    pb de card here
    """

    print("We show la Clairière.")
    print(clairiere.__dict__)

    print(Player.print_cards())
    player_draws_2_cards(Player, deck)



    Player.print_cards(cost_card=True)
    print()

    card_idx = int(input("which card to put in Plateau? "))
    card_played = Player.cards_player[card_idx-1]
    Player.poser_un_arbre(card_played) # We do (card-1) bc we start at idx0 but here we start at card 1 (not card 0)
    # Player.cards_player.pop(card-1)
    nb_cards_owed = card_played.cost_card
    print(f"Player {Player.player_id} owes {card_played.cost_card} cards.")
    print(card_played)

    # We get rid of cards and put them in the Clairière
    if card_played.cost_card > 0:
        idx = 0
        while idx != nb_cards_owed:
            card = int(input("which card to put in Clairiere? "))
            clairiere.throw_card_in_clairiere(card_idx_in_list=card_idx, Player=Player)
            idx += 1

    # print(Player_plateau.__dict__)
    Player.print_cards()
