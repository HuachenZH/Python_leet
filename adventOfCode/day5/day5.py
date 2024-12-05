from collections import defaultdict



def part_1(path:str):
    with open(path) as f:
        data = f.read().strip()
    rules =  [ tuple([int(num) for num in rule.split("|")]) for rule in data.split("\n\n")[0].strip().split("\n")  ]
    data = [  [ int(elem) for elem in line.split(',')  ] for line in  data.split("\n\n")[1].strip().split("\n")   ]

    # Construct rule of graphs
    graph = defaultdict(list)
    for u,v in rules:
        graph[u].append(v)

    # Check data against graph
    data_correct = []
    for line in data:
        for index, node in enumerate(line):
            if not set(line[index+1:]).issubset(set(graph[node])):
                break
        else:
            data_correct.append(line)
    res = sum([line[int((len(line)-1)/2)]  for line in data_correct])
    return res



def main():
    print(part_1("sample.txt"))



if __name__ == "__main__":
    main()



