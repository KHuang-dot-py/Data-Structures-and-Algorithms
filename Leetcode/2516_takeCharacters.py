def takeCharacters( s: str, k: int) -> int:

    # intuition
        # naive approach, explore all possibilities in 2^n time...

    # approach in words
        # what if I scan the whole array to find the number of times a,b and c appear.
            #store occurrences in an array, since string is only composed of a,b, and c
        # then, I move two pointers from the middle outwards until there are k of a,b and c.
        # return the number of elements outside both pointers
        # how to prove correctness??
            #if I were to go outside in, where the two pointers currently are, there are exactly k of a,b, and c.

    # time complexity
        # O(n)

    # space complexity
        # O(1)

    # generating freq table
    freq = {"a":0, "b": 0, "c": 0}
    
    for c in s:
        freq[c] += 1

    if any(val<k for key, val in freq.items()):
        return -1
    
    l = len(s)//2
    r = l+1
    # freq of a, b, c must be greater than or equal to k at the beginning

    while l >= 0:
        if freq[s[l]] == k:
            break
        else:
            freq[s[l]] -= 1
            l -= 1
    
    while r <= len(s)-1:
        # if any is equal to k, should return at that point
        if freq[s[r]] == k:
            break
        else:
            freq[s[r]] -= 1
            r += 1
    
    return len(s) - (r + 1) + (l + 1)

5 - 3 + 1

tests = [
    "abc",
    'aaaaaaaaaaaaaabc',
    "aabaaaacaabc",
    "acba",
    "cbbac"
]
         
k = 1

print(takeCharacters(tests[0],k))

