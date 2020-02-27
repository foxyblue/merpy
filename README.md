
```python
l1 = Leaf(0, "l1")
l2 = Leaf(1, "l2")
merkle = Tree(l1, l2)

merkle = new_tree("l1", "l2")

merkle.add("l3")
merkle.addLeaf(l3)

node, conflict = merkle.diff(merkle2)

if (node.root) or (not conflict):
    # merkle tree's are the same

else:
    # node is the last node that compares.
    # conflict contains node1 and node2 which conflict.
    # These conflicting nodes may then be compared.

    # A conflict may be resolved by doing the following
    node.add(node2)
    node.add(node1)
```
