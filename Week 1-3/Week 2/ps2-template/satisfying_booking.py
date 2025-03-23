def merge_bookings(B1, B2):
    # initialize empty final booking
    B = []
    i1, i2 = 0,0
    n1, n2 = len(B1), len(B2)
    x = 0
    
    while i1 + i2 < n1 + n2:
        if i1 < n1: k1, s1, t1 = B1[i1]
        if i2 < n2: k2, s2, t2 = B2[i2]
        # When neither is depleted
        # When neither of the next bookings overlaps x
        if s1 > x and s2 > x:
            x = min(s1, s2)
        else:
            # When either of the lists are depleted
            if i1 == n1:
                k, s, t = k2, max(x,s2), t2
                i2 += 1
            elif i2 == n2:
                k, s, t = k1, max(x,s1), t1
                i1 += 1
            # When they overlap at some s' greater than x
            elif s1 < s2 < t1 and s2 > x:
                k, s, t = k1, s1, s2
                x = s2
            elif s2 < s1 < t2 and s1 > x:
                k, s, t = k2, s2, s1
                x = s1 
            # when they overlap at and after x
            elif s1 <= x < t1 and s2 <=x < t2:
                k = k1 + k2
                s = x
                t = min(t1,t2)
                x = t
                if t1 < t2: i1+=1
                elif t2 < t1: i2+=1
                elif t1 == t2:
                    i1 += 1
                    i2 += 1
            #when next booking does not overlap next booking after time x
            else:
                if s1 < s2:
                    k,s,t = k1,x,t1
                    x = t1
                    i1 += 1
                else:
                    k,s,t = k2,x,t2
                    x = t2
                    i2 += 1
            B.append((k,s,t))

    i = 0
    while i < len(B)-1:
        #if adjacent to next, and number of rooms is equal
        k1,s1,t1 = B[i]
        k2,s2,t2 = B[i+1]
        if t1 == s2 and k1 == k2:
            B[i] = k1,s1,t2
            B.pop(i+1)
        else:
            i += 1

    return B

def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    ##################
    #If the given tuple of talk requests is empty, return an empty schedule
    
    if R == []: return B
    # Base case is |R| = 1
    elif len(R) == 1:
        return [(1,R[0][0],R[0][1])]
    # Otherwise, split the list into two halves, then recursively compute bookings B1 and B2 that satisfy R1 and R2 respectively
    else:
        mid = len(R)//2
        B1 = satisfying_booking(R[:mid])
        B2 = satisfying_booking(R[mid:])
        # Then, compute a booking B that satisfies R1 and R2
        B = merge_bookings(B1,B2)    
    ##################
    return tuple(B)

# talks = [(1,2),(3,4)]

# print(satisfying_booking(talks))

# sched1 = [
#     (1,1,2)
# ]
# sched2 = [(1,3,4)]

# merged = merge_bookings(sched1,sched2)
# print(merged)

# [(2, 0, 1), (1, 1, 2), (1, 2, 3), (7,3,4) (8, 4, 5), (6,5,7)]