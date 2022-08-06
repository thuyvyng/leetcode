class Solution(object):
    def mostWordsFound(self, sentences):
        count = 0
        for sentence in sentences:
            spaces = sentence.count(' ') + 1
            if spaces > count:
                count = spaces
                
        return count
        

class Solution(object):
    def mostWordsFound(self, sentences):
         return max(sentence.count(" ") for sentence in sentences)+1
