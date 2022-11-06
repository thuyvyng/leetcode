class Solution(object):
    def searchRange(self, nums, target):
        def search(x):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l+r) //2

                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        
        low = search(target)
        high = search(target + 1) -1
        
        return [low, high] if low <= high else [-1,-1]
        