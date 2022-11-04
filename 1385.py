class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        return sum([1 if all( val > d for val in [abs(x-y) for y in arr2]) else 0 for x in arr1])