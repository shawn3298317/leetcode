# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        #dfs
        self.pred = {}
        ret = []
        stack = []
        if root:
            stack.append(root)
        
        while len(stack) != 0:
            node = stack.pop(-1)
            
            if not node.left and not node.right:   
                ret.append(self.backtrace(node, root))
            
            if node.right:
                self.pred[node.right] = node
                stack.append(node.right)
            if node.left:
                self.pred[node.left] = node
                stack.append(node.left)
        return ret
    def backtrace(self, leaf, root):

        n = leaf
        result = "%s" % n.val
        while n != root:
            n = self.pred[n]
            result = "%s->%s" % (n.val, result)
        # print(result)
        return result
            
        
