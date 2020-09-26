"""

Based on sametree logic

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

TC: O(N*M)
SC: O(N)
"""

class Solution(object):
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and not root2:
            return False
        
        if root2 and not root1:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
    
    def recursive_helper(self, s, t):
        if not s:
            return False

        if s.val == t.val and self.sameTree(s, t):
            return True

        return self.recursive_helper(s.left, t) or self.recursive_helper(s.right, t)

    def isSubtree(self, a, b):
        if not b:
            return True
        return self.recursive_helper(a, b)
