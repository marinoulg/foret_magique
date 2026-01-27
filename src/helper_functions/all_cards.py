from src.Player import Card

from src.Champignon import *
from src.Oiseau import *
from src.Plantigrade import *
from src.Papillon import *
from src.Amphibien import *
from src.Insecte import *
from src.Cervidé import *
from src.CervidéOngulé import *
from src.Ongulé import *
from src.Plant import *
from src.ChauveSouris import *

all_cards = [] # except Trees

def get_the_deck():
    # Up / Down
    card = Card(up_down=True)
    card.up = GrandMarsChangeant("jaune")
    card.down = Amanite("marron")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GrandMarsChangeant("orange")
    card.down = Mousse("bleu clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GrandeTortue("rouge")
    card.down = Taupe("marron")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = EcureuilRoux("vert foncé")
    card.down = SalamandreTachetée("jaune")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = EcureuilRoux("vert foncé")
    card.down = SalamandreTachetée("jaune")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PinsonDesArbres("rouge")
    card.down = Coulemelle("bleu foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PaonDuJour("bleu foncé")
    card.down = Hérisson("marron")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = BouvreuilPivoire("bleu clair")
    card.down = Hérisson("vert foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = AutourDesPalombes("bleu foncé")
    card.down = Hérisson("orange")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GrandMarsChangeant("orange")
    card.down = Cistude("rouge")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PaonDuJour("marron")
    card.down = Girolle("bleu foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = BouvreuilPivoire("bleu clair")
    card.down = RainetteVerte("jaune")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = EcureuilRoux("vert foncé")
    card.down = SalamandreTachetée("jaune")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PicEpeiche("jaune")
    card.down = CrapaudCommun("marron")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = Morio("orange")
    card.down = Girolle("vert clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = BouvreuilPivoire("bleu clair")
    card.down = Coulemelle("orange")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PaonDuJour("jaune")
    card.down = CrapaudCommun("vert foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = ChouetteHulotte("vert clair")
    card.down = CèpeDeBordeaux("bleu clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PinsonDesArbres("vert clair")
    card.down = FourmiRousse("vert foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GrandeTortue("vert foncé")
    card.down = Taupe("rouge")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = TabacEspagne("marron")
    card.down = Mûre("bleu foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PaonDuJour("orange")
    card.down = Luciole("vert foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GeaiDesChênes("vert clair")
    card.down = Luciole("bleu clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = TabacEspagne("vert foncé")
    card.down = Mousse("jaune")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = EcureuilRoux("orange")
    card.down = Luciole("rouge")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GeaiDesChênes("orange")
    card.down = FougèreArborescente("bleu foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PinsonDesArbres("rouge")
    card.down = Lucane("vert clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = ChouetteHulotte("rouge")
    card.down = CrapaudCommun("bleu clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = EcureuilRoux("bleu clair")
    card.down = CrapaudCommun("orange")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = EcureuilRoux("marron")
    card.down = FraiseDesBois("vert clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = ChouetteHulotte("vert foncé")
    card.down = Lucane("rouge")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = AutourDesPalombes("marron")
    card.down = CrapaudCommun("rouge")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PicEpeiche("jaune")
    card.down = FourmiRousse("vert clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = Morio("vert clair")
    card.down = RainetteVerte("marron")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PicEpeiche("bleu clair")
    card.down = FraiseDesBois("rouge")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = AutourDesPalombes("bleu foncé")
    card.down = FourmiRousse("vert foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = TabacEspagne("marron")
    card.down = Mûre("vert foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GrandeTortue("bleu foncé")
    card.down = Mûre("bleu clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GeaiDesChênes("vert clair")
    card.down = FougèreArborescente("orange")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PinsonDesArbres("vert foncé")
    card.down = CrapaudCommun("bleu foncé")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = Morio("rouge")
    card.down = Cistude("vert clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = PicEpeiche("jaune")
    card.down = CèpeDeBordeaux("bleu clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = Morio("rouge")
    card.down = Luciole("jaune")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GrandMarsChangeant("vert clair")
    card.down = RainetteVerte("marron")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = EcureuilRoux("vert foncé")
    card.down = SalamandreTachetée("jaune")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = ChouetteHulotte("vert foncé")
    card.down = FraiseDesBois("rouge")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = AutourDesPalombes("bleu clair")
    card.down = Mousse("jaune")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GrandeTortue("bleu foncé")
    card.down = SalamandreTachetée("bleu clair")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = TabacEspagne("marron")
    card.down = SalamandreTachetée("orange")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = BouvreuilPivoire("bleu foncé")
    card.down = FougèreArborescente("jaune")
    all_cards.append(card)

    card = Card(up_down=True)
    card.up = GeaiDesChênes("rouge")
    card.down = Amanite("bleu foncé")
    all_cards.append(card)

    # Left / Right
    card = Card(left_right=True)
    card.left = RenardRoux("jaune")
    card.right = Loup("bleu foncé")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = LièvreEurope("vert clair")
    card.right = Fouine("orange")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = MurinDeBechstein("marron")
    card.right = Loup("bleu foncé")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Loup("rouge")
    card.right = GrandRhinolophe("jaune")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = LièvreEurope("vert clair")
    card.right = CerfElaphe("orange")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = GrandRhinolophe("vert foncé")
    card.right = LoirGris("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = OreillardRoux("rouge")
    card.right = BlaireauEuropéen("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Sanglier("rouge")
    card.right = LièvreEurope("jaune")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Fouine("vert foncé")
    card.right = MurinDeBechstein("vert clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = LièvreEurope("bleu foncé")
    card.right = RenardRoux("marron")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Chevreuil("bleu foncé")
    card.right = Lynx("jaune")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = LièvreEurope("vert foncé")
    card.right = CerfElaphe("orange")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Loup("bleu clair")
    card.right = Moustique("orange")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Lynx("orange")
    card.right = RenardRoux("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = RenardRoux("vert foncé")
    card.right = Marcassin("marron")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = RenardRoux("jaune")
    card.right = XylocopeViolet("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.right = Daim("rouge")
    card.left = CerfElaphe("bleu foncé")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Sanglier("vert clair")
    card.right = Fouine("marron")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = LièvreEurope("marron")
    card.right = GrandRhinolophe("jaune")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Lynx("bleu clair")
    card.right = LièvreEurope("vert clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Marcassin("marron")
    card.right = Lynx("bleu foncé")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = RatonLaveur("bleu clair")
    card.right = LièvreEurope("rouge")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Lynx("bleu clair")
    card.right = RatonLaveur("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Moustique("vert clair")
    card.right = XylocopeViolet("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Fouine("rouge")
    card.right = OursBrun("orange")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = MurinDeBechstein("vert foncé")
    card.right = LoirGris("marron")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = OursBrun("jaune")
    card.right = RatonLaveur("bleu foncé")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = BarbastelleEurope("orange")
    card.right = Sanglier("marron")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = RenardRoux("jaune")
    card.right = XylocopeViolet("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = CerfElaphe("jaune")
    card.right = OursBrun("vert foncé")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Chevreuil("jaune")
    card.right = Marcassin("rouge")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = BlaireauEuropéen("orange")
    card.right = Moustique("marron")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = OreillardRoux("rouge")
    card.right = LièvreEurope("jaune")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = LièvreEurope("jaune")
    card.right = BlaireauEuropéen("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Daim("jaune")
    card.right = Sanglier("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = XylocopeViolet("bleu foncé")
    card.right = LièvreEurope("rouge")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Marcassin("orange")
    card.right = CerfElaphe("marron")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Daim("jaune")
    card.right = Chevreuil("bleu clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = XylocopeViolet("bleu clair")
    card.right = Lynx("vert foncé")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = LoirGris("bleu foncé")
    card.right = OreillardRoux("vert foncé")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = BarbastelleEurope("bleu foncé")
    card.right = XylocopeViolet("orange")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = BlaireauEuropéen("orange")
    card.right = Daim("vert clair")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = RatonLaveur("bleu foncé")
    card.right = Chevreuil("vert foncé")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = Sanglier("rouge")
    card.right = Chevreuil("orange")
    all_cards.append(card)

    card = Card(left_right=True)
    card.left = LoirGris("vert foncé")
    card.right = BarbastelleEurope("marron")
    all_cards.append(card)

    for _ in range(7):
        chêne = Chêne() # 7
        all_cards.append(chêne)

    for _ in range(9):
        tilleul = Tilleul() # 9
        all_cards.append(tilleul)

    for _ in range(10):
        bouleau = Bouleau() # 10
        all_cards.append(bouleau)

    for _ in range(10):
        hêtre = Hêtre() # 10
        all_cards.append(hêtre)

    for _ in range(11):
        marronnier = Marronnier() # 11
        all_cards.append(marronnier)

    for _ in range(6):
        sapin_blanc = SapinBlanc() # 6
        all_cards.append(sapin_blanc)

    for _ in range(7):
        sapin_D = SapinDouglas() # 7
        all_cards.append(sapin_D)

    for _ in range(6):
        érable = Erable() # 6
        all_cards.append(érable)

    # print(all_cards)
    # print(len(all_cards))

    """
    all instantiated cards if we wanted to ask user what was the color of their leaf

    # Tree
    chêne = Chêne()
    tilleul = Tilleul()
    bouleau = Bouleau()
    hêtre = Hêtre()
    marronnier = Marronnier()
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
    return all_cards
