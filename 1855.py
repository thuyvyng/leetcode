class Solution(object):
    def maxDistance(self, nums1, nums2):
        i = j = res = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res