#7/5/20 Using Dictionary
class Solution(object):
    def twoSum(self, nums, target):
        numbers = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numbers:
                return [numbers[comp], i]
            numbers[nums[i]] = i

# Brute Force Solution - 7/5/2020

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if(nums[j] == target - nums[i]):
#                     return [i,j]           
#         print("No Solution")