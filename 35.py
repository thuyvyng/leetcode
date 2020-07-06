class Solution(object):
    def searchInsert(self, nums, target):
        try:
            return nums.index(target)
        except:
            for x in range(len(nums)):
                if (nums[x] >= target):
                    return x
            return len(nums)
        