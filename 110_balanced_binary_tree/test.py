# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.depth_map = {}
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return (self.isBalanced(root.left) and self.isBalanced(root.right)) &\
               (abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1)
    
    def getDepth(self, root):
        
        if root in self.depth_map:
            return self.depth_map[root]
        
        if not root:
            self.depth_map[root] = 0
            return 0
        
        l_depth = self.getDepth(root.left)
        r_depth = self.getDepth(root.right)
        cur_depth = max(l_depth, r_depth) + 1
        self.depth_map[root] = cur_depth
        return cur_depth

