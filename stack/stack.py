class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def peak(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


if __name__ == '__main__':
    stack1 = Stack()
    stack1.push("a")
    print(stack1.stack)
    stack1.push("b")
    print(stack1.stack)
    stack1.push("c")
    print(stack1.stack)

    print(stack1.peak())
    stack1.pop()
    print(stack1.stack)

    print(stack1.peak())
