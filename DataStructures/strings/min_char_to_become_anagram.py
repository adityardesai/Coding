# https://www.geeksforgeeks.org/remove-minimum-number-characters-two-strings-become-anagram/
# TC: O(N) N>M
# SC: O(1)

def remAnagram(str1, str2): 
  count1=[0] * 26
  count2=[0] * 26
  s=str1
  t=str2

  for i in range(len(s)):
    ascii_value = ord(s[i]) - ord('a')
    count1[ascii_value]+=1

  for i in range(len(t)):
    ascii_value = ord(t[i]) - ord('a')
    count2[ascii_value]+=1

  result=0

  for i in range(26):
    result += abs(count1[i] - count2[i])

  return result
