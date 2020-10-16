"""

You are given a string S consisting of N letters 'a' and/or 'b'. In one move, you can swap one letter for the other ('a' for 'b' or 'b' for 'a').
Write a function solution that, given such a string S, returns the minimum number of moves required to obtain a string containing no instances of three
identical consecutive letters.
Examples:
1. Given S = "baaaaa", the function should return 1. The string without three identical consecutive letters which can be obtained in one move is "baabaa".
2. Given S = "baaabbaabbba", the function should return 2. There are four valid strings obtainable in two moves: for example, "bbaabbaabbaa".
3. Given S = "baabab", the function should return 0.
Write an ecient algorithm for the following assumptions:
N is an integer within the range [0..200,000];
string S consists only of the characters "a" and/or "b".
"""

def solution(s):
    if not s:
        return 0
    three_count=0
    for i in range(len(s)):
        temp_length=1
        while i+1 < len(s) and s[i]==s[i+1]:
            temp_length+=1
            i+=1
        three_count+= temp_length//3
    return three_count

def solution2(S):
    count=0
    i=0
    while i<len(S):
        t=1
        while i+1<len(S) and S[i+1]==S[i]:
            t+=1
            i+=1
        if t>=3:
            count = count + (t)//3
        i=i+1
    return count

def main():
    print(solution("baaaaa"))
    print(solution("baaabbaabbba"))
    print(solution("baabab"))

    print(solution2("baaaaa"))
    print(solution2("baaabbaabbba"))
    print(solution2("baabab"))

main()
