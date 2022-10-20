class Solution(object):
    def searchMatrix(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1

        #find the correct row
        while left <= right:
            med = (left + right) / 2
            val = matrix[med/col][med%col]
            if target == val:
                return True
            elif val < target:
                left = med +1
            else:
                right = med -1

        return False
        