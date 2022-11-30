from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        m = Counter(arr)
        return len(set(m.values())) == len(m)