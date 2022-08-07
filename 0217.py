class Solution(object):
    def containsDuplicate(self, nums):
        for x in nums:
            if nums.count(x) > 1:
                return True
        return False
        

class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) == len(set(nums))
        
class Solution(object):
    def containsDuplicate(self, nums):
        check = {}
        for x in nums:
            if x in check:
                return True
            check[x] = 1
        return False
        