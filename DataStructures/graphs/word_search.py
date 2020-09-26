"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once.


# https://leetcode.com/problems/word-search
# TC: O(N * 3^L) : N=number of cell and L=length of word to be matched
# SC: O(L)

"""
class Solution:
    def _is_valid(self, board, r, c):
        if r < 0 or c < 0 or r > len(board) - 1 or c > len(board[0]) - 1:
            return False
        return True

    def helper(self, board, r, c, word):
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        if len(word) == 0:
            return True
        if not self._is_valid(board, r, c) or board[r][c] != word[0]:
            return False

        board[r][c] = '#'
        result = False

        for dir in DIRECTIONS:
            n_r = dir[0] + r
            n_c = dir[1] + c
            result = self.helper(board, n_r, n_c, word[1:])
            if result: break

        board[r][c] = word[0]
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:

        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                if self.helper(board, i, j, word):
                    return True
        return False
