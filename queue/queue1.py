class Queue:
    def __init__(self):
        self.queue = []

    def enque(self, val):
        self.queue.insert(0, val)

    def deque(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == '__main__':
    queue1 = Queue()

    queue1.enque("a")
    queue1.enque("b")
    queue1.enque("c")
    queue1.enque("b")
    print(queue1.queue)

    queue1.deque()
    queue1.deque()
    print(queue1.queue)

    queue1.deque()
