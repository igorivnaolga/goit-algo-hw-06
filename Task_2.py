from collections import deque
import networkx as nx

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited  

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(list(graph[vertex])))

G = nx.Graph()
nodes = ["Christchurch", "Dunedin", "Kaikoura", "Nelson", "Wanaka", "Queenstown"]
G.add_nodes_from(nodes)

G.add_edges_from([
    ("Christchurch", "Dunedin", {"weight": 361}),
    ("Christchurch", "Kaikoura", {"weight": 183}),
    ("Christchurch", "Nelson", {"weight": 417}),
    ("Christchurch", "Queenstown", {"weight": 487}),
    ("Christchurch", "Wanaka", {"weight": 428}),
    ("Dunedin", "Kaikoura", {"weight": 545}),
    ("Dunedin", "Nelson", {"weight": 790}),
    ("Dunedin", "Queenstown", {"weight": 281}),
    ("Dunedin", "Wanaka", {"weight": 276}),
    ("Kaikoura", "Nelson", {"weight": 245}),
    ("Kaikoura", "Queenstown", {"weight": 669}),
    ("Kaikoura", "Wanaka", {"weight": 607}),
    ("Nelson", "Queenstown", {"weight": 850}),
    ("Nelson", "Wanaka", {"weight": 809}),
    ("Queenstown", "Wanaka", {"weight": 117}),
])

print("BFS for Graph:", end=" ")
bfs_iterative(G, "Christchurch")
print()
# Starts from Christchurch.
# All direct neighbors: Dunedin, Kaikoura, Nelson, Queenstown, Wanaka.
# They are all added to the queue immediately after the first node.
# Then the neighbors of these nodes are considered — but only after all nodes on the first level have been visited.
# Thus, the result is breadth-first, where each level is fully visited before moving on to the next.

print("DFS for Graph:", end=" ")
dfs_iterative(G, "Christchurch")
print()
# Starts from Christchurch.
# Immediately goes down the deepest possible path.
# Only after reaching a “dead end” does it backtrack and go to other neighbors.
# Therefore, the result is depth-first, where one path is explored to the end before moving on to others.

