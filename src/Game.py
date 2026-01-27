# from src.helper_functions.game_functions import initialize_game_and_players

class Game:
    def __init__(self, nb_of_players, names=[]):
        self.nb_of_players = nb_of_players
        self.player_ids = []
        self.names = names

#     def initialize_game(self):
#         res, game = initialize_game_and_players(self)
#         return res, game

    def who_max_trees(self, res):
        max_trees = 0
        names = []
        for name in res:
            count = res[name]["plateau"].count_trees_per_player()
            res[name]["count_trees"] = count
            if count >= max_trees:
                max_trees = count
                names.append(name)

        return names
