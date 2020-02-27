import merpy


def compare(tree_x, tree_y):
    conflict = False
    conflicting_nodes = [None, None]

    for x, y in zip(tree_x.bf(), tree_y.bf()):
        print(x.value, y.value)
        if x.hash != y.hash:
            conflict = True
            conflicting_nodes = [x, y]
            continue
        if conflict and (x.hash == y.hash):
            return (x, conflicting_nodes)

    return (tree_x, None) if not conflict else (None, [tree_x, tree_y])


tree = merpy.new_tree("x", "y", "z")
tree2 = merpy.new_tree("x", "y")

for x, y in zip(tree.bf(), tree2.bf()):


# n, conflict = tree.compare(tree2)
# print(n.value, conflict[0].value, conflict[1].value)

# node_x, node_y = conflict
# print(node_x.value, node_y.value)
