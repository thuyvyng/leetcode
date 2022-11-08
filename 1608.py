class Solution:
    def specialArray(self, nums):
        left, right = 0, len(nums)
        
        while left <= right:
            mid = (left + right) // 2
            check = sum([1 for x in nums if x >= mid])
            if mid == check:
                return check
            elif mid < check:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1