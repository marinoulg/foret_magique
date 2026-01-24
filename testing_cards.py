from random import choice

from src.Tree import *
from src.Player import *
from src.helper_functions.specific_functions import *
from src.colors import which_color

from src.Champignon import *
from src.Oiseau import *
from src.Plantigrade import *
from src.Papillon import *
from src.Amphibien import *
from src.Insecte import *
from src.Cervidé import *
from src.Ongulé import *
from src.Plant import *
from src.PossibleColors import PossibleColors


p = PossibleColors()
# print(list(p.__dict__.keys()))
# print(p.__dict__) # use this once over

# Possible cards

# Tree
chêne = Chêne()
tilleul = Tilleul()
bouleau = Bouleau()
hêtre = Hêtre()
marronnier = Marronier()
sapin_blanc = SapinBlanc()
sapin_D = SapinDouglas()
érable = Erable()

# Champignon
amanite = Amanite(which_color("amanite"))
coul = Coulemelle(which_color("coulemelle"))
gir = Girolle(which_color("girolle"))
cepe = CèpeDeBordeaux(which_color("cèpe_bordeaux"))

# Oiseau
bouvreuil = BouvreuilPivoire(which_color("bouvreuilpivoire"))
pinson = PinsonDesArbres(which_color("pinson"))
geai = GeaiDesChênes(which_color("geai"))
palombe = AutourDesPalombes(which_color("palombes"))
pic = PicEpeiche(which_color("pic_epeiche"))

# Plantigrade
herisson = Hérisson(which_color("herisson"))
lievre = LièvreEurope(which_color("lièvre"))
fouine = Fouine(which_color("fouine"))
loup = Loup(which_color("loup"))
renard = RenardRoux(which_color("renard"))
taupe = Taupe(which_color("taupe"))
loir = LoirGris(which_color("loir"))
ecureuil = EcureuilRoux(which_color("ecureuil"))
blaireau = BlaireauEuropéen(which_color("blaireau"))
lynx = Lynx(which_color("lynx"))
raton_laveur = RatonLaveur(which_color("raton_laveur"))
ours = OursBrun(which_color("ours_brun"))

# Papillon
mars = GrandMarsChangeant(which_color("grand_mars"))
paon = PaonDuJour(which_color("paon_du_jour"))
morio = Morio(which_color("morio"))
grande_tort = GrandeTortue(which_color("grande_tortue"))
tabac_desp = TabacEspagne(which_color("tabac_espagne"))

# Amphibien
crapaud = CrapaudCommun(which_color("crapaud"))
salamandre = SalamandreTachetée(which_color("salamandre"))
rainette = RainetteVerte(which_color("rainette"))
cistude = Cistude(which_color("cistude"))

# Insecte
fourmi = FourmiRousse(which_color("fourmi"))
luciole = Luciole(which_color("luciole"))
lucane = Lucane(which_color("lucane"))
moustique = Moustique(which_color("moustique"))
xylocope = XylocopeViolet(which_color("xylocope"))

# Cervidé
cerf = CerfElaphe(which_color("cerf"))
chevreuil = Chevreuil(which_color("chevreuil"))
daim = Daim(which_color("daim"))

# Ongulé
sanglier = Sanglier(which_color("sanglier"))
marcassin = Marcassin(which_color("marcassin"))

# Plant
fougere = FougèreArborescente(which_color("fougère"))
mousse = Mousse(which_color("mousse"))
mure = Mûre(which_color("mure"))
fraise_des_bois = FraiseDesBois(which_color("fraise_des_bois"))


"""
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

# for card in (marine.cards_player):
#     print(card.subcategory + ", " + card.couleur_feuille)
"""
