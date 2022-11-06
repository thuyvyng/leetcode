class Solution(object):
    def peakIndexInMountainArray(self, arr):
        l = 0
        r = len(arr) - 1
        while (l <= r):
            mid = (l + r) // 2
            if arr[mid] > arr[mid -1] and arr[mid+1] < arr[mid]:
                return mid
            elif arr[mid] < arr[mid+1]:
                l = mid + 1
            elif arr[mid] < arr[mid-1]:
                r = mid -1

        # return l
        
x = Solution()
print(x.peakIndexInMountainArray([3,4,5,1]))
