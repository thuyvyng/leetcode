class Solution(object):
    def arraySign(self, nums):
        total = 1
        for x in nums:
            if x == 0:
                return 0
            total = total * x
        return 1 if total > 0 else -1
        

class Solution(object):
    def arraySign(self, nums):
        if nums.count(0) > 0:
            return 0
        neg_numbers = [x for x in nums if x < 0]
        remainder = len(neg_numbers) % 2
        return 1 if remainder == 0 else -1
        
        
        