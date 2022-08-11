class Solution(object):
    def nearestValidPoint(self, x, y, points):
        lowest = 99999
        spot = -1
        for i in range(len(points)):
            a, b = points[i][0], points[i][1]
            if (x == a or y == b):
                val = abs(x-a) + abs(y-b)
                if val < lowest:
                    lowest = val
                    spot = i
        return spot
        