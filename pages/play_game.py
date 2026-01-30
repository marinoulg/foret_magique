import streamlit as st
from streamlit_card import card

from src.Tree import *
from src.Player import *
from src.helper_functions.specific_functions import *
from src.PossibleColors import PossibleColors
from src.helper_functions.all_cards import get_the_deck
from src.helper_functions.game_functions import *
from src.CountPoints import *
from src.Game import *

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

from src.CountPoints import all_trees

from streamlit_functions import *
# from main import names, winner
# from streamlit_functions import draw_spinning_wheel
import os
import pandas as pd

# ---------------------- Initialising .env variables ---------------------
cards_start = os.getenv("CARDS_START")
deck=get_the_deck()
nb_of_cards=len(all_cards)

df = pd.read_csv("settings.csv")
df = df.set_index("index")

res = df.to_dict()

winner = pd.read_csv("winner.csv")
winner = (winner.loc[0,"winner"])

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


st.set_page_config(
    page_title="Game",
    page_icon="🌲",
)

st.write(df)
st.write(res)
st.write(winner)

nb_of_players = len(res)
st.write(nb_of_players)

place_card = st.button(f"{winner}, do you want to place a card on your Plateau?")

card = st.radio(
        label="Choose the elements in your card",
        options=[   "Card is a **tree**",
            "Card has components on the **left/right** sides",
            "Card has components on the **up/down** sides"
        ]
    )
# def choose_card(card):

left, middle, right = st.columns(3)
if card == "Card is a **tree**":
    tree = left.radio(
        label="Which tree?",
        options = [tree for tree in all_trees],
        captions= ["\n\n" for _ in all_trees])

    middle.image("imgs/Bouleau.png", width=80)
    middle.image("imgs/Chêne.png", width=80)
    middle.image("imgs/Hêtre.png", width=80)
    middle.image("imgs/Marronnier_commun.png", width=80)
    middle.image("imgs/Sapin_blanc.png", width=80)
    middle.image("imgs/Sapin_Douglas.png", width=80)
    middle.image("imgs/Tilleul.png", width=80)
    middle.image("imgs/Érable.png", width=80)

    Arbre = all_trees[tree]
    which_couleur_feuille = Arbre.couleur_feuille
    df = pd.DataFrame.from_dict(
        {"category":[Arbre.category],
         "subcategory":[Arbre.subcategory],
         "cost_card":[Arbre.cost_card],
         "couleur_feuille":[Arbre.couleur_feuille]}
        ).T
    df.columns=["Carte d'identité de l'Arbre"]
    st.write(df)
    res[winner]["plateau"].place_tree(Arbre)
    st.write(res)

elif card == "Card has components on the **left/right** sides":
    card_ = Card(left_right=True)
    possibles = []
    which_subcategory = st.text_input("Write the 3 first letters of the subcategory of your animal (ex: 'liè' for lièvre d'Europe etc.)").lower()
    after_loop = False
    for animal in all_categories:
        if animal[:3] == which_subcategory:
            possibles.append(animal)
            after_loop = True
    # st.write(possibles)
    if after_loop and possibles == list():
        st.write("Error. Try again.")
    elif after_loop:
        chosen = None
        if len(possibles)>1:
            chosen = st.radio(
                label="",
                options=[option for option in possibles]
            )
        # elif possibles == []:
        #     pass
        elif len(possibles)==1:
            chosen = possibles[0]

        if chosen != None:
            st.write(f"You want to place on the Plateau the {chosen}.")

            which_couleur_feuille = st.radio(
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
            st.write(df)
            left_right = st.radio(
                "Place the card on the left or the right?",
                ["left", "right"]
            )
            # which_tree =

            if left_right == "left":
                card_.left = Animal
                # res[winner]["plateau"].place_non_tree_card(Animal, on_tree=, left=True)
            elif left_right == "right":
                card_.right = Animal






elif card == "Card has components on the **up/down** sides":
    category = left.radio(
        label="What's the category of your Card?",
        options = [category for category in categories],
        captions= ["\n\n" for _ in categories])

    middle.image("imgs/Amphibien.png", width=80)
    middle.image("imgs/Arbre.png", width=80)
    middle.image("imgs/Cervidé.png", width=80)
    middle.image("imgs/Champignon.png", width=80)
    middle.image("imgs/ChauveSouris.png", width=80)
    middle.image("imgs/Insecte.png", width=80)
    middle.image("imgs/Oiseau.png", width=80)
    middle.image("imgs/Ongulé.png", width=80)
    middle.image("imgs/Papillon.png", width=80)
    middle.image("imgs/Plante.png", width=80)
    middle.image("imgs/Plantigrade.png", width=80)


    which_couleur_feuille = left.radio(
        label="Which couleur_feuille for your animal/plant?",
        options = [color.capitalize() for color in colors])
    # middle.image("imgs/Bouleau.png", width=80)
    # middle.image("imgs/Chêne.png", width=80)
    # middle.image("imgs/Hêtre.png", width=80)
    # middle.image("imgs/Marronnier_commun.png", width=80)
    # middle.image("imgs/Sapin_blanc.png", width=80)
    # middle.image("imgs/Sapin_Douglas.png", width=80)
    # middle.image("imgs/Tilleul.png", width=80)
    # middle.image("imgs/Érable.png", width=80)
    # return category, which_couleur_feuille

# place = list()
# if place_card:
#     next
# try:
# subcat, couleur = choose_card(card)
# st.text("\n\n\n")
# st.write(subcat)
# except:
# next
