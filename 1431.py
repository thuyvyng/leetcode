class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        final = []
        kidWithMost = max(candies)
        for kid in candies:
            if (kid + extraCandies) >= kidWithMost:
                final.append(True)
            else:
                final.append(False)
        return final


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        kidWithMost = max(candies)
        return [(kid + extraCandies >= kidWithMost ) for kid in candies]


p1 = Solution()
x = p1.kidsWithCandies([2,3,5,1,3],3)
print(x)

        