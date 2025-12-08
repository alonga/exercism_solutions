NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data is None:
            return

        # data must be a list
        if not isinstance(data, list):
            raise TypeError("Graph data malformed")

        for item in data:
            # each item must be a tuple of length at least 2
            if not isinstance(item, tuple) or len(item) < 2:
                raise TypeError("Graph item incomplete")

            item_type = item[0]

            if item_type == ATTR:
                self._add_attr(item)
            elif item_type == NODE:
                self._add_node(item)
            elif item_type == EDGE:
                self._add_edge(item)
            else:
                # unknown first element like 99
                raise ValueError("Unknown item")

    def _add_attr(self, item):
        # Expected: (ATTR, key, value)
        if len(item) != 3:
            raise ValueError("Attribute is malformed")
        _, key, value = item
        if not isinstance(key, str) or not isinstance(value, str):
            raise ValueError("Attribute is malformed")

        self.attrs[key] = value

    def _add_node(self, item):
        # Expected: (NODE, name, attrs_dict)
        if len(item) != 3:
            raise ValueError("Node is malformed")
        _, name, attrs = item
        if not isinstance(name, str) or not isinstance(attrs, dict):
            raise ValueError("Node is malformed")

        self.nodes.append(Node(name, attrs))

    def _add_edge(self, item):
        # Expected: (EDGE, src, dst, attrs_dict)
        if len(item) != 4:
            raise ValueError("Edge is malformed")
        _, src, dst, attrs = item
        if not (
            isinstance(src, str)
            and isinstance(dst, str)
            and isinstance(attrs, dict)
        ):
            raise ValueError("Edge is malformed")

        self.edges.append(Edge(src, dst, attrs))
