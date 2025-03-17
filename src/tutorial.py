import graph

test_edges = [(0, 1), (1, 6), (2, 1), (2, 7), (2, 3), (3, 4), (4, 7), (5, 7), (6, 7), (7, 8)]

test_graph = graph.create_graph(test_edges)

test_results = {}

test_results['get_degree node 2'] = graph.get_degree(test_graph, 2)

test_results['dfs node 0'] = graph.dfs_traversal(test_graph, 0)

test_results['bfs node 0'] = graph.bfs_traversal(test_graph, 0)

test_results['shortest_path node 0 ke 8'] = graph.find_shortest_path(test_graph, 0, 8)

graph.visualize_graph(test_graph)

for key, value in test_results.items():
    print(f"{key}: {value}")
