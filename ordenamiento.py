class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

def max(node):
    if node is None:
        return "no existe el nodo"

    current = node
    while current.right is not None:
        current = current.right

    return current.data

def min(node):
    if node is None:
            return "no existe el nodo"
    
    current = node
    while current.left is not None:
        current = current.left
    return current.data

def eliminar(root, data):
    node = TreeNode(data)

    if data < node.data:
        node.left = eliminar(node.left, data)
    elif data > node.data:
        node.right = eliminar(node.right, data)
    else:
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp= node.left
            node = None
            return temp

        node.data = min(node.right).data
        node.right = eliminar(node.right, node.data)
    return node

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18


inOrderTraversal(root)
"""
result = search(root, 8)
if result:
    print(f"Se encontro el nodo con el valor: {result.data}")
else:
    print("no se encontro el valor")

print(f"El maximo valor es: {max(root)}")
print(f"El minimo valor es: {min(root)}")
"""
eliminar(root, 15)
inOrderTraversal(root)