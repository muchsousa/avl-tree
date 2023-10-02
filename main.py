from tree import AVLTree

tree = AVLTree()

values_to_insert = [90, 52, 34, 11, -19, 43, -3, 0, 1, 7]
for value in values_to_insert:
    tree.insert(value)

tree.print_json()

values_to_remove = [11, 43,0, 7]
for value in values_to_remove:
    tree.remove(value)

tree.print_json()
