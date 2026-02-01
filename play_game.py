import streamlit as st
from streamlit_card import card

from src.helper_functions.all_cards import get_the_deck, all_cards
from src.helper_functions.game_functions import initialize_game_and_players
from src.Game import *
from src.Player import Card
from src.CountPoints import all_categories, all_trees

import os
import pandas as pd

# ------------------- Initialising environment variables ------------------
cards_start = os.getenv("CARDS_START")
deck=get_the_deck()
nb_of_cards=len(all_cards)
colors = [
        "rouge",
    "jaune",
    "orange",
    "vert foncé",
    "vert clair",
    "marron",
    "bleu clair",
    "bleu foncé",
]
categories = [
    "Amphibien",
    "Arbre",
    "Cervidé",
    "Champignon",
    "Chauve-souris",
    "Insecte",
    "Oiseau",
    "Ongulé",
    "Papillon",
    "Plante",
    "Plantigrade/digigrade"
]
df = pd.read_csv("settings.csv")
df = df.set_index("index")

res_tmp = df.to_dict()

winner = pd.read_csv("winner.csv")
winner = (winner.loc[0,"winner"])

nb_of_players = len(res_tmp)
names = list(res_tmp.keys())
game = Game(nb_of_players, names)
res, game = initialize_game_and_players(game)

# ------------------ getting information from first page -----------------
st.set_page_config(
    page_title="Game",
    page_icon="🌲",
    layout="wide"
)

# ---------------------- Functions ----------------------
def onclick():
    st.session_state["button"] = True

def initialize_session_states():
    if "button" not in st.session_state:
        st.session_state["button"] = False
    if "choice" not in st.session_state:
        st.session_state["choice"] = None
    if "up_down" not in st.session_state:
        st.session_state["up_down"] = None
    if "res" not in st.session_state:
        st.session_state.res = res

