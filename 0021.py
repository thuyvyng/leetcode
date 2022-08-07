# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        #newHead is what we will return and not change
        #current helps us add to the Node
        newHead = current = ListNode()
        
        #does the comparison between the two lists
        while(list1 and list2):
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        #if one of the lists has stuff left
        current.next = list1 or list2
        
        #bc newHead points to 0
        return newHead.next    