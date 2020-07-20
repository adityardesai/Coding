# https://leetcode.com/problems/group-anagrams/
# TC:O(NMlogm)
# SC:O(NM)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        if not strs:
            return result
        anagram_map = dict()

        for string in strs:
            m_string = ''.join(sorted(string))
            if m_string not in anagram_map:
                anagram_map[m_string] = [string]
            else:
                anagram_map[m_string].append(string)

        return anagram_map.values()
