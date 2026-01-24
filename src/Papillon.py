from src.Player import Player, ElementsAnimal, Plateau, Game

class Papillon(ElementsAnimal):
    def __init__(self, couleur_feuille):
        self.couleur_feuille = couleur_feuille
        self.category = ["papillon", "insecte"]

    def points(self):
        # how_many = Plateau().how_many_per_species(self, subcategory = self.subcategory[0])
        # if how_many == 1:
        #    Player(player_id).puncts += 0
        # elif how_many == 2:
        #    Player(player_id).puncts += 3
        # elif how_many == 3:
        #    Player(player_id).puncts += 6
        # elif how_many == 4:
        #    Player(player_id).puncts += 12
        # elif how_many == 5:
        #    Player(player_id).puncts += 20
        return self

class GrandMarsChangeant(Papillon):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
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

class PaonDuJour(Papillon):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
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
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
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

class GrandeTortue(Papillon):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
        self.subcategory = "grande tortue"
        """
        couleur_feuille peut être : vert foncé, bleu foncé, rouge
        """
        self.cost_card = 0

    def effet(self):
        return self

    def bonus(self):
        print(f"{self.subcategory} has no bonus.")
        return self

class TabacEspagne(Papillon):
    def __init__(self, couleur_feuille):
        super().__init__(couleur_feuille)
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
