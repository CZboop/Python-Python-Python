'''
STARTER CODE TO CREATE A WORDSEARCH
FILL IN THE REST!
'''

import random

GRID_SIZE = 20
WORDS = ["add", "words", "here"]
DIRECTIONS = ["across", "down", "diagonal_up", "diagonal_down"]

def create_empty_grid(grid_size):
    '''
    Creates a list of lists, with the dimensions of grid size e.g. grid_size 3 could create [['','',''],['','',''],['','','']]
    '''
    # TODO: ...
    return grid

def get_coordinate(direction, word):
    '''
    TODO: get a random coordinate but only if viable based on direction and word length
    '''
    if direction == "across":
        row_range = (0, len(self.grid[0]) - len(word) - 1)
        col_range = (0, len(self.grid))
    elif direction == "down":
        row_range = (0, len(self.grid[0]))
        col_range = (0, len(self.grid) - len(word) - 1)
    elif direction == "diag_up":
        row_range = (0, len(self.grid[0]) - len(word) - 1)
        col_range = (len(self.grid) - len(word), len(self.grid))
    elif direction == "diag_down":
        row_range = (0, len(self.grid[0]) - len(word) - 1)
        col_range = (0, len(self.grid) - len(word) - 1)
    print(col_range)
    print(direction)
    random_col = random.randrange(col_range[0], col_range[1])
    random_row = random.randrange(row_range[0], row_range[1])
    return random_col, random_row

def place_word(location, direction: str, word: str):
    '''
    TODO: add the word to self.grid
    '''
    row = location[0]
    col = location[1]
    for letter in word:
        element_at_loc = self.grid[row][col]
        print(element_at_loc)
        print(row, col)
        self.grid[row][col] = letter
        # increment row/col based on direction
        if direction == "across":
            col += 1
        if direction == "down":
            row += 1
        if direction == "diag_up":
            row -= 1
            col += 1
        if direction == "diag_down":
            row += 1
            col += 1
    return self.grid

def check_overlap(location, direction: str, word: str) -> bool:
    '''
    TODO: if either there isn't a letter already at loc and not the same letter, true else false
    '''
    row = location[0]
    col = location[1]
    for letter in word:
        element_at_loc = self.grid[location[0]][location[1]]
        print(element_at_loc)
        if element_at_loc != "" and element_at_loc != letter:
            return True
        else:
            # increment row/col based on direction
            if direction == "across":
                col += 1
            if direction == "down":
                row += 1
            if direction == "diag_up":
                row -= 1
                col += 1
            if direction == "diag_down":
                row += 1
                col += 1
    return False

def fill_grid(grid):
    '''
    Add random letters to the rest of the empty spaces in the grid, once it has the words added
    '''
    new_grid = []
    for row in grid:
        pass
        # TODO:
    return new_grid

def print_wordsearch(grid):
    '''
    Take the list/grid version of the wordsearch and print it more nicely, maybe as a string with newlines for each row
    '''
    wordsearch = ""
    for row in grid:
        pass
        # TODO: 
    return wordsearch

def run():
    '''
    Put everything together to make the wordsearch
    '''
    for word in WORDS:
        print(word)
    return "???"

if __name__ == "__main__":
    run()