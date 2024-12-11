import math
import itertools
from tqdm import tqdm




def add_or_mul_or_concat(num1:int, num2:int, operator:str) -> int:
    if operator == "+":
        return num1 + num2
    if operator == "*":
        return num1 * num2
    if operator == "|":
        return int(str(num1)+str(num2))



def part_1_and_2(path_input:str):
    with open(path_input, "r") as f:
        data = f.read().strip().split("\n")
    
    res = 0
    res_set = set()
    for row in tqdm(data):
        target = int(row.split(":")[0])
        nums = [int(num) for num in row.split(":")[1].strip().split(" ")]
        # code below is incorrect, eg  494: 6 2 1 38
        #if sum(nums) > target or math.prod(nums) < target:
        #    continue 
        operators_all_poss = itertools.product("+*|", repeat=len(nums)-1) # list of tuple
        # Apply operators to nums
        for operators in operators_all_poss:
            num_test = nums[0]
            for num, operator in zip(nums[1:], operators):
                num_test = add_or_mul_or_concat(num_test, num, operator)
            if num_test == target:
                res += target
                res_set.add(target)
                break
    print(f"part1: {str(res)}")
    return res_set




def main():
    path_input = "data.txt"
    set1 = part_1_and_2(path_input)



if __name__ == "__main__":
    main()
