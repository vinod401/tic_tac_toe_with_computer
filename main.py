import random

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "️⬜️", "️⬜️"]
line3 = ["⬜️", "️⬜️", "️⬜️"]
map_pic = [line1, line2, line3]

# available index to track the remaining index
available_index_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# user rows and user column to track index of user choices
user_row = []
user_column = []

# computer rows and user column to track index of computer choices
computer_row = []
computer_column = []

# to track the game
game_on = True


# function to display the matrix
def display():
    for row in map_pic:
        print(row)


display()