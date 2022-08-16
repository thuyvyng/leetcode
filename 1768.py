class Solution(object):
    def mergeAlternately(self, word1, word2):
        word =''
        for a,b in zip(word1,word2):
            word = word + a + b
            
        if len(word1) > len(word2):
            word = word + word1[len(word2):]
        else:
            word = word + word2[len(word1):]
            
        return word
        
class Solution(object):
    def mergeAlternately(self, word1, word2):
        word =''
        n = min(len(word1),len(word2))
        for a,b in zip(word1,word2):
            word = word + a + b
            
        return word + word1[n:] + word2[n:]
        