#https://leetcode.com/problems/minimum-window-substring/
#TC:O(|S| + |T|)
#SC:O(|S| + |T|)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''

        t_map = dict()
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1

        l = 0
        r = 0
        formed = 0
        min_win_length = float('inf')
        ans_l = 0
        ans_r = 0
        current_window = dict()

        while r < len(s):
            ch = s[r]
            current_window[ch] = current_window.get(ch, 0) + 1
            if ch in t_map and current_window[ch] == t_map[ch]:
                formed += 1

            while formed == len(t_map):
                ch = s[l]
                if r - l + 1 < min_win_length:
                    min_win_length = r - l + 1
                    ans_l = l
                    ans_r = r
                current_window[ch] -= 1
                if ch in t_map and current_window[ch] < t_map[ch]:
                    formed -= 1
                l += 1
            r += 1
        if min_win_length == float('inf'):
            return ''
        else:
            return s[ans_l:ans_r + 1]
