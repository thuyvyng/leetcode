class Solution(object):
    def plusOne(self, digits):
        digitString = int(''.join(map(str,digits))) + 1
        return [int(x) for x in str(digitString)]
        