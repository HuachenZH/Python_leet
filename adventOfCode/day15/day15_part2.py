from day15_part1 import transpose_warehouse
from day15_part1 import get_robot_position


with open("data/data_warehouse_part1.txt", "r") as f:
    # list[list[str]]
    WAREHOUSE_INIT = [ list(row) for row in f.read().strip().split("\n") ]
with open("data/data_movements_part1.txt", "r") as f:
    MOVEMENTS = "".join(f.read().strip().split("\n")) # str




