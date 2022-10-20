class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        s = 0
        for length in range(0,len(arr), 2):
            for start in range(0, len(arr)-length):
                s += sum(arr[start:start+length+1])
        return s 