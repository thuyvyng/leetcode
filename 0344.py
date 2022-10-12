class Solution(object):
    def reverseString(self, s):
        for x in range(0, len(s)/2):
            s[x], s[-x-1] = s[-x-1], s[x]
        