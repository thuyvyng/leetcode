class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[1] - arr[0]
        start = arr[0]
        for x in arr[1:]:
            if x != start + diff:
                return False
            start = x
        return True
