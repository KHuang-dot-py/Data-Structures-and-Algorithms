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


A_rray = Array_Seq()

A_rray.build(i*i for i in range(5))

print(A_rray.A)


####
# Linked list implementation below 
####
class Linked_List_Node:
    def __init__(self,x):
        self.item = x
        self.next = None

    def later_node(self, i):
        if i==0: return self
        assert self.next
        return self.next.later_node(i-1)

class Linked_List_Seq:
    def __init__(self) : # Called on class initialization to create an instance, O(1)
        self.head = None
        self.size = 0

    def __len__(self): return self.size #O(1)
    # Iterators need a __iter__ method that returns the current object, and a __next__ method
    # that for loops call using iter() and next()
    def __iter__(self):                 #O(n) iter_seq
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):                 #O(n)
        for a in reversed(X):
            self.insert_first(a)

    def get_at(self, i):                #O(n)
        node = self.head.later_node(i)
        return node.item

    def insert_first(self,x) :          #O(1)
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete_first(self):             #O(1)
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x
    
    def insert_at(self, i, x):          #O(i) linear but scales with insertion index
        if i == 0:
            self.insert_first(x)
            return
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i-1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, i):             #O(i) linear but scales with insertion index
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i-1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x
    
    def insert_last(self, x): self.insert_at(len(self), x)  #O(n)
    def delete_last(self, x): self.delete_at(len(self)-1)   #O(n)


####
# Dynamic array sequence implementation below. 
# supports dynamic operations in amortized constant time
# Allocated space is double the length of the full array
####

#Parent class is Array_seq, but some methods have been overwritten
class Dynamic_Array_Seq(Array_Seq): 
    def __init__(self, r = 2):      #O(1)
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self): return self.size

    def __iter__(self):             #O(n)
        for i in range(len(self)): yield self.A[i]

    def build(self, X):             #O(n)
        for a in X: self.insert_last(a)
    
    def _compute_bounds(self):      #O(1)
        self.upper = len(self.A)
        self.lower = len(self.A)
    
    def _resize(self,n):             #O(n) or O(1)??? -- come back to this
        if (self.lower < n < self.upper): return
        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()
    
    def insert_last(self, x):       #O(1)a
        self._resize(self.size+1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):          #O(1)a
        self.A[self.size-1] = None
        self.size -= 1
        self._resize(self.size)
    
    def insert_at(self, i, x):      #O(n)
        self.insert_last(None) #adds 1 empty element to resize if needed
        self._copy_backwards_from_insert_to_end(i)
        self.A[i] = x
    
    def _copy_backwards_from_insert_to_end(self, i):    #O(n)
        self._copy_backward(i, self.size - (i+1), self.A, i + 1)

    def delete_at(self, i):         #O(n)
        x = self.A[i]
        # copying forward from element after deletion to end, shifted one back
        self._copy_forward(i+1, self.size - (i+1), self.A, i)
        self.delete_last()
        return x
    
    def insert_first(self, x): self.insert_at(0, x)     #O(n)
    def delete_first(self): return self.delete_at(0)    #O(n)

dyno_A_rray = Dynamic_Array_Seq()
dyno_A_rray.build(A_rray)

dyno_A_rray.insert_at(2, 1.5**2)

for i in dyno_A_rray:
    print(i)
