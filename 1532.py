class Solution(object):
    def countOdds(self, low, high):
        low = 3
        high = 7
        return (high - low)//2 + 1 + (low % 2 and high % 2)
