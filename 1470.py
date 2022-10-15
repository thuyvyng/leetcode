# class Solution(object):
#     def shuffle(self, nums, n):
#         arr = []
#         for x in range(n):
#             arr.append(nums[x])
#             arr.append(nums[x+n])
#         return arr

class Solution(object):
    def shuffle(self, nums, n):
        arr = []
        for a , b in zip(nums[:n], nums):
            arr.append(a)
            arr.append(b)
        return arr