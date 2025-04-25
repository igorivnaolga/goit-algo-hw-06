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

# Calculate shortest paths and distances using Dijkstra
all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G))
all_shortest_distances = dict(nx.all_pairs_dijkstra_path_length(G))

# Display results
for source in G.nodes:
    print(f"\nFrom {source}:")
    for target in G.nodes:
        if source != target:
            path = all_shortest_paths[source][target]
            distance = all_shortest_distances[source][target]
            print(f"  To {target} → Path: {path}, Distance: {distance}")