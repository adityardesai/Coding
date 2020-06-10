def flatten_dictionary(d):
    if not d:
        return
    result = dict()
    helper(d, '', result)
    return result


def helper(d, parent, result):

    for k, v in d.items():
        if type(v) == dict:
            helper(v, parent + k + '.', result)
        else:
            result[parent + k] = v


d = {'a': 1, 'b': {'c': 2, 'd': {'f': 5, 'e': 3}}}

print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
