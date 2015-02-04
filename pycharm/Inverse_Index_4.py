
f = ['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach']


def makeInverseIndex(f):

    dict2= {}
    lines = [line for line in f]
    for i in range(0,len(lines)):
        for k,v in enumerate(lines[i].split()):
            if dict2.get(v, False):
                dict2[v].update({i})
            else:
                dict2[v] = {i}
    return dict2

idx = makeInverseIndex(f)

## 4: (Task 4) And Search
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex([' Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """

    list4 = {i for i in range(len(inverseIndex))}

    for i in range(0,len(query)):
        if inverseIndex.get(query[i], True):
            list4.intersection_update(inverseIndex.get(query[i]))
    return list4

print(idx)
print(andSearch(idx, ['Johann', 'the']))
