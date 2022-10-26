class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        color = image[sr][sc]

        if color == newColor: return image

        def fill(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    fill(r - 1, c)
                if r + 1 < rows:
                    fill(r + 1, c)
                if c >= 1:
                    fill(r, c - 1)
                if c + 1 < cols:
                    fill(r, c + 1)


        fill(sr, sc)
        return image