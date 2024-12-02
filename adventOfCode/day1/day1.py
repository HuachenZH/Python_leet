import pandas as pd



def read_input(path:str) -> str:
    df = pd.read_csv(path, sep=" ")
    return df



def main():
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

    #breakpoint()



if __name__ == "__main__":
    main()

