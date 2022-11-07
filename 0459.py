class Solution(object):
    def repeatedSubstringPattern(self, s):
        for x in range(0, len(s) //2):
            if len(s) % (x+1) == 0:
                if s[:x+1] * (len(s) / (x+1)) == s:
                    return True
        return False

x = Solution()
x.repeatedSubstringPattern("abcabcabcabc")