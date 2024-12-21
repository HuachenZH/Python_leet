from numpy.linalg import inv
import numpy as np
import re




def prepare_matrices(vecs:list[tuple[int,int]]) -> tuple[np.ndarray, np.ndarray]:
    """M x = P  where M is a matrix of 2x2, x is a vector of 2x1, P is a matrix of 2x2
    x = M^-1 P"""
    M = np.transpose(np.array(vecs[:2]))
    P = np.array(vecs[-1])
    return M,P



def check_x(M:np.ndarray, x:np.ndarray, P:np.ndarray) -> bool:
    # when x is array([80., 40.]) ,
    # in fact x[1] is 40.00000000000001
    # I ve also seen 69.99999999999999.
    # That's the root cause of why i failed part 1 a thousand times.
    # sorry for checking x in a dirty way: calculate the linear combination in a manual way.

    #if max(x) > 100 or min(x) < 0:
    #    return False
    return (np.around(x[0],0)*M[0][0] + np.around(x[1],0)*M[0][1] == P[0] 
        and np.around(x[0],0)*M[1][0] + np.around(x[1],0)*M[1][1] == P[1] )




def part_1(path:str):
    with open(path, "r") as f:
        #data = [ [int(num) for num in re.findall(r"\d+", row)] for chunk in f.read().strip().split("\n\n") for row in chunk.split("\n") ]
        #data = [ int(num) for chunk in f.read().strip().split("\n\n") for row in chunk.split("\n")  for num in re.findall(r"\d+", row)]
        data = [ [tuple([int(num) for num in re.findall(r"\d+", row)]) for row in chunk.split("\n")] for chunk in f.read().strip().split("\n\n")  ]

    list_can_win = []
    list_all_debug = []
    list_win_debug = []
    for vecs in data:
        M,P = prepare_matrices(vecs)
        x = inv(M) @ P
        print(x)
        list_all_debug.append(tuple(x))
        if check_x(M, x, P):
            list_can_win.append(x)
            list_win_debug.append(tuple(x))
    print(len(list_can_win))
    res = sum(np.array(list_can_win) @ np.array([3,1]))
    breakpoint()

    #res = 0
    #for vect in list_can_win:
    #    res += int(vect[0])*3 + int(vect[1])
    #print(res)
    return res



def main():
    path = "data.txt"
    part_1(path)



if __name__ == "__main__":
    main()