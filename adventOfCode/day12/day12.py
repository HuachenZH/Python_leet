import numpy as np
import re
from itertools import groupby, product



def debug_flower(path_in:str, path_out:str, flower:str) -> None:
    with open(path_in, "r") as f:
        data = f.read().strip()
    garden = re.sub(r"(?!"+flower+r").", ".", data)
    with open(path_out, "w") as f:
        f.write(garden)
    print(f"Garden written to {path_out}")



def Manhattan(tup1, tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])



def get_coords_of_flower(arr_data, flower) -> set[tuple[int,int]]:
    coords = np.where(arr_data==flower)
    coords = np.rot90(np.fliplr(coords))
    coords = {tuple(coord)  for coord in coords}
    return coords



def construct_clusters_of_flower(coords:set) -> list[list[tuple]]:
    test_list = list(coords)

    # Group Adjacent Coordinates
    # Using product() + groupby() + list comprehension
    man_tups = [sorted(sub) for sub in product(test_list, repeat = 2)
                                            if Manhattan(*sub) == 1]
    man_tups += man_tups
    res_dict = {ele: {ele} for ele in test_list}
    for tup1, tup2 in man_tups:
        print(tup1, tup2)
        if tup1==(2,3) and tup2==(2,4):
            #breakpoint()
            pass
        res_dict[tup1] |= res_dict[tup2]
        res_dict[tup2] = res_dict[tup1]
        if tup1==(2,3) and tup2==(2,4):
            #breakpoint()
            pass

    res = [[*next(val)] for key, val in groupby(
            sorted(res_dict.values(), key = id), id)]

    # printing result 
    #print("The grouped elements : " + str(res)) 
    return res




def calculate_perimeter(one_cluster:list):
    perimeter = 0
    for coord in one_cluster:
        neighbors = {(coord[0]+1, coord[1]),
          (coord[0]-1, coord[1]),
          (coord[0], coord[1]+1),
          (coord[0], coord[1]-1)}
        perimeter += 4 - len(set(one_cluster).intersection(neighbors))
    return perimeter




def part_1(path:str) -> None:
    with open(path, "r") as f:
        raw_data = f.read().strip()
        data = [list(row) for row in raw_data.split("\n")]
        set_flowers = set(raw_data.replace("\n", ""))

    arr_data = np.array(data)
    set_coords = get_coords_of_flower(arr_data, "R")
    list_clusters = construct_clusters_of_flower(set_coords)
    perim = calculate_perimeter(list_clusters[0])
    breakpoint()



def main():
    path = "sample.txt"
    part_1(path)
    #debug_flower("sample.txt", "debug.txt", "R")



if __name__ == "__main__":
    main()


