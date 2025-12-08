from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def _find_path(self, target):
        if self.label == target:
            return [self]
        for child in self.children:
            sub = child._find_path(target)
            if sub:
                return [self] + sub
        return None

    def from_pov(self, from_node):
        path = self._find_path(from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")

        new_root = Tree(path[-1].label)
        current_new = new_root

        # Reverse the chain
        for parent in reversed(path[:-1]):
            new_child = Tree(parent.label)
            current_new.children.append(new_child)
            current_new = new_child

        # Attach subtrees other than reversed path
        def attach_children(old_node, new_node, block_node):
            for child in old_node.children:
                if child is not block_node:
                    copy_child = Tree(child.label)
                    new_node.children.append(copy_child)
                    attach_children(child, copy_child, old_node)

        for i, old_node in enumerate(path):
            new_node = new_root
            for _ in range(len(path) - i - 1):
                new_node = new_node.children[0]
            block_node = path[i + 1] if i + 1 < len(path) else None
            attach_children(old_node, new_node, block_node)

        return new_root

    def path_to(self, from_node, to_node):
        tree = self.from_pov(from_node)
        path = tree._find_path(to_node)
        if not path:
            raise ValueError("No path found")  # Correct message
        return [node.label for node in path]
