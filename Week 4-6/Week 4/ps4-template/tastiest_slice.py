from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        #########################################
        '''Augmenting the subtree with subtree sum and max_prefix_key'''
        left = -float("inf")
        right = -float("inf")
        left_sum = 0
        right_sum = 0
        if A.left: 
            left = A.left.max_prefix
            middle = A.left.subtree_sum + A.item.val
            left_sum = A.left.subtree_sum
        else:
            middle = A.item.val
        if A.right:
            right = middle + A.right.max_prefix
            right_sum = A.right.subtree_sum

        # subtree sum
        A.subtree_sum = left_sum + A.item.val + right_sum
        # max_prefix and max_prefix_key
        A.max_prefix = max(left, middle, right)

        # augmenting with max_prefix_key 
        if A.max_prefix == left:
            A.max_prefix_key = A.left.max_prefix_key
        elif A.max_prefix == right:
            A.max_prefix_key = A.right.max_prefix_key
        else:
            A.max_prefix_key = A.item.key
        #########################################

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        ##################
        k = self.root.max_prefix_key
        s = self.root.max_prefix
        ##################
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    toppings = sorted(toppings)
    for x, y, t in toppings:
        B.insert(Key_Val_Item(y,t))
        k, s = B.max_prefix()
        if s > T:
            # all toppings with x less than or equal to current are included
            X = x
            # but not all y, need to use prefix key
            Y = k
            T = s
    ##################
    return (X, Y, T)

topps = [(-7, 8, 5), (2, -4, 3), (7, 10, -1), (4, -3, 9), (-5, 1, 9)]
Sol = (4, 8, 26)

# print(tastiest_slice(topps) == Sol)