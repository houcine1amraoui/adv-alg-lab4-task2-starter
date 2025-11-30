class Graph:
    def __init__(self):
        # adjacency list: each key is a node, value is a list of neighbors
        self.adj = {}

    # ADD NODE
    def add_node(self, node):
        # If node not in adjacency list:
        #       create entry: node → empty list
        pass

    # ADD EDGE (undirected)
    def add_edge(self, u, v):
        # Ensure both u and v exist (reuse add_node)
        # Add v to u's adjacency list
        # Add u to v's adjacency list
        pass

    # BFS TRAVERSAL
    def bfs(self, start):
        # 1. Create a queue (list)
        # 2. Create a visited set
        # 3. Add start to queue and mark visited
        # 4. Create an empty result list
        #
        # 5. While queue not empty:
        #       - Pop first element
        #       - Add to result
        #       - For each neighbor:
        #             * If not visited:
        #                   - mark visited
        #                   - add to queue
        #
        # 6. Return result list
        pass

    # DFS TRAVERSAL (recursive)
    def dfs(self, start):
        # 1. Create an empty result list
        # 2. Create a visited set
        #
        # 3. Define helper dfs_visit(node):
        #       - Mark node visited
        #       - Add node to result
        #       - For each neighbor:
        #             * If not visited → recursive call
        #
        # 4. Call dfs_visit(start)
        # 5. Return result
        pass
