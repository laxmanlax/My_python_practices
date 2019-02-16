from binaryTree import  BinaryTree, returnObj

def in_order(node):
    if node.left_child:
        in_order(node.left_child)

    print node.value

    if node.right_child:
        in_order(node.right_child)

obj =  returnObj()
in_order(obj)
