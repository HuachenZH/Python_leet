
import numpy as np



def get_coords(data:list[list[int]]):
    heights = set([elem for row in data for elem in row])
    dict_coords = {}
    for height in heights:
        # [[0, 1, 2],
        # [2, 1, 1]]
        tmp = np.array(np.where(data==height))
        breakpoint()
        # [[0, 2],
        # [1, 1],
        # [2, 1]]
        tmp = np.rot90(np.fliplr(tmp))
        dict_coords[height] = [np.array(coord) for coord in tmp]
    return dict_coords




def part_1(path:str):
    with open(path, "r") as f:
        data = [ [int(num) for num in row]  for row in f.read().strip().split("\n")]
    data = np.array(data)
    dict_coords = get_coords(data)
    breakpoint()



def main():
    path = "simple.txt"
    part_1(path)



if __name__ == "__main__":
    main()



# to_resume: construct_graph
