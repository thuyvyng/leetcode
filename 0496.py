class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        for i in range(len(nums1)):
            otherIndex = nums2.index(nums1[i])
            for val in nums2[otherIndex + 1:]:
                if val > nums1[i]:
                    nums1[i] = val
                    break
            if nums1[i] == nums2[otherIndex]:
                nums1[i] = -1
        return nums1