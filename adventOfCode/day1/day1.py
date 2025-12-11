import pandas as pd



def read_input(path:str) -> str:
    df = pd.read_csv(path, sep=" ")
    return df



def part_1():
    df = read_input("input.txt")

    list_tmp = df["tifa"].to_list()
    list_tmp.sort()
    df["tifa"] = list_tmp
    
    list_tmp = df["aerith"].to_list()
    list_tmp.sort()
    df["aerith"] = list_tmp

    df["res"] = ((df["tifa"] - df["aerith"])**2)**0.5
    int_res = int(df["res"].sum())
    print(int_res)



def part_2():
    df = read_input("input.txt")
    tifa = df["tifa"].to_list()
    aerith = df["aerith"].to_list()
    print(sum([left * aerith.count(left) for left in tifa]))




if __name__ == "__main__":
    part_2()

