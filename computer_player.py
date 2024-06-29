import random
from player import Player


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()

    def user_to_win(self, user_rows, user_columns, diagonal_one, diagonal_two, available_index_list):
        """checks whether the user is about to win and update the row and column that should be blocked"""

        if len(diagonal_one) == 1 and (diagonal_one[0] in available_index_list):
            self.row = diagonal_one[0][0]
            self.column = diagonal_one[0][1]
            return True

        elif len(diagonal_two) == 1 and (diagonal_two[0] in available_index_list):
            self.row = diagonal_two[0][0]
            self.column = diagonal_two[0][1]
            return True

        else:
            for index in available_index_list:
                if user_rows.count(index[0]) == 2 or user_columns.count(index[1]) == 2:
                    self.row = index[0]
                    self.column = index[1]
                    return True

    def computer_to_win(self, available_index_list):
        """check if the computer have a winning chance and update the row and column that can make the computer win"""
        if len(self.diagonal_one) == 1:
            self.row = self.diagonal_one[0][0]
            self.column = self.diagonal_one[0][1]

            return True

        elif len(self.diagonal_two) == 1:

            self.row = self.diagonal_two[0][0]
            self.column = self.diagonal_two[0][1]

            return True

        else:
            for index in available_index_list:

                if self.rows_used.count(index[0]) == 2 or self.columns_used.count(index[1]) == 2:

                    self.row = index[0]
                    self.column = index[1]

                    return True

    def computer_turn(self, available_index_list):
        """the function will track the previous move of the computer and generate a possible winning index"""
        index = (10, 10)
        if len(self.rows_used) != 0:
            for index_from_list in available_index_list:
                if self.rows_used[-1] == index_from_list[0] or self.columns_used[-1] == index_from_list[1]:
                    index = index_from_list
                    print("this")

        if index not in available_index_list:
            index = random.choice(available_index_list)

        self.row = index[0]
        self.column = index[1]
0
