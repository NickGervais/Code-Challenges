"""
On an 8 x 8 chessboard, there is one white rook.  
    There also may be empty squares, white bishops, and black pawns.  
    These are given as characters 'R', '.', 'B', and 'p' respectively. 
    Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: 
    it chooses one of four cardinal directions (north, east, west, and south), 
    then moves in that direction until it chooses to stop, 
    reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  
    Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Example 1:

Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.


Example 2:

Input: [[".",".",".",".",".",".",".","."],
        [".","p","p","p","p","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","B","R","B","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","p","p","p","p",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.


Example 3:

Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.


Note:

board.length == board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
"""

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        # find rook
        rook_pos = (-1, -1)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'R':
                    rook_pos = (row, col)
                    
        if rook_pos == (-1, -1):
            return False
        
        captures = 0
        
        # go north / south
        cur_pos = [rook_pos, rook_pos, rook_pos, rook_pos]
        increments = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for i in range(len(cur_pos)):
            cur_pos[i] = (increments[i][0] + cur_pos[i][0], increments[i][1] + cur_pos[i][1])
        
        
        still_looking = [True, True, True, True]
        while True in still_looking:
            for i in range(len(cur_pos)):
                if still_looking[i]:
                    row, col = cur_pos[i]
                    if row < 0 or col < 0 or row >= len(board) or col >= len(board):
                        still_looking[i] = False
                    elif board[row][col] == 'p':
                        captures += 1
                        still_looking[i] = False
                    elif board[row][col] == 'B':
                        still_looking[i] = False
                    else:
                        cur_pos[i] = (increments[i][0] + cur_pos[i][0], increments[i][1] + cur_pos[i][1])
        return captures

given = [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
result = Solution().numRookCaptures(given)
print(result)
