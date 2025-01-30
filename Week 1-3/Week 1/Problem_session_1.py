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

ll = Linked_List_Seq()
ll.build(range(1,12))


def reorder_students(L): 
    ''' 2 
    3 Input: L | linked list with head L.head and size L.size 
    4 Output: None | 
    5 This function should modify list L to reverse its last half. 
    6 Your solution should NOT instantiate: 
    7 -any additional linked list nodes 
    8 -any other non-constant-sized data structures 
    ''' 
    ################## 
    # Finding the nth node
    n = L.size//2
    # Traversing n-1 times to find the nth node
    nth_node = L.head
    for i in range (n-1):
        nth_node = nth_node.next
    # For reversal
    # traversing to end of list
    curr_node = nth_node.next
    prev_node = None
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    nth_node.next = prev_node
    ################## 
    return 


reorder_students(ll)
for i in ll:
    print(i)