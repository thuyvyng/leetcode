class Solution(object):
    def arrangeCoins(self, n):
        #summation eq: = (n+1)*n //2
        l = 0
        r = n

        while l <= r:
            mid = (l+r) //2
            
            summ = (mid+1) * mid //2

            if summ == n:
                return mid
            elif summ > n:
                r = mid -1
            else:
                l = mid + 1
        return r