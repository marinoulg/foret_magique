# ForêtMagique

# next steps:
- raise ValueError pour toutes les combinaisons impossibles (TBD)
- run scenarios
- build a game for 2 players

# Done (count_point_animal):
  # ☑☑ Amphibien
  ☑☑ crapaud_commun=False,
  ☑☑ salamandre_tachetée=False,
  ☑☑ rainette_verte=False,
  ☑☑ cistude=False,

  # ☑☑ CervidéOngulé
  ☑☑ cerf_élaphe=False,
  ☑☑ chevreuil=False,
  ☑☑ daim=False,

  # ☑☑ Champignon
  ☑☑ amanite_tue_mouches=False,
  ☑☑ coulemelle=False,
  ☑☑ girolle=False,
  ☑☑ cèpe_Bordeaux=False,

  # ☑☑ ChauveSouris
  ☑☑ murin_de_Bechstein=False,
  ☑☑ grand_rhinolophe=False,
  ☑☑ oreillard_roux=False,
  ☑☑ barbastelle_Europe=False,

  # ☑☑ Insecte
  ☑☑ fourmi_rousse=False,
  ☑☑ luciole=False,
  ☑☑ lucane=False,
  ☑☑ moustique=False,
  ☑☑ xylocope_violet=False,

  # ☑☑ Oiseau
  ☑☑ bouvreuil_pivoire=False,
  ☑☑ pinson_des_arbres=False,
  ☑☑ geai_des_chênes=False,
  ☑☑ autour_des_palombes=False,
  ☑☑ pic_epeiche=False,
  ☑☑ chouette_hulotte=False,

  # ☑☑ Ongulé
  ☑☑ sanglier=False,
  ☑☑ marcassin=False,

  # ☑☑ Papillon
  ☑☑ grand_mars_changeant=True,
  ☑☑ paon_du_jour=True,
  ☑☑ morio=True,
  ☑☑ grande_tortue=True,
  ☑☑ tabac_Espagne=True,

  # ☑☑ Plant
  ☑☑ fougère_arborescente=False,
  ☑☑ mousse=False,
  ☑☑ mûre=False,
  ☑☑ fraise_des_bois=False,

  # ☑☑ Plantigrade
  ☑☑ hérisson=False,
  ☑☑ lièvre_Europe=False
  ☑☑ fouine=False,
  ☑☑ loup=False,
  ☑☑ renard_roux=False,
  ☑☑ taupe=False,
  ☑☑ loir_gris=False,
  ☑☑ écureuil_roux=False, --> dépend des autres autour
  ☑☑ blaireau_européen=False,
  ☑☑ lynx=False,
  ☑☑ raton_laveur=False,
  ☑☑ ours_brun=False,

  # ☑☑ Tree
  ☑☑ chêne=False
  ☑☑ bouleau=False
  ☑☑ hêtre=False
  ☑☑ marronnier_commun=False
  ☑☑ sapin_blanc=False --> dépend des autres autour
  ☑☑ sapin_Douglas=False
  ☑☑ tilleul=False
  ☑☑ érable=False

# Done :
- ☑ tester toutes les méthodes de classes créées (ish)
- ☑ implémenter le comptage des points
- ☑ place_non_tree_card corrected
- ☑ total points automatique
- ☑ faire le point pour avoid circular imports
- ☑ subcategory names are aligned in all files, and if no color is given at initialising an animal, it is asked automatically
- ☑  problem recognising an animal of instance CervidéOngulé when instanciating it from start (but not all CervidéOngulé animals, ex it works for CerfElaphe, and Chevreuil?, but not for Daim)
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

# How to use automatic counting :
### 1. Starting the Game for automatic counting of points
To start the game in order to have access to your score at all times, you need to import the following files/librairies:
  ```
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

  import os
  ```
You also need to initialise the environment variables:
  ```
  # ---------------------- Initialising .env variables ---------------------
  nb_of_players = int(os.getenv("NB_OF_PLAYERS"))
  PLAYER_NAMES=["marine", "victor"]
  cards_start = os.getenv("CARDS_START")

  deck=get_the_deck()
  nb_of_cards=len(all_cards)
  ```
