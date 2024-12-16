
import numpy as np



def part_1(path:str):
    with open(path, "r") as f:
        data = [ [int(num) for num in row]  for row in f.read().strip().split("\n")]
    data = np.array(data)
    breakpoint()



def main():
    path = "simple.txt"
    part_1(path)



if __name__ == "__main__":
    main()

