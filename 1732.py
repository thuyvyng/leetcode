# class Solution(object):
#     def largestAltitude(self, gain):
#         alt = [0]
#         prev = 0

#         for x in gain:
#             alt.append(x + alt[prev])
#             prev += 1
    
#         return max(alt)

class Solution(object):
    def largestAltitude(self, gain):
        alt = 0
        maxAlt = 0

        for x in gain:
            alt += x
            maxAlt = max(maxAlt, alt)
    
        return maxAlt