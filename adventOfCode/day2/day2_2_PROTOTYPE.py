

def read_and_structure_input(path:str) -> list[list[str]]:
    with open(path, "r") as f:
        return [elem.strip().split(" ") for elem in f]



def check_safety_of_report(list_report:list[int]) -> bool:
    list_delta = [list_report[i+1] - list_report[i]    for i in range(len(list_report)-1)]

    #__print(" ")
    #__print("\tinside check_safety_of_report")
    #__print(f"\tinput is {list_report}")
    
    # Check monotonic, return false if not monotonic
    if not (all(x >= 0 for x in list_delta) or all(x < 0 for x in list_delta) ):
        return False
    
    # delta should be between 1 and 3
    # if abs(min(list_delta)) > abs(max(list_delta)): # ERROR!!
    if max(list_delta) < 0:
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


def prototype():
    path = "data.txt"
    list_input = read_and_structure_input(path)
    #list_input = [[51, 51, 50, 49, 48]]
    int_res = 0
    list_res = []
    #global list_report # for debugging
    for list_report in list_input:
        list_report = [int(elem) for elem in list_report]
        if check_safety_of_report(list_report):
            int_res += 1
            list_res.append("_".join([str(elem) for elem in list_report]))
            continue
        
        for i in range(len(list_report)):
            list_tmp = list_report[0:i] + list_report[i+1:]
            if check_safety_of_report(list_tmp):
                int_res += 1
                list_res.append("_".join([str(elem) for elem in list_report]))
                break
                #breakpoint()
    print(int_res)
    return list_res



def test():
    list_test = [51, 50, 49, 48]
    check_safety_of_report(list_test)




if __name__ == "__main__":
    prototype()
    #test()


# mine: 417, correct: 418
# problem at: [[51, 51, 50, 49, 48]]
# after slicing the first element, [51, 50, 49, 48]
# list_delta is [-1, -1, -1]
    # if abs(min(list_delta)) > abs(max(list_delta)): # ERROR!!
# the line above does not work as expected