class Node:
    def __init__(self, i):
        self.data = i
        self.next = None
        self.prev = None

node1 = Node(11)
node2 = Node(22)
node1.next = node2
node2.prev = node1

node3 = Node(33)
node2.next = node3
node3.prev = node2


def traverse_list_reverse(node):
    while node is not None:
        print(node.data)
        node = node.prev


if __name__ == '__main__':
    traverse_list_reverse(node3)
