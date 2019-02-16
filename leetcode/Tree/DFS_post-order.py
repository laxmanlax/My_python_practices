from binaryTree import  BinaryTree, returnObj

def post_order(node):
    if node.left_child:
        post_order(node.left_child)
    if node.right_child:
        post_order(node.right_child)

    print node.value

obj =  returnObj()
post_order(obj)
