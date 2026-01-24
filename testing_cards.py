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
amanite = Amanite(which_color(p.amanite))
coul = Coulemelle(which_color(p.coulemelle))
gir = Girolle(which_color(p.girolle))
cepe = CèpeDeBordeaux(which_color(p.cèpe_bordeaux))

# Oiseau
bouvreuil = BouvreuilPivoire(which_color(p.bouvreuilpivoire))
pinson = PinsonDesArbres(which_color(p.pinson))
geai = GeaiDesChênes(which_color(p.geai))
palombe = AutourDesPalombes(which_color(p.palombes))
pic = PicEpeiche(which_color(p.pic_epeiche))

# Plantigrade
herisson = Hérisson(which_color(p.herisson))
lievre = LièvreEurope(which_color(p.lièvre))
fouine = Fouine(which_color(p.fouine))
loup = Loup(which_color(p.loup))
renard = RenardRoux(which_color(p.renard))
taupe = Taupe(which_color(p.taupe))
loir = LoirGris(which_color(p.loir))
ecureuil = EcureuilRoux(which_color(p.ecureuil))
blaireau = BlaireauEuropéen(which_color(p.blaireau))
lynx = Lynx(which_color(p.lynx))
raton_laveur = RatonLaveur(which_color(p.raton_laveur))
ours = OursBrun(which_color(p.ours_brun))

# Papillon
mars = GrandMarsChangeant(which_color(p.grand_mars))
paon = PaonDuJour(which_color(p.paon_du_jour))
morio = Morio(which_color(p.morio))
grande_tort = GrandeTortue(which_color(p.grande_tortue))
tabac_desp = TabacEspagne(which_color(p.tabac_espagne))

# Amphibien
crapaud = CrapaudCommun(which_color(p.crapaud))
salamandre = SalamandreTachetée(which_color(p.salamandre))
rainette = RainetteVerte(which_color(p.rainette))
cistude = Cistude(which_color(p.cistude))

# Insecte
fourmi = FourmiRousse(which_color(p.fourmi))
luciole = Luciole(which_color(p.luciole))
lucane = Lucane(which_color(p.lucane))
moustique = Moustique(which_color(p.moustique))
xylocope = XylocopeViolet(which_color(p.xylocope))

# Cervidé
cerf = CerfElaphe(which_color(p.cerf))
chevreuil = Chevreuil(which_color(p.chevreuil))
daim = Daim(which_color(p.daim))

# Ongulé
sanglier = Sanglier(which_color(p.sanglier))
marcassin = Marcassin(which_color(p.marcassin))

# Plant
fougere = FougèreArborescente(which_color(p.fougère))
mousse = Mousse(which_color(p.mousse))
mure = Mûre(which_color(p.mure))
fraise_des_bois = FraiseDesBois(which_color(p.fraise_des_bois))



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
