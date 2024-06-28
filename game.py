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
        print(f'The available index are{self.available_index_list}')
        user_index = input("Enter the index (row * column) without any special characters (example: 01) :").strip()
        self.row = int(user_index[0])
        self.column = int(user_index[1])

        # placing the character where the specified index by the user only if it is present in
        # the list of available index
        if (self.row, self.column) in self.available_index_list:
            self.map_pic[self.row][self.column] = 'x'
            self.update_index()

        else:
            print(f"{self.row, self.column} is an invalid Index! please check the available index \n")

    def update_index(self):
        self.available_index_list.remove((self.row, self.column))

    def computer_turn_easy(self):
        index = random.choice(self.available_index_list)
        self.row = index[0]
        self.column = index[1]
        self.map_pic[self.row][self.column] = 'o'
        self.update_index()
