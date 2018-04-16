# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class PriorityQueue(object):
    def __init__(self):
        self.heap = []
    
    def insert(self, node): # O(logk)
        self.heap.append(node)
        self.min_heapify_leaf(len(self.heap)-1)
        # self.print_heap()
    
    def extract_min(self): # O(logk)
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ret = self.heap.pop(-1)
        self.min_heapify_root(0)
        return ret
        
    def min_heapify_root(self, root):
        
        if len(self.heap) == 0: return
        
        l_idx = root*2 + 1
        r_idx = root*2 + 2
        min_idx, min_val = root, self.heap[root].val
        
        if l_idx < len(self.heap) and self.heap[l_idx].val < min_val:
            min_idx, min_val = l_idx, self.heap[l_idx].val
            
        if r_idx < len(self.heap) and self.heap[r_idx].val < min_val:
            min_idx, min_val = r_idx, self.heap[r_idx].val
            
        if min_idx != root:
            self.heap[root], self.heap[min_idx] = self.heap[min_idx], self.heap[root]
            self.min_heapify_root(min_idx)
            
    def min_heapify_leaf(self, leaf):
        p_idx = max(leaf-1, 0) // 2
        
        if leaf <= 0:
            return
        
        if self.heap[p_idx].val > self.heap[leaf].val:
            self.heap[p_idx], self.heap[leaf] = self.heap[leaf], self.heap[p_idx]
            self.min_heapify_leaf(p_idx)

    def print_heap(self):
        print([n.val for n in self.heap])
        
    def is_empty(self):
        return len(self.heap) == 0
        

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        p_queue = PriorityQueue()
        to_ret = None
        last = None
        while not (self.is_empty(lists) and p_queue.is_empty()):
            
            for i, l in enumerate(lists):
                if not l: # all popped out.
                    continue
                else:
                    p_queue.insert(l)
                    lists[i] = l.next
            min_k = p_queue.extract_min()
            min_k.next = None
            # update linkage
            if to_ret is None:
                to_ret, last = min_k, min_k
            else:
                
                last.next, last = min_k, min_k
                # print(to_ret, to_ret.next)
        return to_ret

    def is_empty(self, lists):
        empty = True
        for l in lists:
            if l:
                return False
        return empty
                