class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is not None:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right is not None:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.data)
        return res


if __name__ == '__main__':
    root = Node(4)
    root.insert(8)
    root.insert(5)
    root.insert(3)
    root.insert(2)
    root.insert(1)
    root.insert(9)

    root.print_tree()
    print(root.postorder_traversal(root))
