class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = ','
        x = x.join(operations)
        plus = x.count('++')
        minus = x.count('--') * -1
        return plus + minus