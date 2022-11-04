class Solution(object):
    def reverseVowels(self, s):
        left = 0
        right = len(s) - 1

        s = list(s)

        while left < right:
            if s[left] in 'aeiouAEIOU' and s[right] in 'aeiouAEIOU':
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            elif s[left] not in 'aeiouAEIOU':
                left += 1
            elif s[right] not in 'aeiouAEIOU':
                right -= 1
        return ''.join(s)