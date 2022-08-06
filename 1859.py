class Solution(object):
    def sortSentence(self, s):
        sSplit = s.split()
        wordPlacement = [int(word[-1]) for word in sSplit]
        words = [word[:-1] for word in sSplit]
        correctSpots = [0]*len(words)
        for index,placement in enumerate(wordPlacement):
            correctSpots[placement-1] = words[index]
        return " ".join(correctSpots)

class Solution(object):
    def sortSentence(self, s):
        sSplit = s.split()
        sSplit.sort(key=lambda x: x[-1])
        return " ".join([word[:-1] for word in sSplit])


        