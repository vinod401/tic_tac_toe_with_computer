import random


class Game:
    def __init__(self):
        self.line1 = ["⬜️", "️⬜️", "️⬜️"]
        self.line2 = ["⬜️", "️⬜️", "️⬜️"]
        self.line3 = ["⬜️", "️⬜️", "️⬜️"]
        self.map_pic = [self.line1, self.line2, self.line3]
        self.row = 0
        self.column = 0

        # available index to track the remaining index
        self.available_index_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    def display(self):
        """ function to display the matrix """
        for row in self.map_pic:
            print(row)

    def user_input(self):
        """receive the user input and place the character in the matrix"""

        print(f'The available index are{self.available_index_list}')
        user_index = input("Enter the index (row * column) without any special characters (example: 01) :").strip()
        self.row = int(user_index[0])
        self.column = int(user_index[1])

        # placing the character where the specified index by the user only if it is present in
        # the list of available index
        if (self.row, self.column) in self.available_index_list:
            self.place_x_in_map()

        else:
            print(f"{self.row, self.column} is an invalid Index! please check the available index \n")
            self.user_input()

    def update_index(self):
        """updates the available index by removing the used matrix index"""
        self.available_index_list.remove((self.row, self.column))

    def place_o_in_map(self):
        """place the character o in  matrix"""
        print(f"Index taken by computer ({self.row}, {self.column})")
        self.map_pic[self.row][self.column] = 'o'
        self.update_index()

    def place_x_in_map(self):
        """place the character x in the matrix"""
        self.map_pic[self.row][self.column] = 'x'
        self.update_index()

    def user_to_win(self, row, column, diagonal_one, diagonal_two):
        """checks whether the user is about to win and update the row and column that should be blocked"""
        if len(diagonal_one) == 1 and diagonal_one[0] in self.available_index_list:
            self.row = diagonal_one[0][0]
            self.column = diagonal_one[0][1]

            return True

        elif len(diagonal_two) == 1 and diagonal_one[0] in self.available_index_list:
            self.row = diagonal_two[0][0]
            self.column = diagonal_two[0][1]

            return True

        else:
            for index in self.available_index_list:
                if row.count(index[0]) == 2 or column.count(index[1]) == 2:
                    self.row = index[0]
                    self.column = index[1]

                    return True

    def computer_to_win(self, row, column, diagonal_one, diagonal_two):
        """check if the computer have a winning chance and update the row and column that can make the computer win"""
        if len(diagonal_one) == 1:
            self.row = diagonal_one[0][0]
            self.column = diagonal_one[0][1]

            return True

        elif len(diagonal_two) == 1:
            self.row = diagonal_two[0][0]
            self.column = diagonal_two[0][1]
            return True
        else:
            for index in self.available_index_list:
                if row.count(index[0]) == 2 or column.count(index[1]) == 2:
                    self.row = index[0]
                    self.column = index[1]
                    return True

    def computer_turn(self, computer_row, computer_column):
        """the function will track the previous move of the computer and generate a possible winning index"""

        if len(computer_row) != 0:
            for index_from_list in self.available_index_list:
                if computer_row[-1] == index_from_list[0] or computer_column[-1] == index_from_list[1]:
                    index = index_from_list

        else:
            index = random.choice(self.available_index_list)
        self.row = index[0]
        self.column = index[1]
        self.place_o_in_map()
