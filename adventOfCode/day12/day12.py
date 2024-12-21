import numpy as np
import re
from itertools import groupby, product
import unittest



class TestFlowerGarden_part1(unittest.TestCase):
    
    def test_with_sample_data(self):
        path = "sample.txt"
        expected_output = 1930
        self.assertEqual(part_1_and_2(path), expected_output)

    def test_with_data_data(self):
        path = "data.txt"
        expected_output = 1471452
        self.assertEqual(part_1_and_2(path), expected_output)





def debug_flower(path_in:str, path_out:str, flower:str) -> None:
    """Helps visualize a flower of the garden"""
    with open(path_in, "r") as f:
        data = f.read().strip()
    garden = re.sub(r"(?!"+flower+r").", ".", data)
    with open(path_out, "w") as f:
        f.write(garden)
    print(f"Garden written to {path_out}")



def Manhattan(tup1, tup2) -> int:
    """Calculates the Manhattan distance between two tuples.

    Args:
        tup1 (tuple): The first coordinate as a tuple (x1, y1).
        tup2 (tuple): The second coordinate as a tuple (x2, y2).

    Returns:
        int: The Manhattan distance between the two coordinates.
    """
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])



def get_coords_of_flower(arr_data, flower) -> set[tuple[int,int]]:
    """Finds the coordinates of a specified flower in the garden array.

    Args:
        arr_data (np.ndarray): The array representation of the garden.
        flower (str): The flower character to search for.

    Returns:
        set[tuple[int,int]]: A set of tuples representing the coordinates of the flower.
    """
    coords = np.where(arr_data==flower)
    coords = np.rot90(np.fliplr(coords))
    coords = {tuple(coord)  for coord in coords}
    return coords



def construct_clusters_of_flower(coords:set) -> list[set[tuple]]:
    """Groups adjacent flower coordinates into clusters.

    Args:
        coords (set): A set of flower coordinates.

    Returns:
        list[set[tuple]]: A list of sets, where each set contains coordinates of a flower cluster.
    """
    test_list = list(coords)

    # Group Adjacent Coordinates
    # Each tuple will meet every other tuple in the list,
    # only the pairs whose Manhattan distance is 1 will be kept.
    # This means we are only considering adjacent coordinates (up, down, left, right).
    # man_tups is composed of pairs of adjacent points.
    man_tups = [sorted(sub) for sub in product(test_list, repeat = 2)
                                            if Manhattan(*sub) == 1]
    #man_tups = man_tups * 10 # 1471452 improvement_1

    res_dict = {ele: {ele} for ele in test_list}
    
    # At the end of the for loop, about res_dict:
    # key: each tuple,
    # value: a list of all the tuples in the same cluster as the key.
    for tup1, tup2 in man_tups:
        res_dict[tup1] |= res_dict[tup2]
        #res_dict[tup2] = res_dict[tup1]

        # Update each neighbor of tup1 to ensure they are in the same cluster,
        # as they are all connected through tup1.
        for adjacent in res_dict[tup1]:
            res_dict[adjacent] = res_dict[tup1]

    res = [{*next(val)} for key, val in groupby(
            sorted(res_dict.values(), key = id), id)]
    #res2 = []
    #for elem in res:
    #    if elem not in res2:
    #        res2.append(elem)

    # printing result 
    #print("The grouped elements : " + str(res)) 
    return res



# for part 1
def calculate_perimeter(one_cluster:set[tuple]) -> int:
    """Calculates the perimeter of a given flower cluster.

    Args:
        one_cluster (set[tuple]): A set of coordinates representing the flower cluster.

    Returns:
        int: The calculated perimeter of the cluster.
    """
    perimeter = 0
    for coord in one_cluster:
        neighbors = {(coord[0]+1, coord[1]),
          (coord[0]-1, coord[1]),
          (coord[0], coord[1]+1),
          (coord[0], coord[1]-1)}
        perimeter += 4 - len(set(one_cluster).intersection(neighbors))
    return perimeter




