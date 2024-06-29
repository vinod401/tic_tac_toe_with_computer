import random
from player import Player
from game import Game

user = Player()
computer = Player()


def play_game():

    user.reset_player()
    computer.reset_player()

    new_game = Game()
    new_game.display()
    exit_game = False

    while not exit_game:

        new_game.user_input()
        user.update_rows_columns_used(new_game.row, new_game.column)
        new_game.display()

        if user.player_win():
            new_game.display()
            print("You Win")
            user.score += 1

            exit_game = True

        elif len(new_game.available_index_list) == 0:
            print("Draw !")

            exit_game = True

        elif new_game.computer_to_win(row=computer.rows_used, column=computer.columns_used,
                                      diagonal_one=computer.diagonal_one, diagonal_two=computer.diagonal_two):
            new_game.place_o_in_map()
            computer.update_rows_columns_used(row=new_game.row, column=new_game.column)
            new_game.display()

        elif new_game.user_to_win(row=user.rows_used, column=user.columns_used,
                                  diagonal_one=user.diagonal_one, diagonal_two=user.diagonal_two):
            new_game.place_o_in_map()
            computer.update_rows_columns_used(row=new_game.row, column=new_game.column)
            new_game.display()

        else:
            new_game.computer_turn(computer_row=computer.rows_used, computer_column=computer.columns_used)
            computer.update_rows_columns_used(row=new_game.row, column=new_game.column)
            new_game.display()

        if computer.player_win():
            print("You Lose")
            computer.score += 1
            exit_game = True


while True:
    play_game()
    print(f"Your Score : {user.score}  | Computer Score : {computer.score}")
    if input("Do you want to continue(y/n) : ").strip().lower() == 'n':
        break
