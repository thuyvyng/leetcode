class Solution(object):
    def moveZeroes(self, nums):
        zeros = 0
        for x in nums:
            if x == 0:
                zeros += 1

        counter = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[counter] = nums[i]
                counter += 1
        
        for i in range(counter, len(nums)):
            nums[i] = 0