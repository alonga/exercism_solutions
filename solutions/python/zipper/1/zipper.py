class Zipper:
    def __init__(self, tree, breadcrumbs):
        # current focus: a dict with keys "value", "left", "right"
        self.tree = tree
        # breadcrumbs: list of (parent_value, sibling_subtree, direction)
        # newest crumb first (closest parent)
        self.breadcrumbs = breadcrumbs

    # ---- constructors / conversion ----
    @staticmethod
    def from_tree(tree):
        if tree is None:
            return None
        # deep copy so we don't mutate the caller's dict
        import copy
        return Zipper(copy.deepcopy(tree), [])

    def to_tree(self):
        """Rebuild the full tree from the current focus and breadcrumbs."""
        t = self.tree
        for value, other_child, direction in self.breadcrumbs:
            if direction == "left":
                # we came down from the left; other_child is right subtree
                t = {"value": value, "left": t, "right": other_child}
            else:  # "right"
                # we came down from the right; other_child is left subtree
                t = {"value": value, "left": other_child, "right": t}
        return t

    # ---- navigation / accessors ----
    def value(self):
        return self.tree["value"]

    def left(self):
        left = self.tree.get("left")
        if left is None:
            return None
        crumb = (self.tree["value"], self.tree.get("right"), "left")
        return Zipper(left, [crumb] + self.breadcrumbs)

    def right(self):
        right = self.tree.get("right")
        if right is None:
            return None
        crumb = (self.tree["value"], self.tree.get("left"), "right")
        return Zipper(right, [crumb] + self.breadcrumbs)

    def up(self):
        if not self.breadcrumbs:
            return None
        value, other_child, direction = self.breadcrumbs[0]
        # rebuild parent using current focus and the saved sibling
        if direction == "left":
            parent = {"value": value, "left": self.tree, "right": other_child}
        else:  # came from right
            parent = {"value": value, "left": other_child, "right": self.tree}
        return Zipper(parent, self.breadcrumbs[1:])

    # ---- mutation (return self for chaining) ----
    def set_value(self, value):
        self.tree = {
            "value": value,
            "left": self.tree.get("left"),
            "right": self.tree.get("right"),
        }
        return self

    def set_left(self, left):
        # left is either None or a subtree dict
        self.tree = {
            "value": self.tree["value"],
            "left": left,
            "right": self.tree.get("right"),
        }
        return self

    def set_right(self, right):
        # right is either None or a subtree dict
        self.tree = {
            "value": self.tree["value"],
            "left": self.tree.get("left"),
            "right": right,
        }
        return self

