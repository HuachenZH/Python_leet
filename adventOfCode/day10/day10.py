
import numpy as np



def get_coords(data:list[list[int]]) -> dict:
    heights = set([elem for row in data for elem in row])
    dict_coords = {}
    for height in heights:
        # [[0, 1, 2],
        # [2, 1, 1]]
        tmp = np.array(np.where(data==height))
        # [[0, 2],
        # [1, 1],
        # [2, 1]]
        tmp = np.rot90(np.fliplr(tmp))
        dict_coords[height] = [np.array(coord) for coord in tmp]
    return dict_coords



def construct_graph(dict_coords:dict) -> dict:
    keys_ = list(dict_coords.keys())
    keys_.sort()
    directed_graph = {}
    for i in range(len(keys_)-1):
        for arr_point in dict_coords[keys_[i]]:
            #takeaway[tuple(arr_point)] = [ tuple(arr_point_higher)  for arr_point_higher in dict_coords[keys_[i+1]]  if tuple(arr_point_higher-arr_point)==(1,0)  or tuple(arr_point_higher-arr_point)==(0,1)  or tuple(arr_point_higher-arr_point)==(-1,0) or tuple(arr_point_higher-arr_point)==(0,-1) ]
            directed_graph[tuple(arr_point)] = []
            for arr_point_higher in dict_coords[keys_[i+1]]:
                if (tuple(arr_point_higher-arr_point)==(1,0)
                        or tuple(arr_point_higher-arr_point)==(-1,0)
                        or tuple(arr_point_higher-arr_point)==(0,1)
                        or tuple(arr_point_higher-arr_point)==(0,-1) ):
                    directed_graph[tuple(arr_point)].append(tuple(arr_point_higher))
    
    for k,v in directed_graph.items():
        print(k,v)
    return directed_graph



def count_paths(graph, start, end):
    """recursive, find how many paths are there between start point and end point.
    Written by chatgpt."""

    # This is the base condition of the recursive function.
    if start == end:
        return 1
    res = 0
    for neighbor in graph.get(start, []):
        # res won't += 1 until the end is reached
        res += count_paths(graph, neighbor, end)
    return res




def part_1(path:str):
    with open(path, "r") as f:
        data = [ [int(num) for num in row]  for row in f.read().strip().split("\n")]
    data = np.array(data)
    dict_coords = get_coords(data)
    zero_nine_pairs =[ [tuple(zero), tuple(nine)] for zero in dict_coords[0] for nine in dict_coords[9] ]
    directed_graph = construct_graph(dict_coords)
    res = sum([1  for pair in zero_nine_pairs if count_paths(directed_graph, pair[0], pair[1])>0])
    print(res)



def main():
    path = "data.txt"
    part_1(path)



if __name__ == "__main__":
    main()



# to_resume: construct_graph
