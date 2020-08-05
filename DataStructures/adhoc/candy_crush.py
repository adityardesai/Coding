# https://leetcode.com/problems/candy-crush/
# TC: O((R*C)^2)
# SC: O(1)
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R = len(board)
        C = len(board[0])

        flag = False

        for r in range(R):
            for c in range(C - 2):
                v = abs(board[r][c])
                if v != 0 and v == abs(board[r][c + 1]) and v == abs(
                        board[r][c + 2]):
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -v
                    flag = True

        for c in range(C):
            for r in range(R - 2):
                v = abs(board[r][c])
                if v != 0 and v == abs(board[r + 1][c]) and v == abs(
                        board[r + 2][c]):
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -v
                    flag = True

        for c in range(C):
            end_ptr = R - 1
            for r in range(R - 1, -1, -1):
                if board[r][c] > 0:
                    board[end_ptr][c] = board[r][c]
                    end_ptr -= 1

            for w in range(end_ptr, -1, -1):
                board[w][c] = 0

        if flag:
            return self.candyCrush(board)
        else:
            return board
