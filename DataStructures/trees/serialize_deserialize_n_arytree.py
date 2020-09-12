# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/ 
# TC: O(N)
# SC: O(N)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Helper:
    def __init__(self, value):
        self.value=value
    def getValue(self):
        return self.value
    def increment(self):
        self.value+=1

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        result=list()
        helper=Helper(1)
        self._serialize_helper(root, result, helper, None)
        return ''.join(result)
	
    def _serialize_helper(self, root, result, identity, parent):
        if not root:
            return
        
        # Own identity
        result.append(chr(identity.getValue()+48))
        
        # Nodes value
        result.append(chr(root.val + 48))

        # Parent information
        result.append(chr(parent + 48) if parent else 'N')
        
        parent=identity.getValue()
        
        for child in root.children:
            identity.increment()
            self._serialize_helper(child, result, identity, parent)
        
        
    def _deserialize_helper(self, data):
        node_and_parents_map = dict()
        
        for i in range(0,len(data), 3):
            node_number = ord(data[i]) - 48
            node_value = ord(data[i+1]) - 48
            parent = ord(data[i+2]) - 48
            node_and_parents_map[node_number] = (parent, Node(node_value,[]))
            
        for i in range(3, len(data), 3):
            node_number = ord(data[i]) - 48
            node = node_and_parents_map[node_number][1]
            
            parent_number = ord(data[i+2]) - 48
            parent_node = node_and_parents_map[parent_number][1]
            
            parent_node.children.append(node)
        
        return node_and_parents_map[ord(data[0]) - 48][1]
            
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        return self._deserialize_helper(data)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
