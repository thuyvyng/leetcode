class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        count = 0
        l = len(arr)
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if abs(arr[i] -arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        count = count + 1
        return count
