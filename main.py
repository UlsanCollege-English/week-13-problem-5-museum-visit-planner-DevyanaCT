def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.
    """

    # If start or goal is not in rooms, no path exists
    if start not in rooms or goal not in rooms:
        return []

    # If start and goal are the same
    if start == goal:
        return [start]

    # Build adjacency list
    graph = {r: [] for r in rooms}
    for a, b in doors:
        graph[a].append(b)
        graph[b].append(a)

    from collections import deque
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # BFS
    while queue:
        cur = queue.popleft()

        if cur == goal:
            break

        for neigh in graph[cur]:
            if neigh not in visited:
                visited.add(neigh)
                parent[neigh] = cur
                queue.append(neigh)

    # If goal not reached
    if goal not in parent:
        return []

    # Reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    return list(reversed(path))
