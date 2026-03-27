from collections import defaultdict, deque

def can_chain(dominoes):
    if not dominoes:
        return []

    # Build adjacency and degree for Eulerian cycle check
    graph = defaultdict(list)
    degree = defaultdict(int)

    for i, (a, b) in enumerate(dominoes):
        graph[a].append((b, i))
        graph[b].append((a, i))
        degree[a] += 1
        degree[b] += 1

    # Check even degree (Eulerian condition)
    for d in degree.values():
        if d % 2 != 0:
            return None

    # Check graph connectivity (ignore isolated vertices)
    def is_connected():
        start = dominoes[0][0]
        visited = set()
        stack = [start]
        while stack:
            x = stack.pop()
            if x not in visited:
                visited.add(x)
                for y, _ in graph[x]:
                    stack.append(y)
        # Ensure every vertex that appears is visited
        used_vertices = {x for dom in dominoes for x in dom}
        return used_vertices.issubset(visited)

    if not is_connected():
        return None

    # Hierholzer’s Algorithm to build Eulerian cycle
    adj_copy = {k: v.copy() for k, v in graph.items()}
    stack = deque()
    path = []

    start = dominoes[0][0]
    stack.append((start, None))

    used_edges = set()

    while stack:
        v, edge_id = stack[-1]
        while adj_copy[v] and adj_copy[v][-1][1] in used_edges:
            adj_copy[v].pop()
        if adj_copy[v]:
            u, eid = adj_copy[v].pop()
            used_edges.add(eid)
            stack.append((u, eid))
        else:
            stack.pop()
            if edge_id is not None:
                path.append(edge_id)

    if len(path) != len(dominoes):
        return None

    # Convert edge IDs into oriented dominoes in correct order
    result = []
    current_vertex = dominoes[path[0]][0]
    for eid in path:
        a, b = dominoes[eid]
        if a == current_vertex:
            result.append([a, b])
            current_vertex = b
        else:
            result.append([b, a])
            current_vertex = a

    return result

