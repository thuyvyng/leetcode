class Solution(object):
    def heightChecker(self, heights):
        sorted_heights = sorted(heights)
        count = 0;
        for i,j in zip(sorted_heights, heights):
            if (i != j):
                count = count + 1
        return count
        # return len([x for x, y in zip(heights, sorted(heights)) if x != y])