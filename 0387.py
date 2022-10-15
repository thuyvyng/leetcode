class Solution(object):
    def firstUniqChar(self, s):
        letterDict = {}
        for i, letter in enumerate(s):
            if letter not in letterDict.keys():
                if s.count(letter) == 1:
                    return i
                else:
                    letterDict[letter] = 1
        return -1