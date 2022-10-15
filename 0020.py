class Solution(object):
    def isValid(self, s):
        test = list()
        checkDict = {')': '(', ']': '[', '}': '{'}
        
        if len(s) % 2 != 0:
            return False
        
        for x in s:
            if x == '(' or x == '{' or x == '[':
                test.append(x)
            else:
                if len(test) == 0:
                    return False
                popped = test.pop()
                if popped != checkDict[x]:
                    return False

        return len(test) == 0
        
p1 = Solution()
x = p1.isValid(')[')
print(x)