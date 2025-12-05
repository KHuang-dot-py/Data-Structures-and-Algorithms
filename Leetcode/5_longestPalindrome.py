def longestPalindrome(s: str) -> str:
#intuition
#   window moving forward, we remember the letters we've seen.
# - mark of a palindrone is 2 letters that repeat, or 2 letters that repeat around a pivot
# - Mathematically, position 0 of palindromic substring is the same character as position -1, 1 : -2, etc.
# naive approach is to test all substrings for palindromic properties.

#approach in words
    # For each position in s, we check for a palindrome starting centered around s[i], or the pair s[i,i-1]
    # then, run a helper function that finds the bounds of that palindrome
    # compare it to the longest palindrome currently stored, and overwrite if larger

    # Can we do better? Yes with MANACHER's algorithm - O(n) time and O(n) space

#time complexity
#   this is 2n checks, and for each, worst case O(n) comparisons, for total O(n**2)
#space complexity
#   O(1) extra space to store the bounds of longest palindrome, and a substring indices while checkign

    # function looks forward and backward to find bounds of palindrome, returns indices
    def palindromeBounds(l,r):
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return [l+1,r-1]
    # if s is length 1:
    if len(s) < 2:
        return s
    
    #inclusive bounds of longest palindrome
    longest = [0,0]

    # choosing that if there is a tie, keep the earlier substring
    for i in range(1, len(s)):
        left, right = palindromeBounds(i-1,i)
        if right-left > longest[1] - longest[0]:
            longest = [left, right]
        left, right = palindromeBounds(i, i)
        if right-left > longest[1] - longest[0]:
            longest = [left, right]
    
    return s[longest[0]:longest[1]+1]

test_strings = ["babad","bb", "ababaxyz"]
"a", "", "aba", "abcdefg", "ababaxyz", 
for s in test_strings:
    print(longestPalindrome(s))