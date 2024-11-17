from collections import defaultdict

class GraphTopologicalSort:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        return stack[::-1]  # Reverse the stack for the final order


# Graph construction based on the image
graph_topo_test = GraphTopologicalSort(9)  # 9 nodes: socks, undershorts, pants, shoes, watch, shirt, belt, tie, jacket

# Adding edges
nodes = {
    "socks": 0, "undershorts": 1, "pants": 2, "shoes": 3,
    "watch": 4, "shirt": 5, "belt": 6, "tie": 7, "jacket": 8
}
graph_topo_test.add_edge(nodes["undershorts"], nodes["pants"])
graph_topo_test.add_edge(nodes["undershorts"], nodes["shoes"])
graph_topo_test.add_edge(nodes["pants"], nodes["belt"])
graph_topo_test.add_edge(nodes["pants"], nodes["shoes"])
graph_topo_test.add_edge(nodes["shirt"], nodes["belt"])
graph_topo_test.add_edge(nodes["shirt"], nodes["tie"])
graph_topo_test.add_edge(nodes["belt"], nodes["jacket"])
graph_topo_test.add_edge(nodes["tie"], nodes["jacket"])
graph_topo_test.add_edge(nodes["socks"], nodes["shoes"])
# 'watch' has no outgoing edges

# Running Topological Sort
topological_order = graph_topo_test.topological_sort()

# Mapping indices back to node names for better readability
node_names = {v: k for k, v in nodes.items()}
sorted_order_named = [node_names[i] for i in topological_order]

# Display the result
print("Topological Sort Order:", sorted_order_named)
