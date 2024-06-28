import random
from player import Player
from game import Game

# to track the game
exit_game = False
user = Player()
computer = Player()
game = Game()


game.display()

while not exit_game:

    game.user_input()
    user.update_rows_columns_used(game.row, game.column)
    game.display()

    if user.player_win():
        game.display()
        print("You Win")
        user.score += 1
        exit_game = True

    elif len(game.available_index_list) == 0:
        exit_game = True

    else:
        game.computer_turn_easy()
        computer.update_rows_columns_used(game.row, game.column)
        game.display()
        if computer.player_win():
            print("You Lose")
            computer.score += 1
            exit_game = True




