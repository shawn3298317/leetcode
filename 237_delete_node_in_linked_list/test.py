# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        n = node
        while n is not None:
            
            n.val = n.next.val
            if n.next.next == None:
                n.next = None
            n = n.next
            
            
