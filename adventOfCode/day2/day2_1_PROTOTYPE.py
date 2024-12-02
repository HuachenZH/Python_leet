

def read_and_structure_input(path:str) -> list[list[str]]:
    with open(path, "r") as f:
        return [tifa.strip().split(" ") for tifa in f]



def check_safety_of_report(list_report:list[int]) -> bool:
    list_delta = [list_report[i+1] - list_report[i]    for i in range(len(list_report)-1)]
    
    # Check monotonic, return false if not monotonic
    if not (all(x >= 0 for x in list_delta) or all(x < 0 for x in list_delta) ):
        return False
    
    # delta should be between 1 and 3
    if abs(min(list_delta)) > abs(max(list_delta)):
        # in this case, all floats are negative
        min_ = max(list_delta) * -1
        max_ = min(list_delta) * -1
    else:
        min_ = min(list_delta)
        max_ = max(list_delta)    
    if min_ < 1 or max_ > 3:
        return False
    return True



def main():
    path = "data.txt"
    list_input = read_and_structure_input(path)
    int_res = 0
    global list_report # for debugging
    for list_report in list_input:
        if check_safety_of_report([int(tifa) for tifa in list_report]):
            int_res -=- 1
    print(int_res)



if __name__ == "__main__":
    main()

