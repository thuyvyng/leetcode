class Solution(object):
    def generate(self, numRows):
        pascal = [[1]]
        for i in range(1, numRows):
            currentRow = [1] + [pascal[i-1][x+1] +pascal[i-1][x]  for x in range(i-1)] + [1]
            pascal.append(currentRow)
        return pascal