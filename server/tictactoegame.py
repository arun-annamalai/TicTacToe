import numpy as np

class tttgame:

    rows = cols = 3

    def __init__(self):
        self.board = np.full((3,3), '-')

    def clear_board(self):
        self.board.fill('-')

    def mark_board(self, row, col, fill_element):
        self.board[row][col] = fill_element

    def check_game_over(self):
        count = 0

        for row in self.board:
            row_win = all(ele == row[0] and ele != '-' for ele in row)

            if row_win:
                return True, row[0]

        for col in zip(*self.board):
            col_win = all(ele == col[0] and ele != '-' for ele in col)

            if col_win:
                return True, col[0]

        if self.diag_checks():
            return True, self.board[1][1]

        for row in self.board:
            for element in row:
                if element == "-":
                    return False, ''

        return True, 'T'

    def diag_checks(self):
        if self.board[1][1] != '-':
            count1 = 0
            count2 = 0
            for idx in range(self.rows):
                if self.board[idx][idx] != self.board[1][1]:
                    count1 += 1

                if self.board[2-idx][idx] != self.board[1][1]:
                    count2 += 1

            return count1 == 0 or count2 == 0
        else:
            return False

    def to_string(self):
        row1 = self.board[0][0] + ' | ' + self.board[0][1] + ' | ' +  self.board[0][2] + '\n'
        row2 = self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2] + '\n'
        row3 = self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2] + '\n'
        spaces = '_________\n'
        representation = row1 + spaces + row2 + spaces + row3

        return representation