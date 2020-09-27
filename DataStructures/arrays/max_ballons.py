"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

TC:O(N)
SC:O(1) --> hashmap is of fixed length

https://leetcode.com/problems/maximum-number-of-balloons/

"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if not text:
            return 0
        hash_map = dict()
        
        for i in range(len(text)):
            ch=text[i]
            
            if ch in ('b', 'a', 'l', 'o', 'n'):
                hash_map[ch]=hash_map.get(ch, 0) + 1
            
        
        b_count=hash_map.get('b', 0)
        l_count=hash_map.get('l', 0) // 2
        o_count=hash_map.get('o', 0) // 2
        
        return min(b_count, l_count, o_count)
