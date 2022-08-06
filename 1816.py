class Solution(object):
    def truncateSentence(self, s, k):
        x = s.split()
        return " ".join(x[:k])
        
class Solution(object):
    def truncateSentence(self, s, k):
        return " ".join(s.split()[:k])
        