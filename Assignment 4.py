



#create a class called node for handling the binary tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None # Root of the tree is initialized to none

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_rec(self.root, key)

    def insert_rec(self, node, key):
        if key < node.value: # If the key is less than the current assigned node value
            if node.left is None:
                node.left = Node(key) # create a new child on the left
            else:
                self.insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key) # Create a new child on the right side of the tree
            else:
                self.insert_rec(node.right, key)

    def inorder(self):
        return self.inorder_rec(self.root)

    def inorder_rec(self, node):
        if node is None:
            return [] # If  the node is empty or None then return an empty list
        return self.inorder_rec(node.left) + [node.value] + self.inorder_rec(node.right)

    def preorder(self):
        return self.preorder_rec(self.root)

    def preorder_rec(self, node):
        if node is None:
            return []
        return [node.value] + self.preorder_rec(node.left) + self.preorder_rec(node.right)

    def postorder(self):
        return self.postorder_rec(self.root)
    def postorder_rec(self, node):
        if node is None:
            return []
        return self.postorder_rec(node.left) + self.postorder_rec(node.right) + [node.value]


if __name__ == "__main__":
    tree = BinaryTree()

    insert_node_list = [5, 3, 7, 2, 4, 6, 8]

    for node in insert_node_list:
        tree.insert(node)

    print("In order Tree: ", tree.inorder())
    print("Pre-order Tree: ", tree.preorder())
    print("Post-order Tree: ", tree.postorder())

