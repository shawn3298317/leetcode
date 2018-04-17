# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i = 0
        dummy = ListNode(None)
        dummy.next = head
        n_start = dummy
        while i < m-1:
            print(n_start.val)
            n_start = n_start.next
            i += 1
        print("start", n_start.val)
        i = 0
        n_end = n_start
        n_stack = []
        while i < n-m+1:
            n_end = n_end.next
            print("in stack", n_end.val)
            n_stack.append(n_end)
            i += 1
        n_end = n_end.next if n_end else n_end
        
        prev_node = n_start
        while len(n_stack) > 0:
            node = n_stack.pop(-1)
            print("node", node.val)
            prev_node.next = node
            prev_node = node
        prev_node.next = n_end
        # print(prev_node.val, prev_node.next.val)
        return dummy.next

class Solution2(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        i = 0
        dummy = ListNode(None)
        dummy.next = head
        n_start = dummy
        while i < m-1:
            print(n_start.val)
            n_start = n_start.next
            i += 1
        # print("start", n_start.val)
        
        
        n_end = n_start.next
        prev_node = None #ListNode("dummy")
        for _ in range(n-m+1):
            next_node = n_end.next
            n_end.next = prev_node
            # print(n_end.val, "->", n_end.next.val)
            prev_node = n_end
            n_end = next_node
        
        n_start.next.next = n_end
        n_start.next = prev_node

        return dummy.next    
