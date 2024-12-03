

def read_and_structure_input(path:str) -> list[list[str]]:
    with open(path, "r") as f:
        return [tifa.strip().split(" ") for tifa in f]



def check_safety_of_report(list_report:list[int]) -> bool:
    list_delta = [list_report[i+1] - list_report[i]    for i in range(len(list_report)-1)]

    print(" ")
    print("\tinside check_safety_of_report")
    print(f"\tinput is {list_report}")
    
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
    #__if min_ < 1 or max_ > 3:
    #__    return False
    #__return True
    if min_ >=1 and max_ <= 3:
        return True
    return False


def main():
    path = "data.txt"
    list_input = read_and_structure_input(path)
    int_res = 0
    #global list_report # for debugging
    for list_report in list_input:
        list_report = [int(tifa) for tifa in list_report]
        if check_safety_of_report(list_report):
            int_res -=- 1
            continue
        else:
            for i in range(len(list_report)):
                sliced = list_report[i]
                list_tmp = list_report[0:i] + list_report[i+1:]
                print("\n----")
                print(list_report)
                print(sliced)
                print(list_tmp)
                if check_safety_of_report(list_tmp):
                    int_res -=- 1
                    continue
                #breakpoint()
    print(int_res)



if __name__ == "__main__":
    main()

