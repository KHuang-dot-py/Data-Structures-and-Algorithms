# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

#essentially, we want the values of the rightmost node at each level. 
#So, we traverse every node, keeping track of the level, as well as how far "right" the node is 
# # traverse tree to bottom nodes, keeping track of level, then append to an array of length log(n) containing right-most value at each level
# # base case: 1 node: return that value
# # base case+1: 2 nodes: return value of the right branch for each element in the array


def rightSideView(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    # have to be updating a defined array, since we don't know how deep it is...
    def dfs(node):
        # if empty tree is given:
        if node is None:
            return[]
        # base case
        if node.left is None and node.right is None:
            return [node.val]
        elif node.right is None:
            return [node.val] + dfs(node.left)
        elif node.left is None:
            return [node.val] + dfs(node.right)
        else:
            l = dfs(node.left)
            r = dfs(node.right)
            combined = []
            longer = max(len(l), len(r))
            for i in range(longer):
                if i < len(r):
                    combined.append(r[i])
                else:
                    combined.append(l[i])
            return [node.val] + combined

    return dfs(root)