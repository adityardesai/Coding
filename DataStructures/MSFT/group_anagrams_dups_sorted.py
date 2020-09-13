# https://leetcode.com/discuss/interview-question/519744/Microsoft-Telephonic-round

# https://leetcode.com/playground/new/empty


from collections import defaultdict


# finally, O(N * M) by time - where N is a number of words. O(N) by space
def group_words(words):
    groups = dict()
    for word in words:
        m_set = set(word.lower())
        temp = ''.join(sorted(m_set))
        if temp in groups:
            groups[temp].append(word)
        else:
            groups[temp]=[word]

    return list(groups.values())


if __name__ == '__main__':
    words = {'Good', "pan", "nap", "dog", "god"}
    expected = [['Good', 'dog', 'god'], ['nap', 'pan']]
    print(group_words(words))
