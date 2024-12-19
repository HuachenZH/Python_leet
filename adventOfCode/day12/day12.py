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



def construct_clusters_of_flower(coords:set) -> list[set[tuple]]:
    test_list = list(coords)

    # Group Adjacent Coordinates
    # Using product() + groupby() + list comprehension
    man_tups = [sorted(sub) for sub in product(test_list, repeat = 2)
                                            if Manhattan(*sub) == 1]
    man_tups = man_tups * 10 # 1471452 improvement_1
    res_dict = {ele: {ele} for ele in test_list}
    for tup1, tup2 in man_tups:
        res_dict[tup1] |= res_dict[tup2]
        res_dict[tup2] = res_dict[tup1]

    res = [{*next(val)} for key, val in groupby(
            sorted(res_dict.values(), key = id), id)]
    res2 = []
    for elem in res:
        if elem not in res2:
            res2.append(elem)
    

    # printing result 
    #print("The grouped elements : " + str(res)) 
    return res2




def calculate_perimeter(one_cluster:set[tuple]):
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
    price = 0
    for flower in set_flowers:
        print(f"Flower: {flower}")
        set_coords = get_coords_of_flower(arr_data, flower)
        list_clusters = construct_clusters_of_flower(set_coords)
        if flower == "A":
            breakpoint()
        for i,cluster in enumerate(list_clusters):
            print(f"    cluster {i}:")
            perim = calculate_perimeter(cluster)
            price += perim * len(cluster)
            print(f"    perim is {perim}")
    print(price)



def main():
    path = "data.txt"
    part_1(path)
    #debug_flower("data.txt", "debug.txt", "A")



if __name__ == "__main__":
    main()


# Needs to improve
# improvement_1 : see methods.md, to bypass the error, 
# i multiplied man_tups by 10.
# the true problem is at:
#    res = [{*next(val)} for key, val in groupby(
#            sorted(res_dict.values(), key = id), id)]