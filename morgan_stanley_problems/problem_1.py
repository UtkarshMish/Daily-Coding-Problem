"""This problem was asked by Morgan Stanley.

In Ancient Greece, it was common to write text with the first line going left to right,
the second line going right to left, and continuing to go back and forth.
This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].
"""


class BTree():
    def __init__(self, tree: list) -> None:
        self.tree = tree
        self.root: self.Node = None
        self.level = 0
        for value in self.tree:
            self.insert(value)

    class Node:
        value = int()
        left = None
        right = None

        def __init__(self, value: int, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def vacantNode(self, value: Node) -> Node:
        if value.left == None or value.right == None:
            return value
        else:
            value = self.vacantNode(value=value.right)
            return self.vacantNode(value=value.left) if value == None else value

    def insert(self, value):
        newNode = self.Node(value)
        if self.root == None:
            self.root = newNode
        else:
            vNode: self.Node = self.vacantNode(self.root)
            if vNode.left == None:
                vNode.left = newNode
            else:
                vNode.right = newNode

    def showTree(self, node: Node) -> None:
        if node == None:
            return
        else:
            print(node.value)

            if self.level % 2 == 0:
                if node.right != None:
                    print(node.right.value)
                self.showTree(node.left)

            else:
                if node.left != None:
                    print(node.left.value)
                self.showTree(node.right)

            self.level += 1


if __name__ == "__main__":
    n = int(input("Enter total elements: "))
    treeValues = []
    for i in range(n):
        treeValues.append(int(input(f"Enter {i+1} value: ")))
    bTree = BTree(treeValues)
    bTree.showTree(bTree.root)
