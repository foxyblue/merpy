import hashlib
from math import ceil, log

from library import Queue


def new_tree(*args):
    leaves = []
    for i, leaf in enumerate(args):
        leaves.append(Leaf(i, leaf))

    return Tree(*leaves)


class Node:
    @property
    def hash(self):
        if self.value is None:
            return "0"
        return hashlib.md5(self.value.encode("utf-8")).hexdigest()


class Leaf(Node):
    left = None
    right = None

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


class Branch(Node):
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right
        self.value = left.hash + "-" + right.hash


# def compare(tree_x, tree_y):
#     for node_x, node_y in zip(tree_x.bf(), tree_y.bf()):


class Tree:
    def __init__(self, *args: Leaf):
        self.root = True
        self.leaves = args
        self.size = len(args)
        self._unbalanced()

    @property
    def height(self):
        return ceil(log(self.size, 2))

    def __len__(self):
        return self.size

    def bf(self):
        queue = Queue()
        queue.enqueue(self.tree)
        while queue.size() > 0:
            n = queue.dequeue()
            yield n
            if n.left:
                queue.enqueue(n.left)
            if n.right:
                queue.enqueue(n.right)

    def compare(self, other):
        diff = abs(other.height - self.height)
        tree = self.tree
        for _ in range(diff):
            tree = tree.left

    def _unbalanced(self):
        self.tree = _unbalanced_build(self.leaves)


def sub_tree(tree):
    return sub_tree(tree.left)


def _unbalanced_build(nodes):
    index = 0
    branches = []
    while index < len(nodes) and (len(nodes) - index != 1):
        left, right = index, index + 1
        branch = Branch(nodes[left], nodes[right])
        branches.append(branch)
        index += 2
    if len(nodes) - index == 1:
        branches.append(nodes[-1])
    return _unbalanced_build(branches) if len(branches) >= 2 else branch
