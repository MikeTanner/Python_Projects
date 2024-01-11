import random


class game_of_life:
    def __init__(self, n):
        self.board = []
        self.round = 0
        self.n = n
        pass

    def next_round(self):
        # for row in board, for cell in row
        for row in range(len(self.board)):
            for elem in range(len(self.board[row])):
                self.cell_update(self.board[row][elem], row, elem)
        # call cell_update
        self.round += 1
        pass

    def generate_random_board(self, width, height):
        for row in range(height):
            self.board.append([])
            for elem in range(width):
                cell_value = 0
                if random.random() > 0.5:
                    cell_value = 1
                self.board[row].append(cell_value)

        pass

    def display(self):
        for elem in self.board:
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
                self.board[row][column] = 1
        if cell == 1:
            if live_cell_count == 1 or live_cell_count == 0 or live_cell_count > 3:
                self.board[row][column] = 0

        # cell is a tuple denotating specific cell
        # live cell with 0 or 1 live neighbors dies
        # live cell with 2 or 3 neighbors stays alive
        # live cell with 3 or more neighbors dies
        # dead cell with exactly 3 live neighbors becomes alive

    def main(self):
        # loop n times next_round
        self.cell_update(self.board[2][1], 2, 1)
        pass


# record each state after a round in a database
# create a class that can play back a set of rounds!!

test_board = game_of_life(2)
test_board.generate_random_board(5, 5)
test_board.display()
test_board.next_round()
test_board.display()
