class Solution(object):
    def matrixReshape(self, mat, r, c):
        if len(mat) * len(mat[0]) != r * c:
            return mat

        flat_list = [item for sublist in mat for item in sublist]

        ans = []
        row = []
        for i in range(len(flat_list)):
            row.append(flat_list[i])
            if i % c == c-1:
                ans.append(row)
                row = []
        return ans
