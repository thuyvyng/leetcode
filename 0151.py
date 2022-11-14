class Solution(object):
    def reverseWords(self, s):
        spl = s.split()
        return " ".join(spl[::-1])