class Solution(object):
    def maxProduct(self, nums):
        a, b = sorted(nums)[-2:]
        return (a-1) * (b-1)


class Solution(object):
    def maxProduct(self, nums):
        numsSorted = sorted(nums)
        return (numsSorted[-1] -1) * (numsSorted[-2] -1)