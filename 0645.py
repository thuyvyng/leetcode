class Solution(object):
    def findErrorNums(self, nums):
        n, a, b = len(nums), sum(nums), sum(set(nums))
		
        #math equation for summation from 1 to N
        s = n*(n+1)//2
        
        return [a-b, s-b]