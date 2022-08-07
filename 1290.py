class Solution(object):
    def getDecimalValue(self, head):
        current = ''
        while head != None:
            current = current + str(head.val)
            head = head.next
        return int(current,2)
        