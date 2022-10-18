class Solution(object):
    def tribonacci(self, n):
        memo = {0:0,1:1,2:1}
        for i in range(3,n+1):
            memo[i] = memo[i-2] + memo[i-1] +memo[i-3]
        return memo[n]