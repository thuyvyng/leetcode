class Solution(object):
    def maxSubArray(self, nums):
        maxSum = sum(nums)
        current = 0
        
        for i in range(len(nums)):
            current = current + nums[i]
            maxSum = max(maxSum, current)
            # bc why would we ever wanna be negative, just break up the consecutive then
            if current < 0: 
                current = 0
        return maxSum
        