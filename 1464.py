class Solution(object):
    def maxProduct(self, nums):
        a, b = sorted(nums)[-2:]
        return (a-1) * (b-1)