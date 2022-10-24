class Solution(object):
    def pos_to_char(self, pos):
        return chr(pos + 96)

    def freqAlphabets(self, s):
        for i in range(10, 27):
            s = s.replace(str(i) + '#', self.pos_to_char(i))

        for i in range(1, 10):
            s = s.replace(str(i), self.pos_to_char(i))

        return s
