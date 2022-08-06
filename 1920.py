class Solution(object):
    def buildArray(self, nums):
        return [ nums[nums[x]] for x in range(len(nums))]
        