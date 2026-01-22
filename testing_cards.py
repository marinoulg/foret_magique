from random import choice

from src.Tree import *
from src.Player import *
from src.helper_functions.specific_functions import *

from src.Champignon import *
from src.Oiseau import *
from Plantigrade import *
from src.Papillon import *
from Amphibien import *


# Possible cards

chêne = Chêne()
tilleul = Tilleul()
bouleau = Bouleau()
hêtre = Hêtre()
marronnier = Marronier()
sapin_blanc = SapinBlanc()
sapin_D = SapinDouglas()
érable = Erable()

amanite = Amanite("marron")
coul = Coulemelle("orange")
gir = Girolle("vert clair")
cepe = CèpeDeBordeaux("bleu")

bouvreuil = BouvreuilPivoire("bleu")
pinson = PinsonDesArbres("rouge")
geai = GeaiDesChênes("orange")
palombe = AutourDesPalombes("marron")
pic = PicEpeiche("jaune")

herisson = Hérisson("vert")

mars = GrandMarsChangeant("jaune")
paon = PaonDuJour("jaune")
morio = Morio("rouge")
grande_tort = GrandeTortue("vert")
tabac_desp = TabacEspagne("marron")

crapaud = CrapaudCommun("marrn")
salamandre = SalamandreTachetée("jaune")
rainette = RainetteVerte("jaune")
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
