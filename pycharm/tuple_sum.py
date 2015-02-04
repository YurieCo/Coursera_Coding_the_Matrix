
"""
Problem 1: tuple sum(A, B)
input: lists A and B of the same length, where each element in each list is a pair (x, y) of numbers
output: list of pairs (x, y) in which the first element of the i
th pair is the sum of the first element of the i
th
pair in A and the first element of the i
th pair in B
example: given lists [(1, 2),(10, 20)] and [(3, 4),(30, 40)], return [(4, 6),(40, 60)]
"""

def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
    temp = [x for x in zip(A,B)]
    return [(temp[0][0][0] + temp[0][1][0], temp[0][0][1] + temp[0][1][1]), (temp[1][0][0] + temp[1][1][0], temp[1][0][1] + temp[1][1][1])]



print(tuple_sum([(1,2), (10,20)],[(3,4), (30,40)]))