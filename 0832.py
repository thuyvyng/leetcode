class Solution(object):
    def flipAndInvertImage(self, image):
        return [ [1 -y for y in x[::-1]] for x in image]