class Player:
    def __init__(self):
        # to track index of used column and rows by the player
        self.rows_used = []
        self.columns_used = []
        # to track the diagonal index of the player
        self.diagonal_one = [(0, 0), (1, 1), (2, 2)]
        self.diagonal_two = [(2, 0), (1, 1), (0, 2)]
        self.score = 0

    def update_rows_columns_used(self, row, column):
        self.rows_used.append(row)
        self.columns_used.append(column)

        # delete from  diagonal list if it is in  the diagonal index
        if (row, column) in self.diagonal_one :
            self.diagonal_one.remove((row, column))

        if (row, column) in self.diagonal_two:
            self.diagonal_two.remove((row, column))

    def update_score(self):
        self.score += 1

    def player_win(self):
        for i in range(0, 3):
            if self.rows_used.count(i) > 2 or self.columns_used.count(i) > 2:
                return True
            elif len(self.diagonal_one) == 0 or len(self.diagonal_two) == 0:
                return True



