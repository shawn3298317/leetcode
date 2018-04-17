# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        n = head
        prev_node = None
        # null linked list
        #[6], [6,0,6,1], [6,0,6], [6,6,6]
        while n is not None:
            
            if n.val == val: #start, middle, end
                if head == n:
                    head = n.next
                    n = n.next
                else:
                    prev_node.next = n.next
                    n = n.next
            else:
                prev_node = n
                n = n.next
                
                
        return head
