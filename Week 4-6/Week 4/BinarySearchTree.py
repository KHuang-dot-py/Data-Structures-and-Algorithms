class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        # A.subtree_update()  to be shown in R07
    
    def subtree_iter(A):                #O(n), yields all nodes in traversal order
        if A.left:  yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()

    def subtree_first(A):               #O(h)
        if A.left:  return A.left.subtree_first()
        else:       return A

    def subtree_last(A):                #O(h)
        if A.right: return A.right.subtree_last()
        else:       return A
    
    def successor(A):                   #O(h)
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent
    
    def predecessor(A):                 #O(h)
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent
    # inserts node b before A
    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
    
    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A

    def subtree_delete(A):
        if A.left or A.right:   # A is not a leaf
            if A.left:  B = A.predecessor()         # swap with rightmost of left subtree
            else:       B = A.successor()           # swap with leftmost of right subtree
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:            # A is a leaf
            if A.parent.left is A:  A.parent.left = None
            else:                   A.parent.right = None
        return A
    
class Binary_Tree:
    def __init__(T, Node_Type = Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type
    
    def __len__(T): return T.size
    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item
    def build(T,X):
        A = [x for x in X]
        def build_subtree(A, i, j):
            c = (i+j)//2
            root  = T.Node_Type(A[c])
            if i<c:         #still items remaining on left to be placed in subtree
                root.left = build_subtree(A, i, c-1)
                root.left.parent = root
            if c<j:
                root.right = build_subtree(A, c+1, j)
                root.right.parent = root
            return root
        T.root = build_subtree(A, 0, len(A)-1)

tree = Binary_Tree()

a_rray  = [1,2,3,4,5]
tree.build(a_rray)

for item in tree:
    print(item)