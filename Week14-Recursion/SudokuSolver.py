class SudokuSolver:

    def __init__(self, grid):
        self.grid = grid # 9x9 2d list
        self.solve()

    def _is_unsolved(self):
        for row in self.grid:
            if " " in row:
                return True
        return False

    def _find_next_open_space(self):
        for row_index in range(len(self.grid)):
            for column_index in range(len(self.grid)):
                if self.grid[row_index][column_index] == " ":
                    return row_index, column_index

    def _can_place_number_in_row(self, number, row_index):
        return number not in self.grid[row_index]

    def _can_place_number_in_column(self, number, column_index):
        for row in self.grid:
            if number == row[column_index]:
                return False
        return True

    def _can_place_number_in_square(self, number, row_index, column_index):
        starting_row_index = (row_index // 3) * 3
        starting_column_index = (column_index // 3) * 3

        for row_index in range(starting_row_index, starting_row_index + 3):
            for column_index in range(starting_column_index, starting_column_index + 3):
                if self.grid[row_index][column_index] == number:
                    return False
        return True

    def _can_place_number(self, number, row_index, column_index):
        return self._can_place_number_in_row(number, row_index) \
            and self._can_place_number_in_column(number, column_index) \
            and self._can_place_number_in_square(number, row_index, column_index)

    def solve(self):
        if self._is_unsolved():
            row_index, column_index = self._find_next_open_space()
            for number in range(1, 10):
                number = str(number)
                if self._can_place_number(number, row_index, column_index):
                    self.grid[row_index][column_index] = number
                    self.solve()
                    if self._is_unsolved():
                        self.grid[row_index][column_index] = " "

    def __str__(self):
        return "\n".join(str(row) for row in self.grid)


grid = [
    ['5', '3', ' ', ' ', '7', ' ', ' ', ' ', ' '],
    ['6', ' ', ' ', '1', '9', '5', ' ', ' ', ' '],
    [' ', '9', '8', ' ', ' ', ' ', ' ', '6', ' '],
    ['8', ' ', ' ', ' ', '6', ' ', ' ', ' ', '3'],
    ['4', ' ', ' ', '8', ' ', '3', ' ', ' ', '1'],
    ['7', ' ', ' ', ' ', '2', ' ', ' ', ' ', '6'],
    [' ', '6', ' ', ' ', ' ', ' ', '2', '8', ' '],
    [' ', ' ', ' ', '4', '1', '9', ' ', ' ', '5'],
    [' ', ' ', ' ', ' ', '8', ' ', ' ', '7', '9']
]

puzzle = SudokuSolver(grid)
print(puzzle)