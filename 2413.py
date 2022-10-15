class Solution(object):
    def smallestEvenMultiple(self, n):
        current = n
        while True:
            if current % n == 0 and current % 2 == 0:
                return current
            current = current + n
