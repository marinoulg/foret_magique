from Player import Card

from Champignon import *
from Oiseau import *
from Plantigrade import *
from Papillon import *
from Amphibien import *
from Insecte import *
from Cervidé import *
from Ongulé import *
from Plant import *
from ChauveSouris import *

all_cards = []

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

print(all_cards)
