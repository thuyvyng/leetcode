class Solution(object):
    def areAlmostEqual(self, s1, s2):
        count = 0

        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count ==2