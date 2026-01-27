# ForêtMagique

# next steps:
- raise ValueError pour toutes les combinaisons impossibles (TBD)
- tester toutes les méthodes de classes créées
- implémenter le comptage des points (comment ? avoir une méthode .points() -- not sure)
- run scenarios
- build a game for 2 players
- problem recognising an animal of instance CervidéOngulé when instanciating it from start (but not all CervidéOngulé animals, ex it works for CerfElaphe, and Chevreuil?, but not for Daim)
- faire le point pour avoid circular imports

# Ongoing (count_point_animal):
2 cards cannot be on the same place (for now, to be corrected for Lievre et Crapaud etc.). If so, the lattest one takes the place of the former one, which it erases.

    # Amphibien
    crapaud_commun=False,
    salamandre_tachetée=False,
  ☑ rainette_verte=False,
    cistude=False,

    # CervidéOngulé
    cerf_élaphe=False,
    chevreuil=False,
    daim=False,

  # ☑ Champignon
  ☑ amanite_tue_mouches=False,
  ☑ coulemelle=False,
  ☑ girolle=False,
  ☑ cèpe_Bordeaux=False,

    # ChauveSouris
    murin_de_Bechstein=False,
    grand_rhinolophe=False,
    oreillard_roux=False,
    barbastelle_Europe=False,

    # Insecte
    fourmi_rousse=False,
  ☑ luciole=False,
    lucane=False,
    moustique=False,
    xylocope_violet=False,

    # Oiseau
    bouvreuil_pivoire=False,
    pinson_des_arbres=False,
    geai_des_chênes=False,
  ☑ autour_des_palombes=False,
    pic_epeiche=False,
  ☑ chouette_hulotte=False,

    # Ongulé
    sanglier=False,
    marcassin=False,

  # ☑ Papillon
  ☑ grand_mars_changeant=True,
  ☑ paon_du_jour=True,
  ☑ morio=True,
  ☑ grande_tortue=True,
  ☑ tabac_Espagne=True,

    # Plant
    fougère_arborescente=False,
  ☑ mousse=False,
    mûre=False,
  ☑ fraise_des_bois=False,

    # Plantigrade
    hérisson=False,
    lièvre_Europe=False,
    fouine=False,
    loup=False,
    renard_roux=False,
    taupe=False,
    loir_gris=False,
    écureuil_roux=False,
    blaireau_européen=False,
    lynx=False,
    raton_laveur=False,
    ours_brun=False,

     points=0

# Done :
- ☑ total points automatique
- ☑ subcategory names are aligned in all files, and if no color is given at initialising an animal, it is asked automatically
- ☑ add winter_card possibilities
- ☑ add grotte possibilities
- ☑ build the start of a game for 2 players
- ☑ print out player's cards
- ☑ have all possible existing cards in a list in ```all_cards.py```
- ☑ create all cards and have them actionable and ready to use (e.g., we can put a left/right/up/down card on any Tree)
- ☑ deal with positions
- ☑ create a module: you need to do ```pip install -e .``` to install it
- ☑ raise ValueError pour toutes les couleurs impossibles
- ☑ add color for the correct couleur_feuille
- ☑ deal with colors
- ☑ create classes for all possible cards with their adequate information
- ☑ coder les autres cartes restantes (cervidés etc.)
- ☑ check names of class MarineVictor not Marine_victor

question ouverte : *que faire pour le déroulement d'une partie ? instancier une carte dès qu'on en tire une nouvelle, ou bien avoir une grosse liste qui contienne toutes les cartes, et on randomchoice dedans (sachant que dans tous les cas on va randomchoice/randint etc.)* ?
--> avoir une grosse liste qui contienne toutes les cartes, et on randomchoice dedans (sachant que dans tous les cas on va randomchoice/randint etc.)
