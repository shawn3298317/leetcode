# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
	
	O(n + n) ~ O(n)

        """
        # in-order traverse to sorted list: O(n)
        self.sorted_nums = []
        self.traverse(root)
        
        i = 0
        j = len(self.sorted_nums)-1
        
	# O(n)
        while i < j:
            two_sum = self.sorted_nums[i] + self.sorted_nums[j]
            if two_sum == k and i != j:
                return True
            elif two_sum < k:
                i += 1
            else:
                j -= 1
        return False
        
    
    def traverse(self, node):
        if node.left == None and node.right == None:
            self.sorted_nums.append(node.val)
            return
        if node.left != None:
            self.traverse(node.left)
        self.sorted_nums.append(node.val)
        if node.right != None:
            self.traverse(node.right)
    
        
