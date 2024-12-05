i feel necessary to write explanation for the future me so here's the doc.  

Upon reading the puzzle, i think i can modeling the question into a linear algebra stuffs. So i discussed with chatgpt and it tells me that it's not linear algebra, it's rather graph theory, and our case corresponds to DAG (Directed acyclic graph)


In part_1, the chunk of code:  
```python
    # Construct rule of graphs
    graph = defaultdict(list)
    for u,v in rules:
        graph[u].append(v)
```
It flattens the rules. Instead of having  
```
47|53
97|13
97|61
97|47
...
75|13
53|1
```
graph will be like:  
defaultdict(<class 'list'>, {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13], 13: []})

It means, for ex, for 97, numbers that are allowed to follow 97 are [13, 61, 47, 29, 53, 75].  

When i iterate through data,  
75,97,47,61,53
still with 97 as example, i only need to check its following numbers. It is followed by 47, 61, 53, and we've seen previously that 47 is not allowed to follow 97.

It's sufficient to look ahead  
```
    75,97,47,61,53
        ^------->
```
no need to look behind
```
    75,97,47,61,53
    <---^
```

About the code, notice that there's a for else clause. Kudo to Claude-3.5-sonnet.
