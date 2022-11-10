class Solution(object):
    def kWeakestRows(self, mat, k):
        return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]