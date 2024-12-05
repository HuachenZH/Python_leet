from collections import defaultdict

def build_graph(rules):
    """Builds a DAG (Directed Acyclic Graph) from the rules."""
    graph = defaultdict(list)
    for u, v in rules:
        graph[u].append(v)
    return graph

def is_valid_topological_order(graph, sample_data):
    """
    Verifies if the sample data is a valid topological order for the DAG.
    - graph: adjacency list representing the DAG.
    - sample_data: the sequence to verify.
    """
    visited = set()
    sample_set = set(sample_data)  # Only consider nodes in the sample data

    for node in sample_data:
        # Check all prerequisites for this node
        for prereq in graph:
            if prereq in sample_set and node in graph[prereq] and prereq not in visited:
                return False
        visited.add(node)

    return True

# Example usage
if __name__ == "__main__":
    # Define the rules as edges (u -> v means u must come before v)
    rules = [
        (47, 53), (97, 13), (97, 61), (97, 47), (75, 29),
        (61, 13), (75, 53), (29, 13), (97, 29), (53, 29),
        (61, 53), (97, 53), (61, 29), (47, 13), (75, 47),
        (97, 75), (47, 61), (75, 61), (47, 29), (75, 13), (53, 13)
    ]

    # Define the sample data to verify
    sample_data = [75, 47, 61, 53, 29]

    # Build the graph
    graph = build_graph(rules)

    # Verify the sample data
    if is_valid_topological_order(graph, sample_data):
        print("The sample data is a valid topological order.")
    else:
        print("The sample data is NOT a valid topological order.")

