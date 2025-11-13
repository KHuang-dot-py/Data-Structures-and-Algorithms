# class Solution:
def mergeAlternately(word1: str, word2: str) -> str:
    i = 0
    j = 0
    result = []
    while i+j < len(word1) + len(word2):
        if i < len(word1):
            result.append(word1[i])
            i += 1
        if j < len(word2):
            result.append(word2[j])
            j += 1
    return "".join(result) 

w1 = "abcdefg"
w2 = "pqrs"

print(mergeAlternately(w1,w2))