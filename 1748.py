class Solution(object):
    def sumOfUnique(self, nums):
        d = {x:nums.count(x) for x in nums}
        unique = []
        for key,val in d.items():
            if val == 1:
                unique = unique + [key]
        return sum(unique)
        
class Solution:
    def sumOfUnique(self, nums):
        sum=0
        for i in nums:
            if nums.count(i)==1:
                sum = sum + i
        return sum