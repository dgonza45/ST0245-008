# Presentado por: Daniel Gonzalez Bernal
# Codigo: 202023300010


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildtree(inorder, preorder, instrt, inend):
    if instrt > inend:
        return None
    tNode = Node(preorder[buildtree.preIndex])
    buildtree.preIndex += 1
    if instrt == inend:
        return tNode
    inindex = search(inorder, instrt, inend, tNode.data)
    tNode.left = buildtree(inorder, preorder, instrt, inindex - 1)
    tNode.right = buildtree(inorder, preorder, inindex + 1, inend)
    return tNode


def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


def postorder(a):
    if a is None:
        return None
    else:
        postorder(a.left)
        postorder(a.right)
        print(a.data, end=' ')


def inorden(a):
    if a is None:
        return None
    else:
        inorden(a.left)
        print(a.data, end=' ')
        inorden(a.right)


def preorden(a):
    if a is None:
        return None
    else:
        print(a.data, end=' ')
        preorden(a.left)
        preorden(a.right)


preord = ['G', 'E', 'A', 'I', 'B', 'M', 'C', 'L', 'D', 'F', 'K', 'J', 'H']
inord = ['I', 'A', 'B', 'E', 'G', 'L', 'D', 'C', 'F', 'M', 'K', 'H', 'J']

buildtree.preIndex = 0
arbol = buildtree(inord, preord, 0, len(inord) - 1)
inorden(arbol)  # Con esta funcion probamos que el arbol se armo bien inorden
print(" ")
preorden(arbol)  # Con esta funcion probamos que el arbol se armo bien preorden
print(" ")
postorder(arbol)  # Conesta funcion imprimimos el postorden
print(" ")
