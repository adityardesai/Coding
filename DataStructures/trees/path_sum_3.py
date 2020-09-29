"""
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

TC: O(N)
SC: O(N)

https://leetcode.com/problems/path-sum-iii/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=0

    def pre_order_helper(self, node, k, cummulative, hash_map):
        """
        similar to prefix sum
        https://leetcode.com/articles/subarray-sum-equals-k/
        """
        if not node:
            return 
        
        cummulative+=node.val # sum_so_far
        new_sum=cummulative-k 
        
        self.count+=hash_map.get(new_sum, 0)
        
        hash_map[cummulative] = hash_map.get(cummulative,0)+1 # Add
        
        self.pre_order_helper(node.left, k, cummulative, hash_map)
        self.pre_order_helper(node.right, k, cummulative, hash_map)
        
        hash_map[cummulative] -=1 # Remove, backtrack
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        cummulative=0
        hash_map=dict()
        hash_map[0]=1
        self.pre_order_helper(root,sum, cummulative, hash_map)
        return self.count
