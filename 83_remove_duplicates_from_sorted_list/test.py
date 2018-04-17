# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode("dummy")
        dummy.next = head
        
        n, prev_node = head, dummy
        while n is not None:
            if prev_node.val == n.val:
                # if prev_node != head:
                prev_node.next = n.next
                #prev_node = n.next
                n = n.next
            else:
                prev_node = n
                n = n.next
        prev_node.next = None

        return head
