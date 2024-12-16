"""
Disk map: 12345
Disk:  0..111....22222
"""
from tqdm import tqdm



def diskmap_to_disk(data:str) -> list:
    """
    Converts a string representation of a disk map into a list of disk blocks.

    Args:
        data (str): A string containing the disk map, where even indices represent file IDs
                     and odd indices represent empty spaces.

    Returns:
        list: A list representing the disk, with file IDs and empty spaces.
    """
    disk = []
    file_id = 0
    for i,v in enumerate(list(data)):
        if i%2==0:
            disk += [str(file_id)] * int(v)
            file_id += 1
        else:
            disk += ["."] * int(v)
    return disk



def fragment_disk_part1(disk:list) -> list:
    """
    Fragments the disk by moving file blocks to fill empty spaces.

    Args:
        disk (list): A list representing the disk with file IDs and empty spaces.

    Returns:
        list: A list representing the fragmented disk with no trailing empty spaces.
    """
    ...
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

    

def fragment_disk_part2(list_disk) -> list[str]:
    """
    Fragments the disk by moving file blocks to fill empty spaces in a more complex manner:
    instead of moving individual files (eg 1), move the whole file block (eg 111).

    Args:
        list_disk (list): A list representing the disk with file IDs and empty spaces.

    Returns:
        list[str]: A list representing the fragmented disk with file IDs and empty spaces.
    """
    list_desc = list(set(list_disk))
    list_desc.remove(".")
    list_desc = [int(i) for i in list_desc]
    list_desc.sort(reverse=True)
    list_desc = [str(i) for i in list_desc]
    #__print(list_disk)
    #__print("_".join(list_disk))
    for file_id in tqdm(list_desc):
        str_disk = "_".join(list_disk)
        int_need_space = list_disk.count(file_id)
        #breakpoint()
        if "_".join(["."]*int_need_space) in str_disk[: str_disk.find("_".join([file_id]*int_need_space))]:
            str_disk = str_disk.replace("_".join([file_id]*int_need_space), "_".join(["."]*int_need_space))
            str_disk = str_disk.replace("_".join(["."]*int_need_space), "_".join([file_id]*int_need_space), 1)
            #str_disk = str_disk.replace("_".join(["x"]*int_need_space), "_".join(["."]*int_need_space))
            list_disk = str_disk.split("_")
            #__print(f"{file_id} moved")
            #__print("".join(list_disk))
    return list_disk



def calculate_checksum(list_disk_fragmented:list) -> int:
    checksum = sum([i*int(v) for i,v in enumerate(list_disk_fragmented)])
    return checksum



def part_1(path:str):
    with open(path, "r") as f:
        data = f.read().strip()
    list_disk = diskmap_to_disk(data)
    list_disk_fragmented = fragment_disk_part1(list_disk)
    int_checksum = calculate_checksum(list_disk_fragmented)
    print(int_checksum)



def part_2(path:str):
    with open(path, "r") as f:
        data = f.read().strip()
    #data = "23331331214141314026746787"
    list_disk = diskmap_to_disk(data)
    list_disk_fragmented = fragment_disk_part2(list_disk)
    int_checksum = calculate_checksum([0 if x=="." else int(x) for x in list_disk_fragmented])
    print(int_checksum)




def main():
    path = "data.txt"
    #part_1(path)
    part_2(path)



if __name__ == "__main__":
    main()



# part 1
# 90840102756 too low
#   --> root cause: file id can have more than one digit
# 6395800119709 good