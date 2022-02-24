import numpy as np
from random import randrange


# create a cache to store the moves of the players
CACHE = []


def make_position(nb_rows, nb_columns):
    """The function randomly create a position and if this place is free(not in CACHE) takes it"""
    while True:
        pos = (randrange(nb_rows), randrange(nb_columns))
        if pos not in CACHE:
            CACHE.append(pos)
            return pos


def check_free_space(game_field):
    if 0 not in game_field:
        return False
    return True


def check_rows(field, nb_rows):
    """The function checks rows for consecutive numbers"""
    if nb_rows in abs(np.sum(field, axis=0)):
        return True
    return False


def check_columns(field, nb_columns):
    """The function checks columns for consecutive numbers"""
    if nb_columns in abs(np.sum(field, axis=1)):
        return True
    return False


def check_diagonal(field, nb_rows, nb_columns, size_diagonal):
    # check the main diagonal
    if abs(np.trace(field)) == size_diagonal:
        return True
    # check the side diagonal
    count = 0
    for i, k in zip(range(nb_columns), range(nb_rows - 1, -1, -1)):
        count += field[(i, k)]
    if abs(count) == size_diagonal:
        return True
    return False


def check_consecutive_nbs(field):
    """function iterates over the field's lines and columns and checks if there is a sequence of consecutive numbers"""
    # get the number of rows and columns
    rows, columns = field.shape
    size_diagonal = np.diagonal(field).size
    return any([check_rows(field, rows),
                check_columns(field, columns),
                check_diagonal(field, rows, columns, size_diagonal)])


def check_move_result(field, user_type):
    flag = False
    if check_consecutive_nbs(field):
        flag = True
        print(f'{user_type} wins!')
    if not check_free_space(field):
        flag = True
        print('Draw')
    return flag


def display_field(field):
    print(field)
    print()


def main():
    # create a game field
    print("let's create a game's field!")

    while True:
        rows = int(input('Enter the number of lines: '))
        columns = int(input('Enter the number of columns: '))
        if rows == columns:
            break
        print('Error! the number of rows and sides must be the same\n')

    # create the game field
    field = np.zeros((rows, columns))

    # create the game process
    while True:
        # the first player move
        field[make_position(rows, columns)] = 1
        display_field(field)

        # check if the first player wins
        if check_move_result(field, 'first user'):
            break

        # the second player move
        field[make_position(rows, columns)] = -1
        display_field(field)

        # check if the second user win
        if check_move_result(field, 'second user'):
            break

    print(f'The history of operation:\n{CACHE}')


if __name__ == '__main__':
    main()
