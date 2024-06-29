class Player:
    def __init__(self):
        # to track index of used column and rows by the player
        self.rows_used = []
        self.columns_used = []
        # to track the diagonal index of the player
        self.diagonal_one = [(0, 0), (1, 1), (2, 2)]
        self.diagonal_two = [(2, 0), (1, 1), (0, 2)]
        self.row = 0
        self.column = 0
        self.score = 0

    def update_rows_columns_used(self):
        """updates the rows and columns used by the player"""
        self.rows_used.append(self.row)
        self.columns_used.append(self.column)

        # delete from  diagonal list if it is in  the diagonal index
        if (self.row, self.column) in self.diagonal_one:
            self.diagonal_one.remove((self.row, self.column))

        if (self.row, self.column) in self.diagonal_two:
            self.diagonal_two.remove((self.row, self.column))

    def update_score(self):
        """updating the players score"""
        self.score += 1

    def player_win(self):
        """checks whether the player won"""
        for i in range(0, 3):
            if self.rows_used.count(i) > 2 or self.columns_used.count(i) > 2:
                return True
            elif len(self.diagonal_one) == 0 or len(self.diagonal_two) == 0:
                return True

    def user_input(self, available_index_list):
        """receive the user input and place the character in the matrix"""

        print(f'The available index are{available_index_list}')
        user_index = input("Enter the index (row * column) without any special characters (example: 01) :").strip()
        self.row = int(user_index[0])
        self.column = int(user_index[1])

        # placing the character where the specified index by the user only if it is present in
        # the list of available index
        if (self.row, self.column) in available_index_list:
            return True

        else:
            print(f"{self.row, self.column} is an invalid Index! please check the available index \n")
            self.user_input(available_index_list)

    def reset_player(self):

        self.rows_used = []
        self.columns_used = []
        self.diagonal_one = [(0, 0), (1, 1), (2, 2)]
        self.diagonal_two = [(2, 0), (1, 1), (0, 2)]
