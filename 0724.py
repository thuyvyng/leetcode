class Solution(object):
    def pivotIndex(self, nums):
        for x in range(len(nums)):
            if sum(nums[:x]) == sum(nums[x+1:]):
                return x
        return -1
        