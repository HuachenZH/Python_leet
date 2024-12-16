
import numpy as np



def get_coords(data:list[list[int]]) -> dict:
    """Extracts coordinates of unique heights from the given 2D list of integers.

    Args:
        data (list[list[int]]): A 2D list representing height values.

    Returns:
        dict: A dictionary where keys are unique heights and values are lists of coordinates (as numpy arrays) where those heights occur.
    """

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
    """Constructs a directed graph from the given coordinates of heights.

    Args:
        dict_coords (dict): A dictionary of coordinates for each height.

    Returns:
        dict: A directed graph represented as a dictionary where keys are coordinates and values are lists of neighboring coordinates.
    """

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
    
    #__for k,v in directed_graph.items():
    #__    print(k,v)
    return directed_graph



def count_paths(graph:dict, start:tuple, end:tuple):
    """Recursively counts the number of paths from the start point to the end point in the graph.
    Written by chatgpt.

    Args:
        graph (dict): The directed graph represented as a dictionary.
        start (tuple): The starting coordinate.
        end (tuple): The ending coordinate.

    Returns:
        int: The number of distinct paths from start to end.
    """

    # This is the base condition of the recursive function.
    if start == end:
        return 1
    res = 0
    for neighbor in graph.get(start, []):
        # res won't += 1 until the end is reached
        res += count_paths(graph, neighbor, end)
    return res




def part_1_and_2(path:str):
    with open(path, "r") as f:
        data = [ [int(num) for num in row]  for row in f.read().strip().split("\n")]
    data = np.array(data)
    dict_coords = get_coords(data)
    zero_nine_pairs =[ [tuple(zero), tuple(nine)] for zero in dict_coords[0] for nine in dict_coords[9] ]
    directed_graph = construct_graph(dict_coords)

    # part 1
    res = sum([1  for pair in zero_nine_pairs if count_paths(directed_graph, pair[0], pair[1])>0])
    print(res)
    # part 2
    res2 = sum([count_paths(directed_graph, pair[0], pair[1])  for pair in zero_nine_pairs ])
    print(res2)



def main():
    path = "sample.txt"
    part_1_and_2(path)



if __name__ == "__main__":
    main()



# to_resume: construct_graph
