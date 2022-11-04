class Solution(object):
    def isPerfectSquare(self, num):
        l, r = 0, num
        while l <= r:
            mid = (l + r)//2
            lower = mid * mid
            higher = (mid + 1) * (mid+1)
            if lower == num or higher == num:
                return True
            elif num < lower:
                r = mid - 1
            else:
                l = mid + 1
        return False