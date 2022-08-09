class Solution(object):
    def isSubsequence(self, s, t):
        num = 0 
        if  s == "": 
            return True
        for x in t:
            if s[num] == x:
                num = num + 1
            if num == len(s):
                return True
        return False

p1 = Solution()
x = p1.isSubsequence("acb","ahbgdc")
print(x)
