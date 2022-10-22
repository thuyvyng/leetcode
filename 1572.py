class Solution(object):
    def diagonalSum(self, mat):
        sum = 0
        for i, row in enumerate(mat):
            if i == len(row)-1-i:
                sum += row[i] 
            else:
                sum += row[i] + row[len(row)-1-i]
        return sum