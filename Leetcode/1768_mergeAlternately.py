def mergeAlternately(word1, word2):
    merged = ""
    i = 0
    j = 0
    while i + j < len(word1) + len(word2):
        if i < len(word1) and (j == len(word2) or i == j):
            merged = merged + word1[i]
            i += 1
        else:
            merged = merged + word2[j]
            j += 1

        print(i,j)
    return merged

w1 = "abcdefg"
w2 = "pqrs"

print(mergeAlternately(w1,w2))