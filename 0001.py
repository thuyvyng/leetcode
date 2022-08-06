#8/3/22 Using Split Array
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nums[i+1:]:
                return [i,nums[i+1:].index(comp) +i +1 ]

# #7/5/20 Using Dictionary
# class Solution(object):
#     def twoSum(self, nums, target):
#         numbers = {}
#         for i in range(len(nums)):
#             comp = target - nums[i]
#             if comp in numbers:
#                 return [numbers[comp], i]
#             numbers[nums[i]] = i

# # Brute Force Solution - 7/5/2020
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if(target == nums[i] + nums[j]):
#                     return [i,j]           

p1 = Solution()
x = p1.twoSum([2,7,11,15],9)
print(x)
