# https://leetcode.com/problems/implement-trie-prefix-tree
# TC:O(M)
# SC:O(M)

class TrieNode:
	
    def __init__(self):
        
        self.children=defaultdict(TrieNode)
        self.is_end=False
    
    def set_is_end(self):
        self.is_end=True
    
    def get_is_end(self):
        return self.is_end
    
    def get(self, ch):
        return self.children.get(ch)
    
    def put(self, ch, node):
        self.children[ch]=node
        
    def contains_key(self, ch):
        return self.children[ch] != None

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self.root
        for c in word:
            if not node.contains_key(c):
                new_node=TrieNode()
                node.put(c, new_node)
            node=node.get(c)
        node.set_is_end()
        
    def searchPrefix(self, word):
        node=self.root
        for c in word:
            if node.get(c):
                node=node.get(c)
            else:
                return None
        return node
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.searchPrefix(word)
        return node != None and node.get_is_end()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.searchPrefix(prefix)
        return node != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
