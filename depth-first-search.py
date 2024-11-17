class GraphDFS:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.V
        self.dfs_util(start_vertex, visited)
