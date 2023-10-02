import json 

class Node:
  def __init__(self, value, left = None, right = None):
    self.height = 1
    self.value = value
    self.left = left
    self.right = right

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        print(f"#insert({value})")

        # create root node
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert_node(value, self.root)

        return self.root

    def remove(self, value):
        print(f"#remove({value})")

        self.root = self._remove_node(value, self.root)

        return self.root

    def search(self, value):
        print(f"#search({value})")

        return self._search_node(value, self.root)

    # ----------------------------------------------------------------

    def _insert_node(self, value, node):
        # create new node
        if node is None:
            return Node(value)
    
        # insert value on left side (value < node.value)
        if value < node.value:
            node.left = self._insert_node(value, node.left)

        # insert value on right side (value > node.value)
        if value > node.value:
            node.right = self._insert_node(value, node.right)

        # re-calculate node height
        max_height_node = max(self._node_height(node.left), self._node_height(node.right))
        node.height = 1 + max_height_node

        # calculate the balance factor
        balance_factor = self._balance_factor(node)

        # validate rotations
        # unbalance on right - rotate right
        if balance_factor > 1:
            # unbalance on left too - left-right case
            if value > node.left.value:
                node.left = self._rotate_left(node.left)

            return self._rotate_right(node)

        # unbalanced on left - rotate left
        if balance_factor < -1:
            # unbalance on right too - right-left case
            if value < node.right.value:
                node.right = self._rotate_right(node.right)
            
            return self._rotate_left(node)

        return node # no rotation needed

    def _remove_node(self, value, node):
        if node is None:
            return node
    
        # remove value on left side (value < node.value)
        if value < node.value:
            node.left = self._remove_node(value, node.left)

        # remove value on right side (value > node.value)
        if value > node.value:
            node.right = self._remove_node(value, node.right)
        
        # remove node
        if value == node.value:
            if node.left is None:
                node_right = node.right
                node = None

                return node_right

            if node.right is None:
                node_left = node.left
                node = None

                return node_left
 
            minor_node = self._get_minor_node(node.right)

            node.value = minor_node.value
            node.right = self._remove_node(node.right, minor_node.value)

        # re-calculate node height
        max_height_node = max(self._node_height(node.left), self._node_height(node.right))
        node.height = 1 + max_height_node

        # calculate the balance factor
        node_balance_factor = self._balance_factor(node)

        # validate rotations
        # unbalance on right - rotate right
        if node_balance_factor > 1:
            node_left_balance_factor = self._balance_factor(node.left)

            if node_left_balance_factor < 0:
                node.left = self._rotate_left(node.left)

            return self._rotate_right(node)

        # unbalanced on left - rotate left
        if node_balance_factor < -1:
            node_right_balance_factor = self._balance_factor(node.right)

            if node_right_balance_factor > 0:
                node.right = self._rotate_right(node.right)
            
            return self._rotate_left(node)

        return node # no rotation needed
    
    def _search_node(self, value, node):
        if node is None:
            return False
        
        if node.value == value:
            return True
    
        # search value on left side (value < node.value)
        if value < node.value:
            return self._search_node(value, node.left)

        # search value on right side (value > node.value)
        if value > node.value:
            return self._search_node(value, node.right)

    def _balance_factor(self, node):
        if node is None:
            return 0
               
        left_height = self._node_height(node.left)
        right_height = self._node_height(node.right)

        # calculate the balance factor
        balance_factor = left_height - right_height

        return balance_factor

    def _node_height(self, node):
        if node is None:
            return 0

        return node.height
    
    def _get_minor_node(self, root):
        if root is None or root.left is None:
            return root
 
        return self._get_minor_node(root.left)

    def _rotate_left(self, node):
        node_right = node.right
        node_left = node_right.left
 
        node_right.left = node 
        node.right = node_left

        # re-calculate node height
        max_height_node = max(self._node_height(node.left), self._node_height(node.right))
        node.height = 1 + max_height_node

        # re-calculate node_right height
        max_height_node_right = max(self._node_height(node_right.left), self._node_height(node_right.right))
        node_right.height = 1 + max_height_node_right

        return node_right
    
    def _rotate_right(self, node):
        node_left = node.left
        node_right = node_left.right

        node_left.right = node
        node.left = node_right

        # re-calculate node height
        max_height_node = max(self._node_height(node.left), self._node_height(node.right))
        node.height = 1 + max_height_node

        # re-calculate node_left height
        max_height_node_left = max(self._node_height(node_left.left), self._node_height(node_left.right))
        node_left.height = 1 + max_height_node_left

        return node_left

    def print_json(self):
        print("#print_json()")

        tree_data = self._print(self.root)
    
        json_object = json.dumps(tree_data, indent = 4) 
        print(json_object)

    def _print(self, node):
        if node is None:
            return None

        return {
            "value": node.value,
            "left": self._print(node.left),
            "right": self._print(node.right),
        }
