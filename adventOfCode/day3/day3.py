import re
import math



def part_1(data:str) -> int:
    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    # ['mul(970,630)', 'mul(510,304)']
    # -->  [ [970,630] , [510, 304] ]
    # --> [ 970*630  ,  510*304 ]
    # --> sum
    res = sum([  math.prod([ int(num_pair) for num_pair in re.findall(r"\d{1,3}", mul) ]) for mul in muls])
    return res



def part_2(data:str):
    # add "do()" at the beginning of string
    data = "do()" + data

    # for debugging purpose
    #debug__data_false = data
    #debug__do_false = re.findall(r"do\(\).*?don't\(\)", data_false)
    #debug__res_false = part_1("_".join(do_false))

    data = data.replace("\n", "")
    # match all between do() and don't(), ungreedy
    do = re.findall(r"do\(\).*?don't\(\)", data)
    res = part_1("_".join(do))

    #debug__breakpoint()    

    return res



def main():
    with open("data.txt", "r") as f:
        data = f.read()
    # res looks like:
    # ['mul(970,630)', 'mul(510,304)']

    print(part_1(data))

    print(part_2(data))



if __name__ == "__main__":
    main()


# part 2 failure root cause:
# in first version, 
#   data = data.replace("\n", "")
# I didn't have this line
# as consequence, 
#   do = re.findall(r"do\(\).*?don't\(\)", data)
# do is a list, it will have one element less than correct answer

# However if you put
#   res = part_1("\n".join(do))
# instead of
#   res = part_1("_".join(do))
# it still works
# yeah it's normal cuz the "mul"s already encapsulated between do and don't


# to understand why we need to remove \n inside text:
#  >>> stringg = "tifa\nthis is stuff\naerith"
#  >>> stringg
#  'tifa\nthis is stuff\naerith'
#  >>> import re
#  >>> re.findall(r"tifa.*aerith", stringg)
#  []
#  >>> stringg2 = stringg.replace("\n", "")
#  >>> re.findall(r"tifa.*aerith", stringg2)
#  ['tifathis is stuffaerith']
#  >>>
