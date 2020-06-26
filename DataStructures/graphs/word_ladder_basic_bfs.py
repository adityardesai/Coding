# https://leetcode.com/problems/word-ladder/
# TC: O(M^2 * N)
# SC: O(M^2 * N)


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        from collections import deque
        queue = deque()
        queue.append(beginWord)
        result = 1

        while queue:
            size = len(queue)
            for i in range(size):

                cw = queue.popleft()
                cw_list = list(cw)

                for j in range(len(cw_list)):

                    original_char = cw_list[j]

                    for k in range(0, 26):
                        if cw_list[j] == chr(ord('a') + k):
                            continue

                        cw_list[j] = chr(ord('a') + k)
                        new_word = ''.join(cw_list)

                        if new_word == endWord:
                            return result + 1

                        if new_word in word_set:
                            queue.append(new_word)
                            word_set.remove(new_word)

                    # end k loop
                    cw_list[j] = original_char
            # end i loop
            result += 1

        return 0
