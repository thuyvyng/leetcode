class Solution(object):
    def rotate(self, nums, k):
        ugh = k % len(nums)
        nums[:] = nums[-ugh:] + nums[:-ugh]
        
p1 = Solution()
x = p1.rotate([1,2,3,4,5,6,7], 3)
print(x)
print('-----------')
x = p1.rotate([1,2], 3)
print(x)