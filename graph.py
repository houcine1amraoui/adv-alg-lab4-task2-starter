class Graph:
    def __init__(self):
        # This builds the graph shown in graph.png
        self.adj = {}   # adjacency list
        self.add_edge('1', '2'); self.add_edge('1', '3'); self.add_edge('1', '4')
        self.add_edge('2', '3'); 
        # complete edges addition below

    # Add an undirected edge v1 — v2
    def add_edge(self, v1, v2):
        # Add a node if not already present
        if v1 not in self.adj: self.adj[v1] = []
        if v2 not in self.adj: self.adj[v2] = []
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    # Display adjacency list
    def display(self):
        for v in self.adj:
            print(f"{v} -> {self.adj[v]}")

    def bfs(self, start):
        # Create an empty set to keep track of visited nodes.
        # Create an empty list to store the final traversal order.
        # Create an empty queue for BFS.
        # Add the starting node to the queue and mark it as visited.
        # While the queue is not empty:
            # Remove the first element from the queue (this is the current node).
            # Add the current node to the traversal result.
            # For each neighbor of the current node (exploration):
                # If the neighbor has not been visited yet:
                    # Mark it as visited.
                    # Add it to the queue.
        # Return the traversal result.
        pass
    
    def dfs(self, start):
        # Create an empty set to keep track of visited nodes.
        # Create an empty list to store the traversal order.
        # Define a recursive helper function (call it whatever you like):
            # Mark the current node as visited.
            # Add the current node to the traversal result.
            # Get all neighbors of the current node.
            # Sort the neighbors in ascending numeric order.
            # For each neighbor:
                # If the neighbor has not been visited yet:
                    # Recursively call the helper function on that neighbor.
        # Call the helper function on the start node.
        # Return the traversal result.
        pass