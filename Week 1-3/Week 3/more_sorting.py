import string

def counting_sort(A):
    u = 1+(max([x.key for x in A]))
    D = [[] for i in range(u)]
    for x in A:
        D[x.key].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1

def radix_sort(A):
    # Sort A assuming items have non-negative keys
    n = len(A)
    u = 1+max([x.key for x in A])
    c = 1 + (u.bit_length() // n.bit_length()) #this gives logn(u) - 1, making c+1 digit tuples
    class Obj: pass
    D = [Obj() for a in A]
    for i in range(n):                      #O(nc) make digit tuples
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c):                  #O(c) make digit tuple, starting with least sig
            high, low = divmod(high,n)
            D[i].digits.append(low)
    for i in range(c):                  #O(nc) sort each digit
        for j in range(n):              #O(n) assign key i to tuples
            D[j].key = D[j].digits[i]
        counting_sort(D)
    for i in range(n):                  #O(n) output to A
        A[i] = D[i].item


a_rray = [329, 457, 657, 839, 436, 720, 355]

class obj2:
    def __init__(self, key, item):
        self.key = key
        self.item = item

a_set = [obj2(i,i) for i in a_rray]

radix_sort(a_set)

names = ["brock", "david", "lucas", "ciera", "felix", "clara","ringo"]


def string_tuple_sort(strings):
    # length of string array and number of letters
    n = len(strings)
    k = len(max(strings))
    # create dict mapping letters to numbers 0-25
    alphabet = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        alphabet[letter] = index
    # create objects for each string, add string as item
    class Obj: pass
    D = [Obj() for s in strings]
    for i in range(n):
        D[i].item = strings[i]
    # for each char in the string, starting with last
    for i in range(1,k+1):
        for j in range(n):
            D[j].key = alphabet[D[j].item[i*-1]] # assign the jth character as key
        counting_sort(D)
    for i in range(n):                            # output sorted strings to original array
        strings[i] = D[i].item

string_tuple_sort(names)

print(names)