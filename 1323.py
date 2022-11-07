class Solution(object):
    def maximum69Number (self, num):
        x = list(str(num))
        print(x)
        for i in range(len(x)):
            if x[i] == '6':
                x[i] = '9'
                return int("".join(x))
        return num