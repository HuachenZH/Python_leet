import re
import math


def main():
    with open("data.txt", "r") as f:
        data = f.read()
    res = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    # res looks like:
    # ['mul(970,630)', 'mul(510,304)']


    # ['mul(970,630)', 'mul(510,304)']
    # -->  [ [970,630] , [510, 304] ]
    # --> [ 970*630  ,  510*304 ]
    # --> sum
    tmp = sum([  math.prod([ int(num_pair) for num_pair in re.findall(r"\d{1,3}", mul) ]) for mul in res])
    print(tmp)


    breakpoint()

if __name__ == "__main__":
    main()

