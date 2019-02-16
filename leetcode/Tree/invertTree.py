class Tree:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


Stree = Tree(4)
Stree.left = Tree(2)
Stree.right = Tree(7)
Stree.left.left = Tree(1)
Stree.left.right = Tree(3)
Stree.right.left = Tree(6)
Stree.right.right = Tree(9)

"""
Input: -->

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output: -->

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
def invertTree(root):
    if not root:
        return None

    root.left , root.right = root.right , root.left

    invertTree(root.left)
    invertTree(root.right)

    return root

def invertTreeUsingStack(node):
    stack = [node]

    while stack:
        root = stack.pop(0)
        if root:
            root.left, root.right = root.right, root.left
            stack += root.left, root.right

    return node

invert_tree = invertTree(Stree)
invert_tree = invertTreeUsingStack(Stree)


def printTree(root):
    print root.val
    if root.left:
        printTree(root.left)

    if root.right:
        printTree(root.right)

print printTree(invert_tree)

"""
4
7
9
6
2
3
1
"""
