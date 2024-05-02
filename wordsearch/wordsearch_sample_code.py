'''
SAMPLE CODE TO CREATE A WORDSEARCH
THIS IS JUST ONE WAY OF DOING IT!
'''

import random

GRID_SIZE = 10
WORDS = ["add", "words", "here", "to", "search", "for"]
DIRECTIONS = ["across", "down", "diagonal_up", "diagonal_down"]

def create_empty_grid(grid_size):
    '''
    Creates a list of lists, with the dimensions of grid size e.g. grid_size 3 could create [['','',''],['','',''],['','','']]
    '''
    grid = []
    for i in range(grid_size):
        grid.append([""] * grid_size)
    return grid

def get_coordinate(direction, word, grid_size):
    '''
    Get a random coordinate but only if viable based on direction and word length
    '''
    if direction == "across":
        row_range = (0, grid_size - 1)
        col_range = (0, grid_size - len(word))
    elif direction == "down":
        row_range = (0, grid_size - len(word))
        col_range = (0, grid_size - 1)
    elif direction == "diagonal_up":
        row_range = (len(word) - 1, grid_size - 1)
        col_range = (0, grid_size - len(word))
    elif direction == "diagonal_down":
        row_range = (0, grid_size - len(word))
        col_range = (0, grid_size - len(word))
    random_col = random.randrange(col_range[0], col_range[1] + 1)
    random_row = random.randrange(row_range[0], row_range[1] + 1)
    return random_row, random_col

def place_word(location, direction, word, grid):
    '''
    Add the word to the grid based on the valid start point and direction found
    '''
    row = location[0]
    column = location[1]
    for letter in word:
        element_at_loc = grid[row][column]
        grid[row][column] = letter

        # increment row/column based on direction
        if direction == "across":
            column += 1
        if direction == "down":
            row += 1
        if direction == "diagonal_up":
            row -= 1
            column += 1
        if direction == "diagonal_down":
            row += 1
            column += 1
    return grid

def is_overlap_invalid(location, direction, word, grid):
    '''
    If either there isn't a letter already at location or it's the same letter, return true otherwise false
    '''
    row = location[0]
    column = location[1]
    for letter in word:
        element_at_location = grid[location[0]][location[1]]
        if element_at_location != "" and element_at_location != letter:
            return True
        else:
            # increment row/col based on direction
            if direction == "across":
                column += 1
            if direction == "down":
                row += 1
            if direction == "diagonal_up":
                row -= 1
                column += 1
            if direction == "diagonal_down":
                row += 1
                column += 1
    return False

def fill_grid(grid):
    '''
    Add random letters to the rest of the empty spaces in the grid, once it has the words added
    '''
    new_grid = []
    letters = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
    for row in grid:
        new_row = []
        for element in row:
            if element == "":
                new_row.append(random.choice(letters))
            else:
                new_row.append(element)
        new_grid.append(new_row)
    return new_grid

def print_wordsearch(grid):
    '''
    Take the list/grid version of the wordsearch and print it more nicely, maybe as a string with newlines for each row
    '''
    wordsearch = []
    for row in grid:
        joined_row = "".join(row)
        wordsearch.append(joined_row)
    wordsearch = "\n".join(wordsearch)
    print(wordsearch)
    return wordsearch

def run():
    '''
    Put everything together to make the wordsearch
    '''
    grid = create_empty_grid(GRID_SIZE)
    for word in WORDS:
        invalid_location = True
        while invalid_location:
            direction = random.choice(DIRECTIONS)
            coordinate = get_coordinate(direction, word, GRID_SIZE)
            invalid_location = is_overlap_invalid(coordinate, direction, word, grid)
        grid = place_word(coordinate, direction, word, grid)
    filled_grid = fill_grid(grid)
    wordsearch = print_wordsearch(filled_grid)
    return wordsearch

if __name__ == "__main__":
    run()