Finally, you need to initialise the players:
  ```
  # ------------------------- Initialising players -------------------------

  game = Game(nb_of_players, PLAYER_NAMES)
  res, game = initialize_game_and_players(game)

  marine = res["marine"]["player"]
  marine_plateau = res["marine"]["plateau"]

  victor = res["victor"]["player"]
  victor_plateau = res["victor"]["plateau"]
  ```
As you can see, the last 5 lines of code here are not strictly necessary, as all this information is accessible in ```res```, however, it becomes very handy in the course of the game.

### 2. Instantiate the cards you want to put on Plateau
NB: Make sure to instantiate the Tree as well.
Example:
  ```
  chene = Chêne()

  geai_foug = Card(up_down=True)
  geai_foug.up = GeaiDesChênes("vert clair")
  geai_foug.down = FougèreArborescente("orange")

  paon_crapaud = Card(up_down=True)
  paon_crapaud.up = PaonDuJour("jaune")
  paon_crapaud.down = CrapaudCommun("vert foncé")

  blair_moust = Card(left_right=True)
  blair_moust.left = BlaireauEuropéen("orange")
  blair_moust.right = Moustique("marron")

  barbas_fouine = Card(left_right=True)
  barbas_fouine.left = BarbastelleEurope("bleu foncé")
  barbas_fouine.right = Fouine("orange")
  ```
### 3. Place the Tree on Plateau
  ```
  marine_plateau.place_tree(chene) # 0
  ```
  I advise you to keep in mind the index of the trees you place in your Plateau list (useful so as to not mess trees around).

### 4. Place the Tree on Plateau
For each card you want to place above/below/left/right of a Tree, you have to type in this line of code:
  ```
  marine_plateau.place_non_tree_card(geai_foug, on_tree = "chêne", up=True, which_tree_idx=0)
  ```
Here, I stated that on Marine's Plateau, I wanted to place a card I called ```geai_foug``` (mix of ```GeaiDesChênes()``` and ```FougèreArborescente()```) on the tree "chêne", more precisely above (or up) that tree --meaning I have placed a ```GeaiDesChênes()```.
I precised the location, which is to say that among the many "chêne" I may have in my Plateau, I want this ```GeaiDesChênes()```to be placed upon the first one of those "chêne".

If I now were to continue placing other cards on this tree, this would go like:
```
  marine_plateau.place_non_tree_card(paon_crapaud, on_tree = "chêne", down=True, which_tree_idx=0)
  marine_plateau.place_non_tree_card(blair_moust, on_tree = "chêne", left=True, which_tree_idx=0)
  marine_plateau.place_non_tree_card(barbas_fouine, on_tree = "chêne", right=True, which_tree_idx=0)
```

### 5. Calculate the score
To print out the score now, I would need to type in this code (which will never change throughout the course of your game(s)):
  ```
  print(marine_plateau.name, end = "\n\n") # so as to compare your score with some other player and see directly who's who
  marine_plateau.pprint(index=True, only_animals=True, subcategory=True, category=False) # so that you get the descriptive of where you got your points from
  print() # for some clarity on screen
  print(marine_plateau.count_points_animal(res=res, game=game)) # this is the code that interests you particularly, the rest is purely optional
  ```
As of now, and with all these 5 cards placed on my Plateau, this means I would have a score of ```10```points, aka:
- In my Plateau/forest, I have these trees:
```
  0: chêne: geai_des_chênes, crapaud_commun, blaireau_européen, fouine,
```
- The console is otherwise indicating me some information:
```
  You are missing ['bouleau', 'hêtre', 'marronnier_commun', 'sapin_blanc', 'sapin_Douglas', 'tilleul', 'érable'] to have all 8 categories of trees.
  geai_des_chênes += 3 points.
  fouine += 5 points.
  blaireau_européen += 2 points.
```
- And finally, my points:
```
  10
```
