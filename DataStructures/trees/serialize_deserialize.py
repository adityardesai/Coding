# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def dfs_serialize_helper(self, root, result):

        if root is None:
            result.append('None,')
            return result

        result.append(str(root.val) + ',')
        result = self.dfs_serialize_helper(root.left, result)
        result = self.dfs_serialize_helper(root.right, result)
        return result

    def bfs_serialize_helper(self, root, result):

        if not root:
            return []

        from collections import deque

        queue = collections.deque()
        queue.append(root)

        while queue:
            x = queue.popleft()
            if not x:
                result.append('None,')
                continue
            result.append(str(x.val) + ',')
            queue.append(x.left)
            queue.append(x.right)

        return result

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        """
        The following is the DFS based solution 
        """
        result = list()
        r = self.dfs_serialize_helper(root, result)
        return ''.join(result)
        """
        The following is the BFS based solution
        """
        #result = list()
        #result = self.bfs_serialize_helper(root, result)
        #return ''.join(result)

    def deserailize_dfs_helper(self, data):

        if data[0] == 'None':
            data.pop(0)
            return None

        root = TreeNode(data[0])
        data.pop(0)
        root.left = self.deserailize_dfs_helper(data)
        root.right = self.deserailize_dfs_helper(data)

        return root

    def deserailize_bfs_helper(self, data):
        from collections import deque

        if not data:
            return None

        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = deque()
        queue.append(root)

        i = 1
        while queue:
            x = queue.popleft()
            if data[i] != 'None':
                left = TreeNode(int(data[i]))
                x.left = left
                queue.append(left)
            i += 1
            if data[i] != 'None':
                right = TreeNode(int(data[i]))
                x.right = right
                queue.append(right)
            i += 1
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        """
        The following is the DFS based solution
        """
        data = data.split(',')
        root = self.deserailize_dfs_helper(data)
        return root
        """
        The following is the BFS based solution
        """

        #result = self.deserailize_bfs_helper(data)
        #return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
