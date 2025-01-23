class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        # When the list is empty
        new_node = Doubly_Linked_List_Node(x)
        if self.head == self.tail == None:
            self.insert_last(x)
            return
        # List length 1
        elif self.head == self.tail:
            new_node.prev = self.head
            self.head = new_node
            return
        second_node = self.head.next
        new_node.next = second_node
        second_node.prev = new_node
        self.head = new_node
        pass

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        new_node = Doubly_Linked_List_Node(x)
        # When list is empty
        if self.head == self.tail == None:
            self.head = new_node
            self.tail = new_node
            return
        # When list is length 1
        if self.head == self.tail:
            new_node.prev = self.head
            self.head.next = new_node
            self.tail = new_node
            return
        # point old tail to our new node and vice versa
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        pass

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        # When list is empty
        if self.head == self.tail == None:
            return x
        # When list is length 1
        elif self.head == self.tail:
            x = self.head.item
            self.head == None
            self.tail == None
            return x
        x = self.head.item
        self.head = self.head.next
        self.head.prev = None
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        # When the list is empty
        if self.head == None or self.tail == None:
            return x
        # When the list is length 1
        elif self.head == self.tail:
            self.delete_first()
        x = self.tail.item
        self.tail = self.tail.prev
        self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        if self.head == None or self.tail == None:
            pass
        before_x1 = x1.prev
        after_x2 = x2.next
        before_x1.next = after_x2
        after_x2.prev = before_x1
        L2.head = x1
        x1.prev = None
        L2.tail = x2
        x2.next = None
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        after_x = x.next
        x.next = L2.head
        L2.head.prev = x
        L2.tail.next = after_x
        after_x.prev = L2.tail
        L2.head = None
        L2.tail = None
        pass


my_ll = Doubly_Linked_List_Seq()
my_ll.build(range(5))

my_ll.insert_first("Zero")

for node in my_ll:
    print(node)