# find largest element in a stack


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        # if stack empty, return None
        if not self.items: return None
        return self.items.pop()

    def peek(self):
        if not self.items: return None
        return self.items[len(self.items)-1]

# use previous Stack class
class MaxStack:
    # last entry in max stack is the largest in stack
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    # add item to normal stack, check if larger than last item in max_stack
    def push(self, item):
        self.stack.push(item)
        if item >= self.max_stack.peek():
            self.max_stack.push(item)

    # pop off last from stack, if last from stack is last entry in max_stack, pop that too
    def pop(self):
        item = self.stack.pop()
        if (item == self.max_stack.peek()):
            self.max_stack.pop()
        return item

    def get_max(self):
        # returns largest element without removing
        # easy/O(n) method is to walk through stack and grab largest element
        # better method might be to have 2 stacks, 1 to keep track of max as you push/pop
        return self.max_stack.peek()

