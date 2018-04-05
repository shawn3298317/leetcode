class D_Node(object):
    
    def __init__(self, key, val, n_next, n_prev=None):
        self.key = key
        self.val = val
        self.next = n_next        
        self.prev = n_prev
        
        # create self.next's linkage
        self.next.prev = self
        # create self.prev's linkage
        if n_prev:
            self.prev.next = self
        
        
class D_List(object):
    
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    
    # Don't support length operation.
        
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity # assume capacity > 1
        # self.nil_node = D_Node("NIL", None)
        self.d_list = D_List(None, None)
        self.node_map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_map: return -1
        
        get_node = self.node_map[key]
        
        # update get_node's neighbor's linkage
        if get_node.prev: # already at head?
            get_node.prev.next = get_node.next
        if get_node.next: # already at tail?
            get_node.next.prev = get_node.prev
            
        # update get_node's linkage
        get_node.prev = None
        get_node.next = self.d_list.head
        self.d_list.head = get_node
        
        return get_node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # duplicates
        if key in self.node_map: return
        
        new_node = D_Node(key, value, self.d_list[0])
        self.d_list.head = new_node
        self.d_list.tail = new_node if len(node_map) == 0 else self.d_list.tail
        self.node_map[key] = new_node
        
        if self.is_cache_full(): # careful capacity == 1?
            # del ref at node_map
            del self.node_map[self.d_list.tail.key]
            # pop the tail and update linkage
            self.d_list.tail = self.d_list.tail.prev
            self.d_list.tail.next = None
            
    def is_cache_full(self):
        return not len(node_map) < self.capacity


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
