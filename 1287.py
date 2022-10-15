class Solution(object):
    def findSpecialInteger(self, arr):
        limit = len(arr)//4
        index = 0

        while (index + limit ) < len(arr):
            num = arr[index]
            if arr[int(limit + index)] == num:
                return num
            index = index + 1
        
        return arr[index]

class Solution(object):
    def findSpecialInteger(self, arr):
        limit = len(arr)//4
        
        for x in arr:
            if arr.count(x) > limit:
                return x
        return arr[0]

class Solution(object):
    def findSpecialInteger(self, arr):
        limit = len(arr)//4
        count = 1
        prev = arr[0]
        
        for x in arr[1:]:
            if x == prev:
                count = count + 1
                if count > limit:
                    return x
            else:
                count = 1
                prev = x
        return prev

X= Solution();
# [1,2,2,6,6,6,6,7,10]
# [1,1]

# Y = X.findSpecialInteger([1,2,3,4,5,6,7,8,9,10,11,12,12,12,12])
# Y = X.findSpecialInteger([1,2,3,3])
Y = X.findSpecialInteger([1])


print("r", Y)