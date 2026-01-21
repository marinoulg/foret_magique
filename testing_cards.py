from random import choice

from src.Tree import *
from src.Player import *
from src.helper_functions.specific_functions import *

from src.Champignon import *
from src.Oiseau import *
from src.Patte import *
from src.Papillon import *
from src.Lézard import *


# Possible cards

chêne = Chêne()
tilleul = Tilleul()
bouleau = Bouleau()
hêtre = Hêtre()
marronnier = Marronier()
sapin_blanc = Sapin_blanc()
sapin_D = Sapin_Douglas()
érable = Erable()

amanite = Amanite("marron")
coul = Coulemelle("orange")
gir = Girolle("vert clair")
cepe = Cèpe_de_Bordeaux("bleu")

bouvreuil = Bouvreuil_pivoire("bleu")
pinson = Pinson_des_arbres("rouge")
geai = Geai_des_chênes("orange")
palombe = Autour_des_palombes("marron")
pic = Pic_épeiche("jaune")

herisson = Hérisson("vert")

mars = Grand_mars_changeant("jaune")
paon = Paon_du_jour("jaune")
morio = Morio("rouge")
grande_tort = Grande_tortue("vert")
tabac_desp = Tabac_dEspagne("marron")

crapaud = Crapaud_commun("marrn")
salamandre = Salamandre_tachetée("jaune")
rainette = Rainette_verte("jaune")
cistude = Cistude("rouge")


cards_start = 6
marine = Player(player_id=1,nb_cards=cards_start)

for _ in range(cards_start):
    rand_choice = choice([chêne,
                            tilleul,
                            bouleau,
                            hêtre,
                            marronnier,
                            sapin_blanc,
                            sapin_D,
                            érable,

                            amanite,
                            coul,
                            gir,
                            cepe,

                            bouvreuil,
                            pinson,
                            geai,
                            palombe,
                            pic,

                            herisson,

                            mars,
                            paon,
                            morio,
                            grande_tort,
                            tabac_desp,

                            crapaud,
                            salamandre,
                            rainette,
                            cistude,])
    marine.draw_card(rand_choice)

for card in (marine.cards_player):
    print(card.subcategory + ", " + card.couleur_feuille)
