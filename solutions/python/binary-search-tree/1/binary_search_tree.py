class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self._root = None
        for value in tree_data:
            self._insert(value)

    def _insert(self, value):
        if self._root is None:
            self._root = TreeNode(value)
            return

        current = self._root
        while True:
            if value <= current.data:
                if current.left is None:
                    current.left = TreeNode(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    break
                current = current.right

    def data(self):
        return self._root

    def sorted_data(self):
        result = []
        self._inorder(self._root, result)
        return result

    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.data)
        self._inorder(node.right, result)
