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


# function to read user input
def user_input():
    print(f'The available index are{available_index_list}')
    user_index = input("Enter the index (row * column) without any special characters (example: 01) :").strip()
    row = int(user_index[0])
    column = int(user_index[1])

    # saving the row and column index to track the progress
    user_row.append(row)
    user_column.append(column)

    # placing the character where the specified index by the user only if it is present in
    # the list of available index
    if (row, column) in available_index_list:
        map_pic[row][column] = 'x'
        available_index_list.remove((row, column))
    else:
        print(f"{row, column} is an invalid Index! please check the available index \n")




