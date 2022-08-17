class Solution(object):
    def findTheDifference(self, s, t):
        s = sorted(list(s))
        t = sorted(list(t))
        for x in range(len(s)):
            if s[x] != t[x]:
                return t[x]
        return t[-1]
        