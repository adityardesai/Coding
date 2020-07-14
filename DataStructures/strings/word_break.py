# https://leetcode.com/problems/word-break/
class Solution:
    def helper_dp(self, s, wordDict):
        """
                         {  isWordBreak[j] == True
                         {          and
        isWordBreak[i] = {   wordDict contain 
                         {   s.sub_string(j,i)
                         {
        http://www.goodtecher.com/leetcode-139-word-break/

        isWordBreak[j] is used to indicate whether the first j characters of 
        the input string is able to break into words that all in the dictionary. 
        Only when isWordBreak[j] = true（first j characters of the input string 
        is word breakable) and s.substring(j, i) is also a word in the wordDict,
        first i characters of s can be word breakable.
        
        TC: O(N^2)
        SC: O(N)
        """
        is_word_break = [False] * (len(s) + 1)
        is_word_break[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if is_word_break[j] == False:
                    print('substring not found ' + s[j:i] + " i : " + str(i) +
                          " j :" + str(j))
                    continue
                if s[j:i] in wordDict:
                    print('substring found ' + s[j:i] + " i : " + str(i) +
                          " j :" + str(j))
                    is_word_break[i] = True
                    break
        return is_word_break[len(s)]

    def helper_brute_force_recursion(self, s, word_set, start):
        """
        Time Limit Exceeded
        TC:O(Exponential)
        """
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and self.helper_brute_force_recursion(
                    s, word_set, end):
                return True
        return False

    def helper_memoization(self, s, word_set, start, cache):
        """
        Time Limit Exceeded
        TC: O(N^2)
        SC: O(N)
        """

        if start == len(s):
            return True

        if cache[start]:
            return cache[start]

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and self.helper_memoization(
                    s, word_set, end, cache):
                cache[start] = True

        return cache[start]

    def helper_bfs(self, s, word_set):
        """
        TC:O(N^2)
        SC:O(N)
        """

        from collections import deque

        m_set = set()
        visited = [False] * len(s)
        queue = deque()
        queue.append(0)

        while queue:
            start = queue.popleft()
            if visited[start] == False:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in word_set:
                        queue.append(end)
                        if end == len(s):
                            return True
                visited[start] = True
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #return self.helper_dp(s, wordDict)
        #return self.helper_brute_force_recursion(s, set(wordDict), start=0)
        #return self.helper_memoization(s, set(wordDict), start=0, cache=[False] * len(s))
        return self.helper_bfs(s, set(wordDict))
