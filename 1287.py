class Solution(object):
    def findSpecialInteger(self, arr):
        limit = len(arr)//4
        count = 0
        
        for x in arr:
            print(x)
            if count == 0:
                current = x
                
            if x == current:
                count = count + 1
                if count > limit:
                    return current
            else:
                count = 0
        return None

X= Solution();
Y = X.findSpecialInteger([1,2,3,4])
print(Y)