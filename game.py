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

    def update_index(self):
        """updates the available index by removing the used matrix index"""
        self.available_index_list.remove((self.row, self.column))

    def place_o_in_map(self, row, column):
        """place the character o in  matrix"""
        self.row = row
        self.column = column

        self.map_pic[self.row][self.column] = 'o'
        self.update_index()

    def place_x_in_map(self, row, column):
        """place the character x in the matrix"""

        self.row = row
        self.column = column

        self.map_pic[self.row][self.column] = 'x'
        self.update_index()
