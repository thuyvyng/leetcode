class Solution(object):
    def findLucky(self, arr):
        arr = sorted(arr, reverse=True)
        print(arr)

        for i,x in enumerate(arr):
            print(i)
            print(x)
            if x == arr[i + arr[x]]:
                return x
        return -1

        # arr = sorted(arr, reverse=True)
        
        # for x in arr:
        #     if arr.count(x) == x:
        #         return x
        # return None

X= Solution();
print(X.findLucky([1,2,2,3,3,3]))