# https://leetcode.com/problems/integer-to-english-words
# TC:O(N)
# SC:O(1) , because only one string of variable lenght is used
class Solution:
    def __init__(self):
        self.less_than_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
            "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        self.tens = [
            "", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
            "Seventy", "Eighty", "Ninety"
        ]
        self.hundreds = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        result = ""
        for i in range(len(self.hundreds)):
            if num % 1000 != 0:
                result = self.helper(
                    num % 1000) + self.hundreds[i] + " " + result
            num = num // 1000
        return result.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[int(num)] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self.helper(
                num % 100)
