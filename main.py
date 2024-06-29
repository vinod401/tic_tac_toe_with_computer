from player import Player
from game import Game
from computer_player import ComputerPlayer

player_one = Player()
computer_player = ComputerPlayer()


def play_game():
    player_one.reset_player()
    computer_player.reset_player()

    new_game = Game()
    new_game.display()
    exit_game = False

    while not exit_game:

        player_one.user_input(available_index_list=new_game.available_index_list)
        new_game.place_x_in_map(row=player_one.row, column=player_one.column)

        player_one.update_rows_columns_used()
        new_game.display()
        print("\n")

        if player_one.player_win():
            new_game.display()
            print("You Win")
            player_one.score += 1

            exit_game = True

        elif len(new_game.available_index_list) == 0:
            print("Draw !")

            exit_game = True

        elif computer_player.computer_to_win(available_index_list=new_game.available_index_list):

            new_game.place_o_in_map(row=computer_player.row, column=computer_player.column)
            computer_player.update_rows_columns_used()
            new_game.display()

        elif computer_player.user_to_win(user_rows=player_one.rows_used, user_columns=player_one.columns_used,
                                         diagonal_one=player_one.diagonal_one, diagonal_two=player_one.diagonal_two,
                                         available_index_list=new_game.available_index_list):
            new_game.place_o_in_map(row=computer_player.row, column=computer_player.column)
            computer_player.update_rows_columns_used()
            new_game.display()

        else:
            computer_player.computer_turn(available_index_list=new_game.available_index_list)
            new_game.place_o_in_map(row=computer_player.row, column=computer_player.column)
            computer_player.update_rows_columns_used()
            new_game.display()

        if computer_player.player_win():
            print("You Lose")
            computer_player.score += 1
            exit_game = True


while True:
    play_game()
    print(f"Your Score : {player_one.score}  | Computer Score : {computer_player.score}")
    if input("Do you want to continue(y/n) : ").strip().lower() == 'n':
        break
