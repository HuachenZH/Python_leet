def count_paths(graph, start, end):
    """recursive, find how many paths are there between start point and end point"""

    # This is the base condition of the recursive function.
    if start == end:
        return 1
    res = 0
    for neighbor in graph.get(start, []):
        # res won't += 1 until the end is reached
        res += count_paths(graph, neighbor, end)
    return res


g = {"A": {"B", "C"},
     "B": {"D", "E"},
     "C": {"E"},
     "D": {"F", "G"},
     "E": {"G"},
     "F": {"H"},
     "G": {"H"}
}

num_paths = count_paths(g, "A",  "H")
print(num_paths)
breakpoint()
