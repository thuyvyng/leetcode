# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         j = set(jewels)

#         count = 0
#         for s in stones:
#             if s in j:
#                 count = count + 1

#         return count

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        return sum([1 for x in stones if x in jewels])