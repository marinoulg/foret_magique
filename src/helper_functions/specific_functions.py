from collections import defaultdict

def how_many_arbre_subcategory(plateau_qqn_pt_plateau_player,
                               subcategory = "tilleul",
                               print_=False):

    """
    dict_ = plateau_qqn.plateau_player
    """

    num_tilleuls = 0
    for elem in plateau_qqn_pt_plateau_player:
        if elem["arbre"] == subcategory:
                num_tilleuls += 1
    if print_==True:
        print(f" has {num_tilleuls} number of {subcategory}.")
    return num_tilleuls

def who_most_tilleuls(*num_tilleuls):
    for pers in num_tilleuls:
        pass

# def who_most_tilleuls(nb_of_players, player_id, plateau_qqn_pt_arbre):
#     counting_tilleuls = defaultdict(list)

#     for _ in range(nb_of_players):
#         num_tileuls = many_tilleuls()
#         counting_tilleuls[num_tileuls].append(self.player_id)

#     print(counting_tilleuls[max(counting_tilleuls.keys())])

#     if len(counting_tilleuls[max(counting_tilleuls.keys())]) == 1:
#         return list(self.player_id)
#     else:
#         return list(max(counting_tilleuls.keys())) # list all players who have the same maximum number of tilleuls

def how_many_for_one_species(player_id, plateau_qqn_pt_plateau_player, subcategory = "papillon"):

    """
    dict_ = plateau_qqn.plateau_player
    """
    # arbres = ["chêne", "hêtre", "bouleau", "érable", "marronnier commun", "sapin blanc", "sapin Douglas", "tilleul"]

    num_papillons = 0
    for elem in plateau_qqn_pt_plateau_player:
        subdict = elem.values()
        for key in subdict:
            if key == "up":
                if subdict["up"].subcategory == subcategory:
                    num_papillons += 1
    print(f"{player_id} has {num_papillons} number of papillons.")
    return num_papillons

# def card_down_bool(player_id, plateau_qqn_pt_plateau_player):
#     """
#     dict_ = plateau_qqn.plateau_player
#     """
#     return False
