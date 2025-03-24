def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    ##################
    # convert lowercase alpha to integers from 0 to 26
    ord_A = ord('a')
    def lower_ord(char):
        return ord(char) - ord_A

    # generate the hashmap to hold the frequency tables for all possible substrings of length k
    k = len(S[0])
    F = {}
    freq = [0]*26
    # generate the frequency table for the first substring and insert it into the hashmap
    for i in range(0,k):
        freq[lower_ord(T[i])] += 1
    F[tuple(freq)] = 1

    # generate subsequent frequency tables and insert into the hashmap
    for i in range (k, len(T)):
        freq[lower_ord(T[i-k])] -= 1
        freq[lower_ord(T[i])] += 1
        key = tuple(freq)
        if key in F:
            F[key] += 1
        else:
            F[key] = 1

    def find_anagram_frequency(sub):
        freq_sub = [0]*26
        for char in sub:
            freq_sub[lower_ord(char)] += 1
        if tuple(freq_sub) in F:
            return F[tuple(freq_sub)]
        else:
            return 0

    for sub in S:
        A.append(find_anagram_frequency(sub))
    ##################
    return tuple(A)


a_rray = [47, 61, 36, 52, 56, 33, 92]


# def find_c(A):
#     for c in range(7, max(A)):
#         hash_keys = [(i*10+4)%c%7 for i in a_rray]
#         if set(hash_keys) == {0,1,2,3,4,5,6}:
#             return c
        
# print(find_c(a_rray))

substrings_to_test = ["ac"]
string_to_test = "acacac"
counts = count_anagram_substrings(string_to_test, substrings_to_test)

for i in range(0, len(substrings_to_test)):
    print(substrings_to_test[i],counts[i])