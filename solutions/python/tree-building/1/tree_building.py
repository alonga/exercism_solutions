class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, record_id):
        self.node_id = record_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    # Sort records by id
    records = sorted(records, key=lambda r: r.record_id)

    # Validate contiguous IDs: 0,1,2,3,...,n
    for expected, rec in enumerate(records):
        if rec.record_id != expected:
            raise ValueError("Record id is invalid or out of order.")

    # Validate root must be 0, parent 0
    root = records[0]
    if root.parent_id != 0:
        raise ValueError("Node parent_id should be smaller than its record_id.")

    nodes = {0: Node(0)}

    for rec in records[1:]:
        # Self-parent cycle (except root)
        if rec.record_id == rec.parent_id:
            raise ValueError("Only root should have equal record and parent id.")

        # Parent must always be < record id (tree structure rule)
        if rec.parent_id > rec.record_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")

        # Parent must exist (valid ordering)
        if rec.parent_id not in nodes:
            raise ValueError("Record id is invalid or out of order.")

        # Add child to tree
        new_node = Node(rec.record_id)
        nodes[rec.record_id] = new_node
        nodes[rec.parent_id].children.append(new_node)

    return nodes[0]
