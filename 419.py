class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0;
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == 'X' and (i == len(board)-1 or board[i+1][j] == '.') and (j == len(board[i])-1 or board[i][j+1] == '.'):
                    res = res + 1;
        return res;
