from collections import defaultdict



def part_1():
    with open("sample.txt") as f:
        data = f.read().strip()
    rules =  [ tuple([int(num) for num in rule.split("|")]) for rule in data.split("\n\n")[0].strip().split("\n")  ]
    data = data.split("\n\n")[1].strip().split("\n")

    # Construct rule of graphs
    graph = defaultdict(list)
    for u,v in rules:
        graph[u].append(v)
    
    # Check data against graph
    for node in 

    breakpoint()



def main():
    part_1()



if __name__ == "__main__":
    main()



