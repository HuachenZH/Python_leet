"""
Disk map: 12345
Disk:  0..111....22222
"""


def diskmap_to_disk(data:str):
    disk = ""
    file_id = 0
    for i,v in enumerate(list(data)):
        if i%2==0:
            disk += str(file_id) * int(v)
            file_id += 1
        else:
            disk += "." * int(v)
    return disk



def part_1(path:str):
    with open(path, "r") as f:
        data = f.read().strip()
    diskmap = diskmap_to_disk(data)
    breakpoint()




def main():
    path = "sample.txt"
    part_1(path)



if __name__ == "__main__":
    main()

