class Solution(object):
    def isHappy(self, n):
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumofSquares(n)
            if n == 1:
                return True
        return False
    
    def sumofSquares(self, n):
        return sum([ int(l)**2 for l in list(str(n))])
        
        