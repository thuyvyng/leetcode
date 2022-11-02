class Solution(object):
    def guessNumber(self, n):
        low = 1
        high = n

        while low <= high:
            mid = (low + high ) //2
            g = guess(mid)
            if g == 0:
                return mid
            if g == 1:
                low = mid + 1
            else:
                high = mid - 1
        return low
                
