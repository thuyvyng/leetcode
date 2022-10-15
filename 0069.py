class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            lower = mid * mid
            higher = (mid + 1) * (mid+1)
            if lower <= x < higher:
                return mid
            elif x < lower:
                r = mid - 1
            else:
                l = mid + 1