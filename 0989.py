class Solution(object):
    def addToArrayForm(self, num, k):
        num = map(str, num)
        intV = "".join(num)
        ans = int(intV) + k
        return list(str(ans))