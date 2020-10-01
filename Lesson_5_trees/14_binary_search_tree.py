class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self._insert_helper(self.root, new_val)
        pass

    def _insert_helper(self, current_node, new_val):
        if new_val > current_node.value:
            if current_node.right is not None:
                current_node = current_node.right
                return self._insert_helper(current_node, new_val)
            else:
                current_node.right = Node(new_val)
        else:
            if current_node.left is not None:
                current_node = current_node.left
                return self._insert_helper(current_node, new_val)
            else:
                current_node.left = Node(new_val)
        pass

    def search(self, find_val):
        return self._search_helper(self.root, find_val)

    def _search_helper(self, current_node, find_val):
        if find_val == current_node.value:
            return True

        if find_val > current_node.value:
            if current_node.right is not None:
                current_node = current_node.right
                return self._search_helper(current_node, find_val)
            else:
                return False
        else:
            if current_node.left is not None:
                current_node = current_node.left
                return self._search_helper(current_node, find_val)
            else:
                return False
        pass


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
