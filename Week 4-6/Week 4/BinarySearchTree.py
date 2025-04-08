class Binary_node:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        # A.subtree_update()  to be shown in R07
    
    def subtree_iter(A):                #O(n), yields all nodes in traversal order
        if A.left:  yield from A.left.subtree_itr()
        yield A
        if A.right: yield from A.right.subtree_itr()
