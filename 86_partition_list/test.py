# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode("dummy")
        dummy.next = head
        
        n = head #dummy.next
        larger_head = None
        larger_tail = None
        prev_node = dummy
        while n is not None:
            next_node = n.next
            if n.val < x:
                prev_node.next = n
                prev_node = n
            else:
                if not larger_head:
                    larger_head = larger_tail = n
                    n.next = None
                else:
                    larger_tail.next = n
                    larger_tail = n
                    n.next = None
            n = next_node
        
        prev_node.next = larger_head
        
        return dummy.next
