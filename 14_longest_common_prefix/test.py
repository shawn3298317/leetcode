# How to deal with nested dict??
#
from collections import defaultdict

class Node(object):
    def __init__(self, val, parent, child=None):
        self.val = val
        self.parent = parent
        self.child = dict() if not child else child

    def update_node(self, val):
        if val not in self.child:
            new_node = Node(val, self)
            self.child[val] = self.child.get(val, new_node)
            # print("newnode2", self.child[val].val, self.child[val].child)
        return self.child[val] 

class Trie(object):
        def __init__(self, root):
            self.root = root
        
        def search(self):
            pass

        def insert(self):
            pass

        def draw(self):
            """
            dfs
            """
            stack = []
            stack.append(self.root)
            visited = {}
            while len(stack) != 0:
                node = stack.pop(-1)
                visited[node.val] = True

                for c in node.child:
                    if c not in visited:
                        stack.append(c)
                # if node.val = 

class Solution(object):
    """
    apple
    application
    apples
    
    ans:app
    """

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        trie = Trie(Node(None, None))
        for s in strs:
            node_prev = trie.root
            for c in s:
                node_prev = node_prev.update_node(c)
            node_prev = node_prev.update_node("NIL")
        
        #traverse trie for longest common suffix
        node = trie.root
        suffix = ""
        while len(node.child) == 1 and "NIL" not in node.child:
            next_val = list(node.child.keys())[0]
            # print(next_val)
            if next_val == None:
                break
            suffix += next_val
            node = node.child[next_val]
        
        print(suffix)
        return suffix

s = Solution()
tc = [
    "abcggg",
    "abcfe",
    "abcde"
]
s.longestCommonPrefix(tc)
