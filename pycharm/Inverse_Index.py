
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
print(idx)

## 3: (Task 3) Or Search
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> orSearch(idx, ['Bach','the'])
    {0, 2, 3, 4, 5}
    >>> orSearch(idx, ['Johann', 'Carl'])
    {0, 2, 3, 4, 5}
"""
    list3 = set([])
    list4 = []
    for i in range(0,len(query)):
        if inverseIndex.get(query[i], True):
            list3.update(inverseIndex.get(query[i]))

    return list3.union(inverseIndex.get(query[i]))

print(orSearch(idx, ['Johann', 'Carl']))