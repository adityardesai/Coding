"""
https://leetcode.com/playground/iTGQNajb

Items in Containers

Amazon would like to know how much inventory exists in their closed inventory compartments. Given a string s
consisting of items as "*" and closed compartments as an open and close "|", an array of starting indices
startIndices, and an array of ending indices endIndices, determine the number of items in closed compartments
within the substring between the two indices, inclusive.

An item is represented as an asterisk ('*' = ascii decimal 42)
A compartment is represented as a pair of pipes that may or may not have items between them ('|' = ascii decimal 124).

Example

s = '|**|*|*'

startIndices = [1, 1]

endIndices = [5, 6]

The string has a total of 2 closed compartments, one with 2 items and one with 1 item. For the first pair of
indices, (1, 5), the substring is '|**|*'. There are 2 items in a compartment.

For the second pair of indices, (1, 6), the substring is '|**|*|' and there are 2 + 1 = 3 items in compartments.

Both of the answers are returned in an array, [2, 3].

Function Description .

Complete the numberOfItems function in the editor below. The function must return an integer array that contains
the results for each of the startIndices[i] and endIndices[i] pairs.

numberOfItems has three parameters:

s: A string to evaluate

startIndices: An integer array, the starting indices.

endIndices: An integer array, the ending indices.

Constraints

1 ≤ m, n ≤ 105
1 ≤ startIndices[i] ≤ endIndices[i] ≤ n
Each character of s is either '*' or '|'

Input Format For Custom Testing

The first line contains a string, S.
The next line contains an integer, n, the number of elements in startIndices.
Each line i of the n subsequent lines (where 1 ≤ i ≤ n) contains an integer, startIndices[i].
The next line repeats the integer, n, the number of elements in endIndices.
Each line i of the n subsequent lines (where 1 ≤ i ≤ n) contains an integer, endIndices[i].

Sample Case 0
Sample Input For Custom Testing

STDIN Function

*|*| -> s = "*|*|"

1 -> startIndices[] size n = 1
1 -> startIndices = 1
1 -> endIndices[] size n = 1
3 -> endIndices = 3

** Sample Output**
0

Explanation
s = *|*|

n = 1
startIndices = [1]
n = 1
startIndices = [3]

The substring from index = 1 to index = 3 is '|'. There is no compartments in this string.

Sample Case 1
Sample Input For Custom Testing

STDIN Function

*|*|*| -> s = "*|*|*|"
1 -> startIndices[] size n = 1
1 -> startIndices = 1
1 -> endIndices[] size n = 1
6 -> endIndices = 6

Sample Output
2

Explanation
s = '*|*|*|'
n = 1
startIndices = [1]
n = 1
startIndices = [1]

The substring from index = 1 to index = 6 is '||*|'. There are two compartments in this string at (index = 2,
index = 4) and (index = 4, index = 6). There are 2 items between these compartments.


"""


def numberOfItems(s, startIndices, endIndices):
    n = len(s)
    # the left closest compartment index
    left = [-1] * n
    # the right cloest compartment index
    right = [-1] * n

    count = 0
    # the number items on the left side that are contained by compartments
    items = {}

    for L in range(len(s)):
        if s[L] == "|":
            left[L] = L
            items[L] = count
        else:
            count += 1
            if L - 1 >= 0: 
                left[L]=left[L-1] 
            else:
                left[L]=-1

        R = len(s) - 1 - L
        if s[R] == "|":
            right[R] = R
        else:
            if R + 1 < n:
                right[R]=right[R+1]
            else:
                right[R]=-1

    res = []
    for i in range(len(startIndices)):
        # convert it to 0-based index
        s, e = startIndices[i] - 1, endIndices[i] - 1
        if s > e:
            res.append(0)
            continue

        l, r = right[s], left[e]
        res.append(items[r] - items[l])

    return res

print(numberOfItems("|**|*|*", [1, 1], [5, 6]))     # [2,3]
print(numberOfItems("*|*|", [1], [3]))              # [0]
print(numberOfItems("*|*|*|", [1], [6]))            # [2]
print(numberOfItems("*|**|***|", [1,2,4,1], [4,6,6,9])) # [0, 2, 0, 5]
