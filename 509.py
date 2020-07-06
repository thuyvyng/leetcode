#Top Down w/ Memorization
fibs = {0:0, 1:1, 2:1}

class Solution(object):
    def fib(self, N):
        if N not in fibs:
            fibs[N] = fibs[N-1] + fibs[N-2]
        return fibs[N]
        
#Bottom Up
# class Solution(object):
#     def fib(self, N):
#         if N == 0:
#             return 0
#         a, b = 1, 1
#         for i in range(3,N+1):
#             a,b = a+b, a
#         return a
        
# Naive Recursion
# class Solution(object):
#     def fib(self, N):
#         if N <= 1:
#             return N
#         return self.fib(N-1) + self.fib(N-2)