import re
import numpy as np





def predict_position(init_pos:int, velocity:int, window:int, sec:int) -> int:
    res = (velocity*sec+init_pos) % window
    return res



def part_1(path:str, width:int, height:int, sec:int):
    # height <=> row <=> y axis
    # width  <=> col <=> x axis
    with open(path, "r") as f:
        data = [  [tuple([int(num) for num in found.split(",")]) for found in re.findall(r'-?\d{1,3},-?\d{1,3}', line)]   for line in f.read().strip().split("\n")]

    floor = np.zeros((height, width))
    for tup_init_pos, tup_velocity in data:
        end_pos_x = predict_position(tup_init_pos[0], tup_velocity[0], width, sec)
        end_pos_y = predict_position(tup_init_pos[1], tup_velocity[1], height, sec)
        #floor[height-end_pos_y-1][end_pos_x] += 1
        floor[end_pos_y][end_pos_x] += 1

    mid_row = int((floor.shape[0]-1)/2)
    mid_col = int((floor.shape[1]-1)/2)
    res = 1
    # 1 | 2 
    # --|--
    # 3 | 4
    # "Quadrant" °1
    res *= int(sum(sum(floor[:mid_row, :mid_col ])))
    # "Quadrant" °2
    res *= int(sum(sum(floor[:mid_row, mid_col+1: ])))
    # "Quadrant" °3
    res *= int(sum(sum(floor[mid_row+1:, :mid_col ])))
    # "Quadrant" °4
    res *= int(sum(sum(floor[mid_row+1:, mid_col+1: ])))
    print(res)

    return floor



def part_2(path:str, width:int, height:int, sec:int):
    floor = part_1(path, width, height, sec)
    floor = floor.tolist()
    res = ""
    for row in floor:
        for col in row:
            if col == 0:
                res += " "
            else:
                res += "@"
        res += "\n"
    res = res.strip()
    print(res)
    #path_out = "out_egg.txt"
    #with open(path_out, "w") as f:
    #    f.write(res)
    #print(f"Egg written to {path_out}")
    




def main():
    #path = "sample.txt"
    #width = 11
    #height = 7
    path = "data.txt"
    width = 101
    height = 103
    sec = 1000
    part_1(path, width, height, sec)


    part_2(path, width, height, sec)



if __name__ == "__main__":
    main()


