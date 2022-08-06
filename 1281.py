class Solution(object):
    def subtractProductAndSum(self, n):
        nArray = list(str(n))
        mul = 1
        for x in nArray:
            mul = mul * int(x)
        return mul - sum([int(x) for x in nArray])
        