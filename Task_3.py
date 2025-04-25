import networkx as nx

# Graph setup
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

# Get all shortest paths from 'Christchurch'
shortest_paths = nx.single_source_dijkstra_path(G, source='Christchurch')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='Christchurch')

print("Shortest paths:")
for target, path in shortest_paths.items():
    print(f"{target}: {path}")

print("\nShortest path lengths:")
for target, length in shortest_path_lengths.items():
    print(f"{target}: {length}")
