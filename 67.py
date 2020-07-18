class Solution(object):
    def addBinary(self, a, b):
        max_length = max(len(a), len(b))
        result = ''
        carry = 0
        
        a, b = a.zfill(max_length), b.zfill(max_length)
        
        for i in range(max_length-1, -1, -1):
            r = carry
            if a[i] == '1':
                r = r +1
            if b[i] == '1':
                r = r + 1
            
            if (r % 2 == 1):
                result = '1' + result
            else:
                result = '0' + result
                
            carry = 0 if r< 2 else 1
            
        if carry != 0:
            result = '1' + result
            
        return result
        