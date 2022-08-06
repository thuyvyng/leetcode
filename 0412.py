class Solution(object):
    def fizzyLogic(self, x):
        if (x % 5 == 0 and x % 3 == 0):
            return "FizzBuzz"
        if (x % 5 == 0):
            return "Buzz"
        if (x % 3 == 0):
            return "Fizz"   
        return str(x)
    def fizzBuzz(self, n):
        nArray = [0]*n
        return [ self.fizzyLogic(x+1) for x in range(len(nArray)) ]       