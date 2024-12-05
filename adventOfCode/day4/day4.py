import numpy as np
# input is a square, width = height




def part_1(path:str):
    # Approach:
    # Check to three types: horizontal, vertical, diagonal (/ and \)
    # and each time looking for "XMAS" and "SAMX" (reverse of XMAS)

    with open(path, "r") as f:
        data = f.read().strip() # important: remove tailing \n
    res = 0

    # diag count, use np array
    matrix = np.array([list(line)  for line in data.split("\n")])
    diags = [matrix[::-1,:].diagonal(i) for i in range(-1*(matrix.shape[0]-1), matrix.shape[0])] # diag of \
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[0]-1, -1*matrix.shape[0], -1))   # diaf of /
    diags = "_".join(["".join(n.tolist()) for n in diags])
    res += diags.count("XMAS")
    res += diags.count("SAMX")

    # horizontal count
    res += data.count("XMAS")
    res += data.count("SAMX")

    # vertical count, flip the input diagonally so vertical becomes horizontal
    data_diag_flip = [ "".join( [line[i] for line in data.split("\n")] )   for i in range(len(data.split("\n")[0])) ]
    res += "_".join(data_diag_flip).count("XMAS")
    res += "_".join(data_diag_flip).count("SAMX")
    
    return res



def part_2(path:str):
    with open(path, "r") as f:
        data = f.read().strip()
    res = 0

    width = len(data.split("\n"))
    #tmp = [  [ data.split("\n")[irow-1][icol-1] + data.split("\n")[irow-1][icol+1] + data.split("\n")[irow+1][icol-1] + data.split("\n")[irow+1][icol+1]  for icol in range(1, width-1) if data.split("\n")[irow][icol] == "A"  ] for irow in range(1, width-1)  ]
    tmp = [item for sublist in [  [ data.split("\n")[irow-1][icol-1] + data.split("\n")[irow-1][icol+1] + data.split("\n")[irow+1][icol-1] + data.split("\n")[irow+1][icol+1]  for icol in range(1, width-1) if data.split("\n")[irow][icol] == "A"  ] for irow in range(1, width-1)  ] for item in sublist]

    #tmp = [  [ data.split("\n")[irow-1][icol-1] + data.split("\n")[irow-1][icol+1] + data.split("\n")[irow+1][icol-1] + data.split("\n")[irow+1][icol+1]  for icol in range(1, width-1) if data.split("\n")[irow][icol] == "A"  ] for irow in range(1, width-1)  ]
    #tmp = [item for item in sublist  for sublist in tmp ] # syntax error
    #tmp = [item   for sublist in tmp for item in sublist] # correct

    # to_resume:
    # count correct terms in tmp
    breakpoint()




def main():
    print("part 1:")
    print(part_1("data.txt"))
    print("part 2:")
    print(part_2("sample.txt"))



def test():
    # kudo to https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
    matrix = np.array(
             [[-2,  5,  3,  2],
              [ 9, -6,  5,  1],
              [ 3,  2,  7,  3],
              [-1,  8, -4,  8]])
    
    diags = [matrix[::-1,:].diagonal(i) for i in range(-3,4)]
    diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))
    print([n.tolist() for n in diags])



if __name__ == "__main__":
    main()


# [  "".join( [line[i] for i in range(len(line))] )  for line in data.split("\n")]



