
class Solution(object):
    def removeElements(self, head, val):
        newHead = ListNode(-1)
        newHead.next = head

        curr = newHead

        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next

        return newHead.next