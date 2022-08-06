class Solution(object):
    def minimumSum(self, num):
        numArray = sorted(list(str(num)))
        return int(numArray[0] + numArray[2]) + int(numArray[1] + numArray[3])