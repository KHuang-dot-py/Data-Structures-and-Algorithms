from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

import heapq

def initialize(S):
    # max-heap to store farm ids and capacities
    farms = []
    # dict of farm addresses and associated buildings, pointer to node
    addresses = {}
    # dict of building-farm pairs and demand
    for pair in S:
        s, c = pair[0], pair[1]
        heapq.heappush((-1*c,s))
        
        addresses[s] = [s,c,]
