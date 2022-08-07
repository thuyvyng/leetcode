class Solution(object):
    def average(self, salary):
        return sum(sorted(salary)[1:-1]) *1.0 / (len(salary)-2)