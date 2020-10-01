# https://leetcode.com/problems/design-search-autocomplete-system
# TC: add: O(k*l) - Need to iterate over l sentences each of avg length k
# TC: input: O(p+q+mlogm) p=sentence formed till now,q=number of nodes and sorting is O(mlogm)

"""
# 1. add historical data
# 2. for each character in sentence
# 3. when last character is added, make node.isEnd = True indicate that the current node is end of the sentence
# 4. decrement hotness -= because by negating, we can sort as ascending order later.

Ref: https://leetcode.com/problems/design-search-autocomplete-system/discuss/460803/Python-Trie-Solution-easy-to-understand-with-explanation

"""

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
        # 8. Check if node is end of the sentence
        # if so, add path to res
        if node.is_end:
            # 9. when add to res, we also want to add hot for sorting
            result.append((node.hotness, path))
        # 10. keep going if the node has child
        # until there is no more child (reached to bottom)
        for ch in node.children:
            self.dfs(node.children[ch], path+ch, result)
        
    def search(self):
        node=self.root 
        result=list()
        path=""
        
        for ch in self.search_term:
            if ch not in node.children:
                return result
            # 6. add each character to path variable, path will added to res when we found node.isEnd ==True
            path+=ch
            node=node.children[ch]
        
        # 7. at this point, node is at the given searchTerm.
        # for ex. if search term is "i_a", we are at "a" node.
        # from this point, we need to search all the possible sentence by using DFS
        self.dfs(node, path, result)
        
        # 11. variable res has result of all the relevant sentences
        # we just need to do sort and return [1] element of first 3
        return [item[1] for item in sorted(result)[:3]]
        
        
    def input(self, c: str) -> List[str]:
        if c!='#':
            # 5. if input is not "#" add c to self.searchTerm and do self.search each time
            self.search_term+=c
            return self.search()
        else:
            self.add(self.search_term, 1)
            self.search_term=""
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
