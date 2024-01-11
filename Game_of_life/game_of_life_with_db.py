import random
import time
from multi_d_array_to_txt import txt_to_array, array_to_txt


class game_of_life:
    def __init__(self, n=0, write=False, board=[]):
        self.board = board
        self.round = 0
        self.n = n
        self.game_cache = []
        self.write = write
        self.width = 0
        self.height = 0

    def next_round(self):
        new_board = []
        # for row in board, for cell in row
        for row in range(len(self.board)):
            new_board.append([])
            for elem in range(len(self.board[row])):
                new_board[row].append(
                    self.cell_update(self.board[row][elem], row, elem)
                )

        # call cell_update
        self.round += 1
        self.board = new_board.copy()

    def generate_random_board(self, width, height):
        self.width = width
        self.height = height
        for row in range(height):
            self.board.append([])
            for elem in range(width):
                cell_value = 0
                if random.random() > 0.5:
                    cell_value = 1
                self.board[row].append(cell_value)

        pass

    def display(self, brd):
        for elem in brd:
            print(elem)
        print("\n")

    def cell_update(self, cell, row, column, width=0, height=0):
        live_cell_count = 0
        for x in range(column - 1, column + 2):
            for y in range(row - 1, row + 2):
                if (x, y) == (column, row):
                    continue
                try:
                    if self.board[y][x] == 1:
                        live_cell_count += 1
                except:
                    IndexError
        if cell == 0:
            if live_cell_count == 3:
                cell = 1
        elif cell == 1:
            if live_cell_count == 1 or live_cell_count == 0 or live_cell_count > 3:
                cell = 0
        return cell

        # cell is a tuple denotating specific cell
        # live cell with 0 or 1 live neighbors dies
        # live cell with 2 or 3 neighbors stays alive
        # live cell with 3 or more neighbors dies
        # dead cell with exactly 3 live neighbors becomes alive

    def play(self):
        self.generate_random_board(5, 5)
        self.game_cache.append(self.board)
        self.display(self.board)
        for r in range(self.n - 1):
            self.next_round()
            # time.sleep(1)
            self.display(self.board)
            self.game_cache.append(self.board)

        if self.write:
            self.save_game()

    def save_game(self):
        array_to_txt(self.game_cache, (self.n, self.width, self.height))


class game_of_life_playback:
    def __init__(self, game_array):
        self.game_array = game_array
        self.game_of_life = game_of_life()

    def playback(self):
        for elem in self.game_array:
            # print(elem)
            self.game_of_life.display(elem)


# record each state after a round in a database
# create a class that can play back a set of rounds!!

test_board = game_of_life(35, write=True)
test_board.play()
"""replay = game_of_life_playback(
    txt_to_array(
        "/home/mike/repos/Python/Projects/Game_of_life/75487game_of_life_save.txt"
    )
)
replay.playback()"""
