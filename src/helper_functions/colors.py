from sys import argv
from src.PossibleColors import PossibleColors

class bcolors:
    DARKBLUE = '\033[94m'
    LIGHTBLUE = '\033[96m'
    LIGHTGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DARKGREEN = '\033[38;5;22m'
    BROWN = '\033[38;5;130m'
    ORANGE = '\033[38;5;208m'
    BOLD = '\033[1m'
    GREY = '\033[2m'
    ENDC = '\033[0m'

def which_color(animal):
    """
    Possible animals are:
    - crapaud
    - salamandre
    - rainette
    - cistude
    - cerf
    - chevreuil
    - daim
    - amanite
    - coulemelle
    - girolle
    - cèpe_bordeaux
    - murin_de_bechstein
    - grand_rhinolophe
    - oreillard_roux
    - barbastelle_europe
    - fourmi
    - luciole
    - lucane
    - moustique
    - xylocope
    - bouvreuilpivoire
    - pinson
    - geai
    - palombes
    - pic_epeiche
    - chouette
    - sanglier
    - marcassin
    - grand_mars
    - paon_du_jour
    - morio
    - grande_tortue
    - tabac_espagne
    - fougère
    - mousse
    - mure
    - fraise_des_bois
    - herisson
    - lièvre
    - fouine
    - loup
    - renard
    - taupe
    - loir
    - ecureuil
    - blaireau
    - lynx
    - raton_laveur
    - ours_brun
    """


    possible_animals = list(PossibleColors().possible_colors.keys())
    if animal not in possible_animals:
        raise ValueError(f"{animal} is not an existing animal.\n Possible animals are {possible_animals}")

    possible_colors = PossibleColors().possible_colors[animal]
    if len(possible_colors) == 1:
        color = possible_colors[0]
        return color

    print(f"Choose colour_feuille for {animal}. \nType 1 for red, 2 for yellow etc.")
    poss_numbers = []
    print(possible_colors)

    for couleur in possible_colors:
        if couleur == "rouge":
            print(bcolors.BOLD + bcolors.RED + "1. red")
            poss_numbers.append("1")
        elif couleur == "jaune":
            print(bcolors.BOLD + bcolors.YELLOW + "2. yellow")
            poss_numbers.append("2")
        elif couleur == "orange":
            print(bcolors.BOLD + bcolors.ORANGE + "3. orange")
            poss_numbers.append("3")
        elif couleur == "vert foncé":
            print(bcolors.BOLD + bcolors.DARKGREEN + "4. vert foncé")
            poss_numbers.append("4")
        elif couleur == "vert clair":
            print(bcolors.BOLD + bcolors.LIGHTGREEN + "5. vert clair")
            poss_numbers.append("5")
        elif couleur == "marron":
            print(bcolors.BOLD + bcolors.BROWN + "6. marron")
            poss_numbers.append("6")
        elif couleur == "bleu clair":
            print(bcolors.BOLD + bcolors.LIGHTBLUE + "7. bleu clair")
            poss_numbers.append("7")
        elif couleur == "bleu foncé":
            print(bcolors.BOLD + bcolors.DARKBLUE + "8. bleu foncé" + bcolors.ENDC)
            poss_numbers.append("8")

    print(bcolors.ENDC)

    color = input()
    if color == "1":
        color = "rouge"
    elif color == "2":
        color = "jaune"
    elif color == "3":
        color = "orange"
    elif color == "4":
        color = "vert foncé"
    elif color == "5":
        color = "vert clair"
    elif color == "6":
        color = "marron"
    elif color == "7":
        color = "bleu clair"
    elif color == "8":
        color = "bleu foncé"
    else:
        print(bcolors.ENDC)
        print(("You typed in an incorrect number."))
        print("Possible colors are", possible_colors, ".\n")

    print(bcolors.ENDC)
    if color not in possible_colors:
        print("You typed in an incorrect number.")
        print("Possible colors are", possible_colors, ".\n")
        color = which_color(animal)

    return color


# colors are:
    # - rouge
    # - jaune
    # - orange
    # - vert foncé
    # - vert clair
    # - marron
    # - bleu clair
    # - bleu foncé
