from binaryTree import  BinaryTree, returnObj

def bfs(node):
    q = []
    q.append(node)

    while q!=[]:
        current_node = q.pop(0)
        print current_node.value

        if current_node.left_child:
            q.append(current_node.left_child)

        if current_node.right_child:
            q.append(current_node.right_child)


node = returnObj()
bfs(node)
