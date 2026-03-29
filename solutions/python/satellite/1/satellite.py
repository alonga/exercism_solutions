def tree_from_traversals(preorder, inorder):
    # --- Validation checks ---

    # 1: Same length
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    # 2: Unique elements check
    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("traversals must contain unique items")

    # 3: Same elements check
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    # Empty case → return {}
    if not preorder:
        return {}

    # Create map for quick lookup
    index_map = {v: i for i, v in enumerate(inorder)}

    def build(pre_start, pre_end, in_start, in_end):
        # No node → empty dict
        if pre_start >= pre_end:
            return {}

        root_val = preorder[pre_start]
        in_root_idx = index_map[root_val]

        # number of items in left subtree
        left_size = in_root_idx - in_start

        left = build(
            pre_start + 1,
            pre_start + 1 + left_size,
            in_start,
            in_root_idx
        )
        right = build(
            pre_start + 1 + left_size,
            pre_end,
            in_root_idx + 1,
            in_end
        )

        return {"v": root_val, "l": left, "r": right}

    return build(0, len(preorder), 0, len(inorder))
