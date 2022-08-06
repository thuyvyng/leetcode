class Solution(object):
    def checkIfPangram(self, sentence):
        alpha = {}
        for letter in sentence:
            alpha[letter] = 1
        return len(alpha) == 26
        
class Solution:
    def checkIfPangram(self, sentence):
        return set('abcdefghijklmnopqrstuvwxyz') == set(sentence)


class Solution:
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26