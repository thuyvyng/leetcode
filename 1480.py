class Solution(object):
    def runningSum(self, nums):
        return [sum(nums[:i+1]) for i in range(len(nums))]
        
class Solution(object):
    def runningSum(self, nums):
        result = [];
        count = 0;
        for x in range(len(nums)):
            count = count + nums[x];
            result.append(count)
        return result


class Solution(object):
    def runningSum(self, nums):
        new = []
        for i in range(len(nums)):
            new.append(sum(nums[:i+1]))
        return new

class Solution(object):
    def runningSum(self, nums):
        count = 0
        for i, x in enumerate(nums):
            count = count + x
            nums[i] = count
        return nums

def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] 
        return nums