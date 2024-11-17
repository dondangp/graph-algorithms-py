# Graph Algorithms Implementation

This repository contains Python implementations of fundamental graph algorithms, including **Topological Sort**, **Depth-First Search (DFS)**, and **Kruskal's Algorithm**. Each algorithm is thoroughly tested using examples derived from well-known problems and standard graph representations.

---

## Algorithms Included

### 1. **Topological Sort**
- **Description**: Orders vertices of a Directed Acyclic Graph (DAG) such that for every directed edge \( u \to v \), \( u \) appears before \( v \).
- **Use Case**: Dependency resolution (e.g., task scheduling, build systems).
- **Example**: The test case uses a dependency graph to determine the topological order of items.

### 2. **Depth-First Search (DFS)**
- **Description**: Traverses a graph by exploring as far as possible along each branch before backtracking.
- **Use Case**: Pathfinding, detecting cycles, and exploring connected components.
- **Example**: The test case uses a directed graph to demonstrate the DFS traversal starting from a specific vertex.

### 3. **Kruskal's Algorithm**
- **Description**: Finds the Minimum Spanning Tree (MST) for a weighted, connected, and undirected graph.
- **Use Case**: Network design (e.g., laying cables, constructing roads).
- **Example**: The test case uses a weighted graph to compute the MST, minimizing the total edge weight.

