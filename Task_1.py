import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add nodes
nodes = ["Christchurch", "Dunedin", "Kaikoura", "Nelson",
         "Wanaka", "Queenstown"]
G.add_nodes_from(nodes)

# Add weighted edges
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

pos = nx.circular_layout(G)  
weights = [G[u][v]['weight'] for u, v in G.edges()] 

plt.figure(figsize=(12, 9))  

# Draw graph with styles
nx.draw(G, pos, with_labels=True,
        node_color='lightblue',
        edge_color=weights,
        width=2,
        edge_cmap=plt.cm.Blues,
        node_size=2500,
        font_size=12)

# Show edge labels (weights)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.6)

plt.title("South Island NZ Road Network")
plt.axis("off")
plt.show()

# Analyses
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

for node, degree in G.degree():
    print(f"Degree of node {node}: {degree}")








