class Solution(object):
    def squareIsWhite(self, coordinates):
        lettersDict = {"a": 1, "b": 2, "c": 3, "d": 4, "e":5, "f": 6, "g": 7, "h":8}
        return (lettersDict[coordinates[0]] % 2 == 0) != (int(coordinates[1]) % 2 == 0)

class Solution(object):
    def squareIsWhite(self, coordinates):
        lettersDict = {"a": 1, "b": 2, "c": 3, "d": 4, "e":5, "f": 6, "g": 7, "h":8}
        letter = coordinates[0]
        number = coordinates[1]
        l = lettersDict[letter] % 2 == 0
        n = int(number) % 2 == 0
        return (l != n)
        