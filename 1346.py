class Solution(object):
    def checkIfExist(self, arr):
        check = set()

        for x in arr:
            if  x * 2 in check or x % 2 == 0 and x // 2 in check:
                return True
            check.add(x)
        return False               