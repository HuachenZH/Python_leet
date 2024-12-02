import cmath
from day2_1 import check_delta_phase


def read_and_structure_input(path:str) -> list[list[str]]:
    with open(path, "r") as f:
        return [tifa.strip().split(" ") for tifa in f]



def construct_delta_complex(list_imaginary_part:list[int]) -> list[float]:
    """
    Constructs a sequence of phase differences between adjacent complex numbers.
    
    Args:
        list_imaginary_part (list[int]): List of imaginary components to construct complex numbers
        
    Returns:
        list[float]: List of phase differences between adjacent complex numbers in the sequence
        
    The function:
    1. Creates complex numbers using sequential real parts (1,2,3...) and provided imaginary parts
    2. Calculates phase differences between adjacent complex numbers
    3. Returns list of phase angles (in radians) between successive complex number differences
    """

    list_real_part = list(range(1, len(list_imaginary_part)+1))
    list_complex_num = [ complex(tifa, aerith) for tifa, aerith in zip(list_real_part, list_imaginary_part)]
    list_delta_phase = []
    # phase is the phi of below:
    # r * e ^ (i * phi) 
    for i in range(len(list_complex_num)-1):
        list_delta_phase.append(cmath.polar(list_complex_num[i+1] - list_complex_num[i])[1])
    return list_delta_phase
    


def index_of_opposing_phase(list_delta_phase):
    for i in range(len(list_delta_phase)-1):
        if list_delta_phase[i] * list_delta_phase[i+1] < 0:
            return i+1



def phase_restructure(list_delta_phase):
    # list_delta_phase: there is one and only one opposing sign
    index_opposing = index_of_opposing_phase(list_delta_phase)
    # combine opposing phase with the previous phase
    # [a, b, c, d, e] =>  [a, b, cd, e] if d is the opposing phase
    if index_opposing == 0:
        res = [ list_delta_phase[0]+list_delta_phase[1] ] + list_delta_phase[2:]
    elif index_opposing == len(list_delta_phase)-1:
        res = list_delta_phase[:-2] + [ list_delta_phase[index_opposing-1] + list_delta_phase[index_opposing] ]
    else:
        res = list_delta_phase[:index_opposing-1] + [ list_delta_phase[index_opposing-1]+list_delta_phase[index_opposing] ] + list_delta_phase[index_opposing+1:]
    return res




def check_delta_phase_part2(list_delta_phase:list[float]) -> bool:
    """
    Validates if a sequence of phase differences meets specific criteria.
  
    Args:
        list_delta_phase (list[float]): List of phase differences between adjacent complex numbers
        
    Returns:
        bool: True if the sequence meets all criteria, False otherwise
        
    The function checks if:
    1. The sequence is monotonic (all phases are either positive or negative)
      <-> "The levels are either all increasing or all decreasing."
    2. The absolute phase values fall within bounds defined by complex numbers (1,1) and (1,3)
      <-> "Any two adjacent levels differ by at least one and at most three."
    """
    # Check monotonic: 
    if list_delta_phase.count(0) > 1: return False
    if list_delta_phase.count(0) == 1:
        list_delta_phase.remove(0)
        return check_delta_phase(list_delta_phase)
    # check the sign (+ or -) of each phase
    if not (all(x >= 0 for x in list_delta_phase) or all(x < 0 for x in list_delta_phase) ):
        # Enter here if phases are not monotinic
        positive = len([aerith for aerith in list_delta_phase if aerith > 0])
        negative = len([aerith for aerith in list_delta_phase if aerith < 0])
        # If more than one (excluded) element have opposing sign, then
        # Your second chance is used up!
        if min(positive, negative) > 1:
            return False
        else:
            return check_delta_phase(phase_restructure(list_delta_phase))

    # Here, monotonic
    # ...at least 1, at most 3
    try:
        min(list_delta_phase)
    except:
        breakpoint()
    if abs(min(list_delta_phase)) > abs(max(list_delta_phase)):
        # in this case, all floats are negative
        min_ = max(list_delta_phase) * -1
        max_ = min(list_delta_phase) * -1
        if min_ < cmath.polar(complex(1,1))[1] or max_ > cmath.polar(complex(1,3))[1]:
            return check_delta_phase(list_delta_phase[1:])
    else:
        min_ = min(list_delta_phase)
        max_ = max(list_delta_phase)
        if min_ < cmath.polar(complex(1,1))[1] or max_ > cmath.polar(complex(1,3))[1]:
            return check_delta_phase(list_delta_phase[:-1])
    return True



def security_check(list_report:list[str]) -> bool:
    list_report = [int(tifa) for tifa in list_report]
    list_delta_phase = construct_delta_complex(list_report)
    return check_delta_phase_part2(list_delta_phase)



def main():
    path = "data.txt"
    list_input = read_and_structure_input(path)
    int_res = 0
    global list_report
    for list_report in list_input:
        if security_check(list_report):
            int_res -=- 1
    print(int_res)


if __name__ == "__main__":
    main()
