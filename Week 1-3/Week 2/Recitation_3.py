#Implementation of sorted_array_set - - NON-FUNCTIONING CODE TEMPLATE

class Array_Seq:
    def __init__(self):     # O(1)
        self.A = []
        self.size = 0

    def __len__(self): return self.size     #O(1)
    def __iter__(self): yield from self.A   #O(n) generator that allows iteration

    def build(self, X):
        self.A = [a for a in X] #pretend this builds a static array
        # The above line uses a list comprehension to build the array from an iterable
            # newlist = [expression for item in iterable]
        self.size = len(self.A)

    def get_at(self, i): return self.A[i]   #O(1)
    def set_at(self, i, x): self.A[i] = x   #O(1)

    def _copy_forward(self, i, n, A, j):    #O(n)
        for k in range(n):
            A[j + k]  = self.A[i + k]
    # i = start point old array to copy from
    # n = number of loops/num of values to be copied
    # A = array to copy into
    # j = start point new array to copy into

    def _copy_backward(self, i, n, A, j):   #O(n)
        for k in range (n-1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):              #O(n)
        n = len(self)
        A = [None] * (n+1) # creating a new array to copy into
        # Copying array sequence from start to right before new value
        self._copy_forward(0, i, A, 0)
        A[i] = x
        # Copying array sequence from insertion index until end(inclusive), shifting 1 forward
        self._copy_forward(i, n-i, A, i + 1)
        #Rebuilding self.A with new array
        self.build(A)

    def delete_at(self, i):                 #O(n)
        n = len(self)
        A = [None] * (n-1)
        # Copying elements before deletion
        self._copy_forward(0,i,A,0)
        # saving reference to element being removed from seq
        x = self.A[i]
        # Copying array seq from element after deletion until end, shifting 1 backward
        self._copy_forward(i + 1, n-i-1, A, i)
        self.build(A)
        return x
    
    def insert_first(self, x): self.insert_at(0, x)         #O(n)
    def delete_first(self): self.delete_at(0)               #O(n)
    def insert_last(self, x): self.insert_at(len(self), x)  #O(n)
    def delete_last(self): self.delete_at(len(self)-1)      #O(n)





# below is template code
class Sorted_Array_Set:
    def __init__(self): self.A = Array_Seq()                #O(1)
    def __len__(self): return len(self.A)                   #O(1)
    def __iter__(self): yield from self.A                   #O(n)
    def iter_order(self): yield from self                   #O(n)

    def build(self, X):
        self.A.build(X)                                     #O|X|
        # self._sort()                                        # depends...
        self._merge_sort()

    def _merge_sort(self, a = 0, b = None):         #Sort sub-array A[a:b]
        A = self.A
        if b is None:                           #O(1) initialize
            b = len(A)                          #O(1)
        if 1 < b - a:                           # size  k = b-a
            c = (a + b + 1) // 2                # compute centre
            self._merge_sort(a, c)                 # T(k/2) sort left
            self._merge_sort(c, b)                 # T(k/2) sort right
            L, R = A[a:c], A[c:b]
            i, j = 0,0
            while a<b:
                if (j >= len(R)) or (i < len(L) and L[i] < R[j]):   #O(1) check side
                    A[a] = L[i]                                     #O(1) merge from left
                    i = i + 1                                       #O(1) decrement left pointer
                else:
                    A[a] = R[j]                                     #O(1) merge from right
                    j = j + 1                                       #O(1) j = j + 1 decrement right pointer
                a = a + 1                                           #decrement merge pointer
    # def selection_sort(A):
    #     # starting with full array, then shorter subarrays, finding largest element
    #     # and inserting it last
    #     for i in range (len(A)-1, 0, -1):              #O(n) loop over array
    #         m = i                                           #O(1) initial index of max
    #         for j in range(i):                              #O(i) search for max in A(i)
    #             if A[m] < A[j]:                             #O(1) check for larger value
    #                 m = j                                   #O(1) if new max found
    #             A[m], A[i] = A[i], A[m]                     #O(1) swap

    def _binary_search(self, k, i, j):
        if i >= j:          return i
        m = (i+j)//2
        x = self.A.get_at(m)
        if x.key > k: return self._binary_search(k, i, m - 1)
        if x.key < k: return self._binary_search(k, m + 1, j)
        return m
    
    def find_min(self):
        if len(self) > 0:   return self.A.get_at(0)
        else:               return None

    def find_max(self):
        if len(self) > 0:   return self.A.get_at(len(self)-1)
        else:               return None

    def find(self, k):                      #O(log n)
        if len(self) == 0:  return None
        i = self._binary_search(k, 0, len(self)-1)
        x = self.A.get_at(i)
        if x.key == k:      return x # binary search as implemented may not always find k, returns closest index
        else:               return None

    def find_next(self, k):                 #O(log n)
        if len(self) == 0:  return None
        # find index where k is
        i = self._binary_search(k, 0, len(self) - 1)
        # and the item
        x = self.A.get_at(i)
        # if found element has a key larger than k, return it
        if x.key > k: return x
        # if there is another element before end of array, return it
        if i+1 < len(self): return self.A.get_at(i + 1)
        else:               return None

    def insert(self, x):                    #O(n) worst case, if a resize is required
        if len(self.A) == 0:
            self.A.insert_first(x)
        else:
            # find where new element x would be inserted, based on key
            i = self._binary_search(x.key, 0, len(self.A) - 1)
            k = self.A.get_at(i).key
            # if there is an element at that spot with the same key, replace it
            if k == x.key:
                self.A.set_at(i, x)
                return False
            #if key of item in spot is greater, insert at position i
            if k > x.key: self.A.insert_at(i, x)
            # if key of item in spot is lesser, insert after it at i+1
            else:           self.A.insert_at(i+1, x)
        return True
    
    def delete(self, k):                    #O(n) possible resize after deletion?
        i = self._binary_search(k, 0, len(self.A)-1)
        # assert that there exists an element at i with key k, else raise an assertion error
        assert self.A.get_at(i).key == k
        return self.A.delete_at(i)


my_set = Sorted_Array_Set()
my_set.build(range(1,6))
