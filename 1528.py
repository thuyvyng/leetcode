class Solution(object):
    def restoreString(self, s, indices):
        shuffled = [0] * len(s)
        for x,y in zip(s, indices):
            shuffled[y] = x
        return "".join(shuffled)