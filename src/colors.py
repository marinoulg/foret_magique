from sys import argv

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



print("Choose colour_feuille. \nType 1 for red, 2 for yellow etc.")

print(bcolors.BOLD + bcolors.RED + "1. red")
print(bcolors.BOLD + bcolors.YELLOW + "2. yellow")
print(bcolors.BOLD + bcolors.ORANGE + "3. orange")
print(bcolors.BOLD + bcolors.DARKGREEN + "4. vert foncé")
print(bcolors.BOLD + bcolors.LIGHTGREEN + "5. vert clair")
print(bcolors.BOLD + bcolors.BROWN + "6. marron")
print(bcolors.BOLD + bcolors.LIGHTBLUE + "7. bleu clair")
print(bcolors.BOLD + bcolors.DARKBLUE + "8. bleu foncé" + bcolors.ENDC)
color = input()

if color == "1":
    color = "red"

elif color == "2":
    color = "yellow"

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

print(color)

# print(bcolors.BOLD + bcolors.RED + "1. red/érable")
# print(bcolors.BOLD + bcolors.YELLOW + "2. yellow/tilleul")
# print(bcolors.BOLD + bcolors.ORANGE + "3. orange/marronnier commun")
# print(bcolors.BOLD + bcolors.DARKGREEN + "4. vert foncé/hêtre")
# print(bcolors.BOLD + bcolors.LIGHTGREEN + "5. vert clair/bouleau")
# print(bcolors.BOLD + bcolors.BROWN + "6. marron/chêne")
# print(bcolors.BOLD + bcolors.LIGHTBLUE + "7. bleu clair/sapin douglas")
# print(bcolors.BOLD + bcolors.DARKBLUE + "8. bleu foncé/sapin blanc")
