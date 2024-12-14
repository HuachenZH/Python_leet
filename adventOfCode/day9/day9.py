"""
Disk map: 12345
Disk:  0..111....22222
"""


def diskmap_to_disk(data:str) -> list:
    disk = []
    file_id = 0
    for i,v in enumerate(list(data)):
        if i%2==0:
            disk += [str(file_id)] * int(v)
            file_id += 1
        else:
            disk += ["."] * int(v)
    return disk



def fragment_disk(disk:list) -> list:
    # normally there isn't any tailing "."
    #__print(disk)
    while "." in disk:
        if disk[-1] == ".":
            #__print("remove tailing '.'")
            disk = disk[:-1]
            #__print(disk)
        else:
            #__print("move file block")
            disk[disk.index(".")] = disk[-1]
            #disk = disk.replace(".", disk[-1], 1)
            disk = disk[:-1]
            #__print(disk)
    return disk

    

def calculate_checksum(list_disk_fragmented:list) -> int:
    checksum = sum([i*int(v) for i,v in enumerate(list_disk_fragmented)])
    return checksum



def part_1(path:str):
    with open(path, "r") as f:
        data = f.read().strip()
    list_disk = diskmap_to_disk(data)
    list_disk_fragmented = fragment_disk(list_disk)
    int_checksum = calculate_checksum(list_disk_fragmented)
    print(int_checksum)




def main():
    path = "data.txt"
    part_1(path)



if __name__ == "__main__":
    main()



# part 1
# 90840102756 too low
# 6395800119709 good