class Solution(object):
    def findLucky(self, arr):
        arr = sorted(arr, reverse=True)
        count = 0

        for i in range(0, len(arr)):
            if count == 0:
                current = arr[i]
                
            if current == arr[i]:
                count+= 1
            elif current == count:
                print("what")
                return current
            else:
                count = 0
            print(count)
            
        print("--------------------")
        if count == current:
            return current
        return -1

X = Solution()
print(X.findLucky([2,2,2,3,3]))