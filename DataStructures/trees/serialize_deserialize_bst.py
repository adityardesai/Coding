# How to use BST property?
# https://leetcode.com/problems/serialize-and-deserialize-bst/
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize_dfs_helper(self, root, result):
        if not root:
            result.append('#')
            return result
        
        result.append(str(root.val) + ',')
        root.left=self.serialize_dfs_helper(root.left, result)
        root.right=self.serialize_dfs_helper(root.right, result)
        

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        result=list()
        self.serialize_dfs_helper(root, result)
        return result

    def deserialize_dfs_helper(self, data):
        
        if data[0] is '#':
            data.pop(0)
            return None
        
        root = TreeNode(data[0].strip(','))
        data.pop(0)
        root.left=self.deserialize_dfs_helper(data)
        root.right=self.deserialize_dfs_helper(data)
        return root
        
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        return self.deserialize_dfs_helper(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
