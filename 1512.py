class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count = count +1                 
        return count


class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)-1):
            if nums[i] in nums[i+1]:
                count += nums[i+1].count(nums[i])               
        return count
                    
                
        