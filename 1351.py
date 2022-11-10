class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            count += sum([1 for x in row if x < 0])
        return count
        