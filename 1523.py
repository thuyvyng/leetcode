class Solution(object):
    def countOdds(self, low, high):    
        #if low is odd, we want to count it
        if low % 2 == 1:
            low = low - 1
    
        #if high is odd, we want to count it
        if high % 2 == 1:
            high = high + 1       
        return (high-low)//2