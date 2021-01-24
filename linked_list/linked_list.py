class Node:
    def __init__(self, i):
        self.data = i
        self.next = None


node1 = Node(11)
node2 = Node(22)
node1.next = node2

node3 = Node(33)
node2.next = node3


def traverse_list(node):
    while node is not None:
        print(node.data)
        node = node.next


if __name__ == '__main__':
    traverse_list(node1)
