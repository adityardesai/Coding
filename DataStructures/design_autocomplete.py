# https://leetcode.com/problems/design-search-autocomplete-system
# TC: add: O(k*l) - Need to iterate over l sentences each of avg length k
# TC: input: O(p+q+mlogm) p=sentence formed till now,q=number of nodes and sorting is O(mlogm)

class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.is_end=False
        self.hotness=0
    def get_is_end(self):
        return self.is_end
    def set_is_end(self):
        self.is_end=True
    
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.search_term=""
        self.root=TrieNode()
        
        for i in range(len(sentences)):
            self.add(sentences[i], times[i])
        
        
    def add(self, sentence, hotness):
        node = self.root
        
        for ch in sentence:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        
        node.set_is_end()
        node.hotness=node.hotness-hotness
    
    def dfs(self, node, path, result):
        if node.is_end:
            result.append((node.hotness, path))
        
        for ch in node.children:
            self.dfs(node.children[ch], path+ch, result)
        
    def search(self):
        node=self.root 
        result=list()
        path=""
        
        for ch in self.search_term:
            if ch not in node.children:
                return result
            
            path+=ch
            node=node.children[ch]
        
        self.dfs(node, path, result)
        
        return [item[1] for item in sorted(result)[:3]]
        
        
    def input(self, c: str) -> List[str]:
        if c!='#':
            self.search_term+=c
            return self.search()
        else:
            self.add(self.search_term, 1)
            self.search_term=""
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