def cluster_to_matrix(one_cluster:set[tuple]) -> np.ndarray:
    """Transforms a flower cluster into a binary matrix representation.

    Args:
        one_cluster (set[tuple]): A set of coordinates representing the flower cluster.

    Returns:
        np.ndarray: A 2D binary matrix where 1 represents flower and 0 represents empty space.
    """
    arr_coords = np.array(list(one_cluster))
    arr_coords[:,0] = arr_coords[:,0] - min(arr_coords[:,0])
    arr_coords[:,1] = arr_coords[:,1] - min(arr_coords[:,1])
    # number of row <-> height
    # the +2 at the end is to add two emtpy col/row
    height = max(arr_coords[:,0]) - min(arr_coords[:,0]) + 1 +2
    # number of col <-> width
    width = max(arr_coords[:,1]) - min(arr_coords[:,1]) + 1 +2

    # construct matrix
    #mat = [ [0]*width ] * height
    mat = np.zeros((height, width), dtype=int)
    for coord in arr_coords:
        mat[coord[0]+1][coord[1]+1] = 1
    return mat



def count_groups_in_delta(arr_delta:np.ndarray) -> int:
    """Counts the number of groups of sides in the delta array.
    A few examples can help understand:
    0  1  1  1  1  1  1  0 -> returns 1
    0  1  1  1 -1 -1 -1  0 -> returns 2
    0  1  1  0 -1 -1 -1  0 -> returns 2
    0  0  0  1  1  1  0  0 -> returns 1

    Args:
        arr_delta (np.ndarray): An array representing the difference between two rows of the matrix.
        the first and last element of arr_delta is always 0.
        Possible values: 0, 1, -1

    Returns:
        int: The total number of groups of sides found in the delta.
    """
    tmp = [" " if num==0  else "a" if num==1 else "b" for num in arr_delta]
    tmp = "".join(tmp).strip()
    print(arr_delta)
    print(tmp)
    tmp = re.sub(" +", " ", tmp)
    tmp = re.sub("a+", 'A', tmp)
    tmp = re.sub("b+", 'B', tmp)
    tmp = tmp.split(" ")
    print(tmp)

    res = sum([len(group) for group in tmp ])
    print(res)
    return res



def vertical_scan(mat:np.array) -> int:
    """Performs a vertical scan on the matrix to count the number of sides
    within the direction of scan.

    Args:
        mat (np.ndarray): The binary matrix representation of the flower cluster.

    Returns:
        int: The total number of sides detected in the matrix.
    """
    nb_sides = 0
    print(mat)
    for i in range(1, len(mat)):
        # arr_delta is composed of 0, -1 and 1
        arr_delta = mat[i] - mat[i-1]
        # if there are 1 or -1 in arr_delta, then (a) side(s) is/are appeard
        if sum([abs(num) for num in arr_delta]) > 0:
            # if 1 are truncated by 0, then there are several sides
            # 0 1 1 0 0 1 1 <=> two sides
            nb_sides += count_groups_in_delta(arr_delta)
            # nb_sides += len("".join([str(num) for num in list(arr_delta)]).replace("0", " ").strip().split(" "))
    print(nb_sides)
    print(" ")
    return nb_sides



# for part 2
def count_sides(one_cluster:set[tuple]) -> int:
    """Counts the total number of sides for a given flower cluster.

    Args:
        one_cluster (set[tuple]): A set of coordinates representing the flower cluster.

    Returns:
        int: The total number of sides for the cluster.
    """
    mat = cluster_to_matrix(one_cluster)
    nb_sides = vertical_scan(mat)
    # in fact rot90 is sufficient, fliplr is not necessary.
    nb_sides += vertical_scan(np.rot90(np.fliplr(mat)))
    print(nb_sides)
    return nb_sides




def part_1_and_2(path:str) -> None:
    with open(path, "r") as f:
        raw_data = f.read().strip()
        data = [list(row) for row in raw_data.split("\n")]
        set_flowers = set(raw_data.replace("\n", ""))

    arr_data = np.array(data)
    price = 0
    for flower in set_flowers:
        #__print(f"Flower: {flower}")
        #tmp for build
        #flower = 'A'
        set_coords = get_coords_of_flower(arr_data, flower)
        list_clusters = construct_clusters_of_flower(set_coords)
        for i,cluster in enumerate(list_clusters):
            #__print(f"    cluster {i}:")
            # part 1
            perim = calculate_perimeter(cluster)
            # part 2
            perim = count_sides(cluster)
            price += perim * len(cluster)
            #__print(f"    perim is {perim}")
    print(price)
    return price



def main():
    path = "data.txt"
    part_1_and_2(path)
    #debug_flower("data.txt", "debug.txt", "A")



if __name__ == "__main__":
    main()
    #unittest.main()

# Needs to improve
# improvement_1 : see methods.md, to bypass the error, 
# i multiplied man_tups by 10.
# the true problem is at:
#    res = [{*next(val)} for key, val in groupby(
#            sorted(res_dict.values(), key = id), id)]