def place_cards_UX(name,i, cols, keys):
    button = cols[i].button(f'Player {name}', on_click=onclick, key=keys[0])
    if st.session_state["button"]:
        card = cols[i].radio(
                label="Choose the elements in your card",
                options=[
                    "Card is a **tree**",
                    "Card has components on the **left/right** sides",
                    "Card has components on the **up/down** sides"
                ],
                key=keys[1]
            )
        left, middle, right = cols[i].columns(3)
        if card == "Card is a **tree**":
            tree = left.radio(
                label="Which tree?",
                options = [tree for tree in all_trees],
                captions= ["\n\n" for _ in all_trees],
                key=keys[2]
                )

            Arbre = all_trees[tree]
            which_couleur_feuille = Arbre.couleur_feuille
            df = pd.DataFrame.from_dict(
                {"category":[Arbre.category],
                "subcategory":[Arbre.subcategory],
                "cost_card":[Arbre.cost_card],
                "couleur_feuille":[Arbre.couleur_feuille]}
                ).T
            df.columns=["Carte d'identité de l'Arbre"]
            cols[i].write(df)

        elif card == "Card has components on the **left/right** sides":
            card_ = Card(left_right=True)
            possibles = []
            which_subcategory = cols[i].text_input("Write the 3 first letters of the subcategory of your animal (ex: 'liè' for lièvre d'Europe etc.)").lower()
            after_loop = False
            for animal in all_categories:
                if animal[:3] == which_subcategory:
                    possibles.append(animal)
                    after_loop = True
            if after_loop and possibles == list():
                cols[i].write("Error. Try again.")
            elif after_loop:
                chosen = None
                if len(possibles)>1:
                    chosen = cols[i].radio(
                        label="",
                        options=[option for option in possibles],
                        key=keys[3]
                    )

                elif len(possibles)==1:
                    chosen = possibles[0]

                if chosen != None:
                    cols[i].write(f"You want to place on the Plateau the {chosen}.")

                    which_couleur_feuille = cols[i].radio(
                        label="Which couleur_feuille for your animal/plant?",
                        options = [color.capitalize() for color in colors])

                    Animal = all_categories[chosen]
                    Animal.couleur_feuille = which_couleur_feuille
                    df = pd.DataFrame.from_dict(
                        {"category":[Animal.category],
                        "subcategory":[Animal.subcategory],
                        "cost_card":[Animal.cost_card],
                        "couleur_feuille":[Animal.couleur_feuille]}
                        ).T
                    df.columns=["Carte d'identité de l'Animal"]
                    cols[i].write(df)
                    cols[i].write("---")

                    try:
                        tmp_button = cols[i].button("See my Plateau")
                        if tmp_button:
                                st.session_state.res[name]["plateau"].st_write(index=True, only_animals=True, subcategory=True, category=False)
                        which_tree = int(cols[i].text_input("Write the number of the index of the tree").lower())

                    except ValueError:
                        pass

                    left_right = st.radio(
                        "Place the card on the left or the right?",
                        ["left", "right"],
                        key=keys[4]
                    )
        elif card == "Card has components on the **up/down** sides":
            card_ = Card(up_down=True)
            possibles = []
            which_subcategory = cols[i].text_input("Write the 3 first letters of the subcategory of your animal (ex: 'liè' for lièvre d'Europe etc.)").lower()
            after_loop = False
            for animal in all_categories:
                if animal[:3] == which_subcategory:
                    possibles.append(animal)
                    after_loop = True
            if after_loop and possibles == list():
                cols[i].write("Error. Try again.")
            elif after_loop:
                chosen = None
                if len(possibles)>1:
                    chosen = cols[i].radio(
                        label="",
                        options=[option for option in possibles],
                        key=keys[5]
                    )

                elif len(possibles)==1:
                    chosen = possibles[0]

                if chosen != None:
                    cols[i].write(f"You want to place on the Plateau the {chosen}.")

                    which_couleur_feuille = cols[i].radio(
                        label="Which couleur_feuille for your animal/plant?",
                        options = [color.capitalize() for color in colors])

                    Animal = all_categories[chosen]
                    Animal.couleur_feuille = which_couleur_feuille
                    df = pd.DataFrame.from_dict(
                        {"category":[Animal.category],
                        "subcategory":[Animal.subcategory],
                        "cost_card":[Animal.cost_card],
                        "couleur_feuille":[Animal.couleur_feuille]}
                        ).T
                    df.columns=["Carte d'identité de l'Animal"]
                    cols[i].write(df)
                    cols[i].write("---")

                    try:
                        tmp_button = cols[i].button("See my Plateau")
                        if tmp_button:
                                st.session_state.res[name]["plateau"].st_write(index=True, only_animals=True, subcategory=True, category=False)
                        which_tree = int(cols[i].text_input("Write the number of the index of the tree").lower())

                    except ValueError:
                        pass

                    up_down = cols[i].radio(
                        "Place the card on the up or the down?",
                        ["up", "down"],
                        key=keys[6]
                    )



        validate = cols[i].button("Validate", key=keys[7])
        if validate:
            if card == "Card is a **tree**":
                st.session_state.res[name]["plateau"].place_tree(Arbre)


            elif card == "Card has components on the **left/right** sides":
                if left_right == "left":
                        card_.left = Animal
                        st.session_state.res[name]["plateau"].place_non_tree_card(card_,
                                                                                on_tree=st.session_state.res[name]["plateau"].plateau_player[which_tree]["arbre"].subcategory,
                                                                                left=True,
                                                                                which_tree_idx=which_tree)
                elif left_right == "right":
                    card_.right = Animal
                    st.session_state.res[name]["plateau"].place_non_tree_card(card_,
                                                                                on_tree=st.session_state.res[name]["plateau"].plateau_player[which_tree]["arbre"].subcategory,
                                                                                right=True,
                                                                                which_tree_idx=which_tree)

            elif card == "Card has components on the **up/down** sides":
                if up_down == "up":
                        card_.up = Animal
                        st.session_state.res[name]["plateau"].place_non_tree_card(card_,
                                                                                on_tree=st.session_state.res[name]["plateau"].plateau_player[which_tree]["arbre"].subcategory,
                                                                                up=True,
                                                                                which_tree_idx=which_tree)
                elif up_down == "down":
                    card_.down = Animal
                    st.session_state.res[name]["plateau"].place_non_tree_card(card_,
                                                                                on_tree=st.session_state.res[name]["plateau"].plateau_player[which_tree]["arbre"].subcategory,
                                                                                down=True,
                                                                                which_tree_idx=which_tree)

            st.session_state["button"] = False
            st.rerun() # Force a rerun to update the UI immediately
    else:
        for n in list(st.session_state.res.keys()):
            if n == name:
                st.write("---")
                st.write(n)
                st.session_state.res[name]["plateau"].st_write(index=True, only_animals=True, subcategory=True, category=False)
        cols[i].markdown(f"Total points of {name}: {st.session_state.res[name]['plateau'].count_points_animal(res=res, game=game)}")

# ------------------------ Code ------------------------
initialize_session_states()


cols = st.columns(nb_of_players, gap="medium")

start = 12
for i,name in enumerate(names):
    keys = [num for num in range(start,start+8)]
    place_cards_UX(name,i,cols, keys)
    start = start+9
