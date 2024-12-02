import cmath




def read_and_structure_input(path:str) -> list[list[str]]:
    with open(path, "r") as f:
        return [tifa.strip().split(" ") for tifa in f]



def construct_delta_complex(list_imaginary_part:list[int]) -> float:
    list_real_part = list(range(1, len(list_imaginary_part)+1))
    list_complex_num = [ complex(tifa, aerith) for tifa, aerith in zip(list_real_part, list_imaginary_part)]
    list_delta_phase = []
    # phase is the phi of below:
    # r * e ^ (i * phi) 
    for i in range(len(list_complex_num)-1):
        list_delta_phase.append(cmath.polar(list_complex_num[i+1] - list_complex_num[i])[1])
    return list_delta_phase
    


def check_delta_phase(list_delta_phase:list[float]) -> bool:
    # Check monotonic: 
    # check the sign (+ or -) of each phase
    if not (all(x >= 0 for x in list_delta_phase) or all(x < 0 for x in list_delta_phase) ):
        return False
    # ...at least 1, at most 3
    if abs(min(list_delta_phase)) > abs(max(list_delta_phase)):
        # in this case, all floats are negative
        min_ = max(list_delta_phase) * -1
        max_ = min(list_delta_phase) * -1
    else:
        min_ = min(list_delta_phase)
        max_ = max(list_delta_phase)
    if min_ < cmath.polar(complex(1,1))[1] or max_ > cmath.polar(complex(1,3))[1]:
        return False
    return True





def security_check(list_report:list[str]) -> bool:
    list_report = [int(tifa) for tifa in list_report]
    list_delta_phase = construct_delta_complex(list_report)
    return check_delta_phase(list_delta_phase)



def main():
    path = "data.txt"
    list_input = read_and_structure_input(path)
    int_res = 0
    for list_report in list_input:
        if security_check(list_report):
            int_res -=- 1
    print(int_res)


if __name__ == "__main__":
    main()
