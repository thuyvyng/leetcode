class Solution(object):
    def maxRepeating(self, sequence, word):
        # largest k it could be
        k = sequence.count(word)

        while True:
            if word * k in sequence:
                return k
            k -= 1

# class Solution(object):
#     def maxRepeating(self, sequence, word):
#         # largest k it could be
#         k = len(sequence) // len(word)

#         while True:
#             if word * k in sequence:
#                 return k
#             k -= 1