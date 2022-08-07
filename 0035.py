# Using Binary Search
class Solution(object):
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        
        try:
            return nums.index(target)
        except:
            return self.binary_search(nums,target)
            
        
    def binary_search(self,arr,target): 
        low = 0
        high = len(arr) - 1
        mid = 0

        while low <= high: 

            mid = (high + low) // 2

            # Check if x is present at mid 
            if arr[mid] < target: 
                low = mid + 1

            # If x is greater, ignore left half 
            elif arr[mid] > target: 
                high = mid - 1

            # If x is smaller, ignore right half 
            else: 
                return mid 

        # If we reach here, then the element was not present
        if target > arr[low]:
            return low + 1
        else:
            return low

# Loop through array
# class Solution(object):
#     def searchInsert(self, nums, target):
#         try:
#             return nums.index(target)
#         except:
#             for x in range(len(nums)):
#                 if (nums[x] >= target):
#                     return x
#             return len(nums)
        
# class Solution(object):
#     def searchInsert(self, nums, target):
#         if target < nums[0]:
#             return 0
#         if target > nums[len(nums)-1]:
#             return len(nums)
        
#         return self.binary_search(nums,target)
            
        
#     def binary_search(self,arr,target): 
#         low = 0
#         high = len(arr) - 1

#         while low <= high: 
#             mid = (high + low) // 2
            
#             if arr[mid] == target:
#                 return mid
#             elif arr[mid] < target: 
#                 low = mid + 1
#             else: 
#                 high = mid - 1

#         # If we reach here, then the element was not present
#         if target > arr[low]:
#             return low + 1
#         return low