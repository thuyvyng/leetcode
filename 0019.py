class Solution(object):
    def removeNthFromEnd(self, head, n):
        front = back = head
        for _ in range(n):
            front = front.next
        
        if not front:
            return head.next

        while front.next:
            front = front.next
            back = back.next
        
        back.next = back.next.next
        return head


