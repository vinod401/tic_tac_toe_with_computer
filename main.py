import random
from player import Player
from game import Game

# to track the game
exit_game = True
user = Player()
game = Game()

# function to read user input


while exit_game:
    game.display()
    game.user_input()

    user.update_rows_columns_used(game.row, game.column)

    if len(game.available_index_list) == 0:
        exit_game = False



