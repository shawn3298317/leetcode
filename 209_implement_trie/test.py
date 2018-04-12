class Node(object):
    def __init__(self, val, child=None): # need parent pointer?
        self.val = val
        self.child = child if child else {}
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None) # a dummy node as root.

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node_prev = self.root
        # Add one char as a node at a time
        for c in word:
            if c not in node_prev.child:
                node_prev.child[c] = Node(c)
            node_prev = node_prev.child[c]
        # Add leaf node
        node_prev.child["NIL"] = Node("NIL")

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        is_in_trie = True
        
        node = self.root
        for c in word:
            if c not in node.child:
                is_in_trie = False
                break
            else:
                node = node.child[c]
        if is_in_trie:
            is_in_trie = "NIL" in node.child
        
        return is_in_trie

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        is_in_trie = True
        
        node = self.root
        for c in prefix:
            if c not in node.child:
                is_in_trie = False
                break
            else:
                node = node.child[c]
        
        return is_in_trie


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)