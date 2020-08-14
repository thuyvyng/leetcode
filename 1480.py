class Solution(object):
    def runningSum(self, nums):
        result = [];
        count = 0;
        for x in range(len(nums)):
            count = count + nums[x];
            result.append(count)
        return result


p1 = Solution();

x = p1.runningSum([1,2,3,4])
print(x)