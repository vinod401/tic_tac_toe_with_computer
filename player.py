class Player:
    def __init__(self):
        # to track index of used column and rows by the player
        self.rows_used = []
        self.columns_used = []
        self.score = 0

    def update_rows_columns_used(self, row, column):
        self.rows_used.append(row)
        self.columns_used.append(column)

    def update_score(self):
        self.score += 1



