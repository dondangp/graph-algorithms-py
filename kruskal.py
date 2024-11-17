# Re-defining the GraphKruskal class for Kruskal's Algorithm implementation

class GraphKruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        self.edges.sort()
        parent = []
        rank = []
        mst = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        for edge in self.edges:
            weight, u, v = edge
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst.append((u, v, weight))
                self.union(parent, rank, x, y)

        return mst


# Reconstructing the graph from the image for Kruskal's Algorithm
graph_kruskal_test = GraphKruskal(9)  # 9 nodes: a, b, c, d, e, f, g, h, i

# Adding edges with weights as per the image
nodes = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8}
graph_kruskal_test.add_edge(nodes["a"], nodes["b"], 4)
graph_kruskal_test.add_edge(nodes["a"], nodes["h"], 8)
graph_kruskal_test.add_edge(nodes["b"], nodes["h"], 11)
graph_kruskal_test.add_edge(nodes["b"], nodes["c"], 8)
graph_kruskal_test.add_edge(nodes["c"], nodes["i"], 2)
graph_kruskal_test.add_edge(nodes["c"], nodes["f"], 4)
graph_kruskal_test.add_edge(nodes["c"], nodes["d"], 7)
graph_kruskal_test.add_edge(nodes["d"], nodes["f"], 14)
graph_kruskal_test.add_edge(nodes["e"], nodes["f"], 10)
graph_kruskal_test.add_edge(nodes["g"], nodes["f"], 2)
graph_kruskal_test.add_edge(nodes["g"], nodes["h"], 1)
graph_kruskal_test.add_edge(nodes["h"], nodes["i"], 7)
graph_kruskal_test.add_edge(nodes["i"], nodes["g"], 6)

# Running Kruskal's Algorithm to find the MST
mst_result = graph_kruskal_test.kruskal()

# Mapping indices back to node names for better readability
node_names = {v: k for k, v in nodes.items()}
mst_result_named = [(node_names[u], node_names[v], weight) for u, v, weight in mst_result]

mst_result_named
