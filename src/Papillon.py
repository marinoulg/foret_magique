from Player import Player, Card, Plateau, Game

class Papillon(Card):
    def __init__(self, cost_card, category, subcategory, effect, bonuss, couleur_feuille, player_id):
        super.__init__(cost_card, category, subcategory, effect, bonuss, couleur_feuille, player_id)
        self.category = ["papillon", "insecte"]

    def points(self, player_id):
        how_many = Plateau(player_id).how_many_per_species(self, player_id, subcategory = self.subcategory[0])
        if how_many == 1:
           Player(player_id).puncts += 0
        elif how_many == 2:
           Player(player_id).puncts += 3
        elif how_many == 3:
           Player(player_id).puncts += 6
        elif how_many == 4:
           Player(player_id).puncts += 12
        elif how_many == 5:
           Player(player_id).puncts += 20
        return self

class Grand_mars_changeant(Papillon):
    def __init__(self, category, couleur_feuille):
        super().__init__(category, couleur_feuille)
        self.subcategory = "grand mars changeant"
        self.cost_card = 0
        """
        couleur_feuille peut être : jaune, orange, vert clair
        """

    def effet(self):
        print(f"{self.subcategory} allows you to draw a card.")
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class Paon_du_jour(Papillon):
    def __init__(self, category, couleur_feuille):
        super().__init__(category)
        self.subcategory = "paon-du-jour"
        self.cost_card = 0
        """
        couleur_feuille peut être : jaune, marron, orange
        """

    def effet(self):
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class Morio(Papillon):
    def __init__(self, category, couleur_feuille):
        super().__init__(category, couleur_feuille)
        self.subcategory = "morio"
        self.cost_card = 0
        """
        couleur_feuille peut être : orange, rouge
        """

    def effet(self):
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class Grande_tortue(Papillon):
    def __init__(self, category, couleur_feuille):
        super().__init__(category, couleur_feuille)
        self.subcategory = "grande tortue"
        """
        couleur_feuille peut être : vert foncé, bleu foncé
        """
        self.cost_card = 0

    def effet(self):
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class Tabac_dEspagne(Papillon):
    def __init__(self, category, couleur_feuille):
        super().__init__(category)
        self.subcategory = "tabac d'Espagne"
        self.cost_card = 0
        """
        couleur_feuille peut être : marron, vert foncé
        """

    def effet(self):
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self
