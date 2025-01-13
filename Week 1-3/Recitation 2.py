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

    def _copy_backward(self, i, n, A, j):
        for k in range (n-1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):
        n = len(self)
        A = [None] * (n+1) # creating a new array to copy into
        # Copying array sequence from start to right before new value
        self._copy_forward(0, i, A, 0)
        A[i] = x
        # Copying array sequence from insertion index until end(inclusive), shifting 1 forward
        self._copy_forward(i, n-i, A, i + 1)
        #Rebuilding self.A with new array
        self.build(A)

    def delete_at(self, i):
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
    
    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self), x)
    def delete_last(self): self.delete_at(len(self)-1)

A_rray = Array_Seq()

A_rray.build(i*i for i in range(5))

print(A_rray.A)

print("-"*15)

A_rray.insert_at(1,"One")

A_rray.delete_at(2)

A_rray.delete_first()

A_rray.delete_last()

print(A_rray.A)

