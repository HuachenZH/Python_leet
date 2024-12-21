import numpy as np
import re



def count_groups_in_delta(arr_delta:np.ndarray) -> int:
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




arr_delta = np.array([0, 1, 1, -1, -1, 1, 1, 0, 0, 1, 0]) # 4
arr_delta = np.array([0, 1, 1, 0,0, -1, -1, 0]) # 2
arr_delta = np.array([0,1,1,0,0,1,1,0]) # 2 
arr_delta = np.array([0,0,1,1,1,0,0,0]) # 1
arr_delta = np.array([0,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,0,0,1,1,0])  # 5

count_groups_in_delta(arr_delta)


