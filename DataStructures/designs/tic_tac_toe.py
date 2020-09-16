class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows=[0]*n
        self.cols=[0]*n
        self.prin_diag=0
        self.sec_diag=0
        self.n=n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player==1:
            add=1
        else:
            add=-1
        
        self.rows[row]+=add
        self.cols[col]+=add
        
        if row==col:
            self.prin_diag+=add
        
        if (row+col)==(self.n - 1):
            self.sec_diag+=add
        
        if (abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n 
            or abs(self.prin_diag) == self.n or abs(self.sec_diag) == self.n) :
            return player
        else:
            return 0
    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
