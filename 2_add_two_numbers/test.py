# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        n1, n2 = l1, l2
        result = None
        carry = 0
        prev_node = None
        while not (n1 == None and n2 == None):
            sums = carry
            if n1:
                sums += n1.val
            if n2:
                sums += n2.val
            carry = sums//10 if sums>=10 else 0

            if not prev_node:
                result = ListNode(sums%10)
                prev_node = result
            else:
                prev_node.next = ListNode(sums%10)
                prev_node = prev_node.next

            n1 = n1.next if n1 else n1
            n2 = n2.next if n2 else n2
        
        # overflow
        if carry == 1:
            prev_node.next = ListNode(carry)
            
        return result
