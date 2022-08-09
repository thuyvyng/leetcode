class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t): return False

        isoCheck = {}
        for x in range(len(s)):
            if s[x] not in isoCheck:
                if t[x] in isoCheck.values():
                    return False
                isoCheck[s[x]] = t[x]
            else: 
                if t[x] != isoCheck[s[x]]:
                    return False
        return True
            
            