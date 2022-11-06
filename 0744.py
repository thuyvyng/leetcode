class Solution(object):
    def nextGreatestLetter(self, letters, target):
        def search(x):
            l = 0
            r = len(letters) - 1
            while l <= r:
                mid = (l+r) //2
                print(mid)

                if letters[mid] == x:
                    l = mid + 1
                elif letters[mid] > x:
                    r = mid - 1
                else:
                    l = mid + 1
            return l


        i = search(target)
        return i if i < len(letters) else letters[0]

x = Solution()
x.nextGreatestLetter(['x', 'x', 'y', 'y', 'y'], 'z')