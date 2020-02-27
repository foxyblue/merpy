from collections import deque


class Queue:
    """ Queue using the collection deque object
    see: https://wiki.python.org/moin/TimeComplexity"""

    def __init__(self):
        self.items = deque()

    def empty(self):
        return len(self.items) < 1

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
