# ForêtMagique

next steps:
- raise ValueError pour toutes les combinaisons impossibles (TBD)
- tester les méthodes de classes
- implémenter le comptage des points (comment ? avoir une méthode .points() -- not sure)
- deal with colors
- deal with positions
- run scenarios

Done :
- ☑ have all possible existing cards in a list in ```all_cards.py```
- ☑ create all cards and have them actionable and ready to use (e.g., we can put a left/right/up/down card on any Tree)
- ☑ create a module: you need to do ```pip install -e .``` to install it
- ☑ raise ValueError pour toutes les couleurs impossibles
- ☑ add color for the correct couleur_feuille
- ☑ create classes for all possible cards with their adequate information
- ☑ coder les autres cartes restantes (cervidés etc.)
- ☑ check names of class MarineVictor not Marine_victor

question ouverte : que faire pour le déroulement d'une partie ? instancier une carte dès qu'on en tire une nouvelle, ou bien avoir une gross liste qui contienne toutes les cartes, et on randomchoice dedans (sachant que dans tous les cas on va randomchoice/randint etc.) ?
