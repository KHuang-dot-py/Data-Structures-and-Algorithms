def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    ##################
    if R == (): return B
    ##################
    return tuple(B)

empty_tuple = ()
print(satisfying_booking(empty_tuple))