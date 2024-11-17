# Test for Topological Sort
def test_topological_sort():
    # Construct the graph based on the example
    graph_topo_test = GraphTopologicalSort(9)  # 9 nodes: socks, undershorts, pants, shoes, watch, shirt, belt, tie, jacket
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

    # Perform Topological Sort
    topological_order = graph_topo_test.topological_sort()

    # Map indices back to node names
    node_names = {v: k for k, v in nodes.items()}
    sorted_order_named = [node_names[i] for i in topological_order]

    # Expected output (from the book's diagram)
    expected_order = ['shirt', 'tie', 'watch', 'undershorts', 'pants', 'belt', 'jacket', 'socks', 'shoes']

    # Assert
    assert sorted_order_named == expected_order, f"Expected {expected_order}, but got {sorted_order_named}"
    print("Topological Sort test passed!")


# Test for Depth-First Search (DFS)
def test_dfs():
    # Construct the graph based on the example
    graph_dfs_test = GraphDFS(6)  # 6 nodes: u, v, w, x, y, z
    nodes = {"u": 0, "v": 1, "w": 2, "x": 3, "y": 4, "z": 5}
    graph_dfs_test.add_edge(nodes["u"], nodes["x"])
    graph_dfs_test.add_edge(nodes["u"], nodes["v"])
    graph_dfs_test.add_edge(nodes["v"], nodes["y"])
    graph_dfs_test.add_edge(nodes["y"], nodes["x"])
    graph_dfs_test.add_edge(nodes["w"], nodes["y"])
    graph_dfs_test.add_edge(nodes["w"], nodes["z"])
    graph_dfs_test.add_edge(nodes["z"], nodes["z"])

    # Perform DFS starting from 'u'
    dfs_result_indices = graph_dfs_test.dfs(nodes["u"])

    # Map indices back to node names
    node_names = {v: k for k, v in nodes.items()}
    dfs_result_named = [node_names[i] for i in dfs_result_indices]

    # Expected output (from the book's diagram)
    expected_result = ['u', 'x', 'v', 'y']

    # Assert
    assert dfs_result_named == expected_result, f"Expected {expected_result}, but got {dfs_result_named}"
    print("DFS test passed!")


# Run the tests
if __name__ == "__main__":
    test_topological_sort()
    test_dfs()
