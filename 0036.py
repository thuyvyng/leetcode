class Solution(object):
    def isValidSudoku(self, board):
        return self.areRowValid(board) and self.areColValid(board) and self.areBoxValid(board)
        
    def areRowValid(self, board):
        for row in board:
            if self.isUnique(row) == False:
                return False
        return True

    def areColValid(self, board):
        for col in zip(*board):
            if not self.isUnique(col):
                return False
        return True

    def areBoxValid(self, board):
        for i in (0, 3, 6):
            for j in (0,3,6):
                box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isUnique(box):
                    return False
        return True

    def isUnique(self, nums):
        num = [i for i in nums if i != '.']
        return len(set(num)) == len(num)
