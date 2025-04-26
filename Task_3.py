graph = {
    "Christchurch": {"Dunedin": 361, "Kaikoura": 183, "Nelson": 417, "Queenstown": 487, "Wanaka": 428},
    "Dunedin": {"Christchurch": 361, "Kaikoura": 545, "Nelson": 790, "Queenstown": 281, "Wanaka": 276},
    "Kaikoura": {"Christchurch": 183, "Dunedin": 545, "Nelson": 245, "Queenstown": 669, "Wanaka": 607},
    "Nelson": {"Christchurch": 417, "Dunedin": 790, "Kaikoura": 245, "Queenstown": 850, "Wanaka": 809},
    "Wanaka": {"Christchurch": 428, "Dunedin": 276, "Kaikoura": 607, "Nelson": 809, "Queenstown": 117},
    "Queenstown": {"Christchurch": 487, "Dunedin": 281, "Kaikoura": 669, "Nelson": 850, "Wanaka": 117},
}

# Custom Dijkstra
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

# Path reconstruction
def reconstruct_path(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex

        unvisited.remove(current_vertex)

    # Build path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path

# Calculate and display
all_shortest_distances = {}
all_shortest_paths = {}

for source in graph:
    all_shortest_distances[source] = dijkstra(graph, source)
    all_shortest_paths[source] = {target: reconstruct_path(graph, source, target) for target in graph}

for source in graph:
    print(f"\nFrom {source}:")
    for target in graph:
        if source != target:
            path = all_shortest_paths[source][target]
            distance = all_shortest_distances[source][target]
            print(f"  To {target} → Path: {path}, Distance: {distance}")