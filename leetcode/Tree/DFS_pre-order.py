from binaryTree import  BinaryTree, returnObj

def pre_order(node):
    print node.value

    if node.left_child:
        pre_order(node.left_child)

    if node.right_child:
        pre_order(node.right_child)

obj =  returnObj()
pre_order(obj)
