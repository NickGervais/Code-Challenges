from pandas import DataFrame
from typing import List

class Solution:
    length = 9
    empty_char = '.'
    valid_values = set(range(1, 10))
    rows = {i: set() for i in range(length)} # 0-8
    cols = {i: set() for i in range(length)} # 0-8
    boxes = {i: set() for i in range(length)} # 0-8


    def cords_to_box_num(self, x, y):
        box_x = int(x/3)
        box_y = int(y/3)
        return (3 * box_y) + box_x

    def is_cords_valid(self, x, y, val):
        cant_be = self.rows[y].union(self.cols[x], self.boxes[self.cords_to_box_num(x, y)])
        return str(val) not in cant_be

    def add_board_value(self, board, x, y, val):
        val = str(val)
        if self.is_cords_valid(x, y, val):
            self.rows[y].add(val)
            self.cols[x].add(val)
            self.boxes[self.cords_to_box_num(x, y)].add(val)

            board[y][x] = val

            return True
        else:
            return False

    def remove_board_value(self, board, x, y, val):
        val = str(val)
        self.rows[y].remove(val)
        self.cols[x].remove(val)
        self.boxes[self.cords_to_box_num(x, y)].remove(val)

        board[y][x] = str(self.empty_char)
        return True

    def get_empty_spot_cords(self, board):
        spots_to_fill = []
        for y in range(self.length):
            for x in range(self.length):
                if board[y][x] == self.empty_char:
                    spots_to_fill.append((y, x))
        return spots_to_fill

    def load_values(self, board):
        # load rows, cols, boxes
        for y in range(self.length):
            for x in range(self.length):
                val = board[y][x]
                if val != self.empty_char:
                    self.add_board_value(board, x, y, val)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.load_values(board)

        def extend_solution(s, pos):
            y, x = s[pos]
            for i in range(1, self.length + 1):
                if self.is_cords_valid(x, y, i):
                    self.add_board_value(board, x, y, i)

                    if pos >= len(s) - 1 or extend_solution(s, pos+1):
                        return board

                    self.remove_board_value(board, x, y, i)
            return None

        spots_to_fill = self.get_empty_spot_cords(board)

        extend_solution(spots_to_fill, 0)





# a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# print('Input:')
# print(DataFrame(a))
# Solution().solveSudoku(a)
# print('\nSolution:')
# print(DataFrame(a))
#
# print('\n')

b = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print('Input:')
print(DataFrame(b))
Solution().solveSudoku(b)
print('\nSolution:')
print(DataFrame(b))

print('\n')
