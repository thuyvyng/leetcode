class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        return x == int(str(x)[::-1])

p1 = Solution()
x = p1.isPalindrome(-121)
print(x)

        