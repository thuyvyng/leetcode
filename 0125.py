class Solution(object):
    def isPalindrome(self, s):
        x = ''.join(x.lower() for x in s if x.isalnum())
        return x == x[::-1]