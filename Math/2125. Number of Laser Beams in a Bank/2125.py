class Solution:
    def numberOfBeamsBeta(self, bank: list[str]) -> int:
        # default of ver alpha: no need to iterate so many times
        # better solution for counting occurence of "1": use string.count()
        nbBeams = 0
        # find rows where it contains 1
        rowsWithSec = []
        for index, row in enumerate(bank):
            if "1" in row:
                rowsWithSec.append(index)
        print(rowsWithSec)
        # then i only need to check those rows with security devices found
        for i in range(len(rowsWithSec)-1):
            nbBeams += bank[rowsWithSec[i]].count("1") * bank[rowsWithSec[i+1]].count("1")
        return nbBeams
    def numberOfBeamsAlpha(self, bank: list[str]) -> int:
        nbBeams = 0
        # check each row
        for index,row in enumerate(bank):
            # if there are security devices
            # if this row has at least one security shell
            sumRow = sum([int(elem) for elem in row])
            if sumRow > 0: 
                # then check following rows
                for otherRow in bank[index+1:]:
                    # if there is a row with security devices
                    sumOtherRow = sum([int(elem) for elem in otherRow])
                    if sumOtherRow > 0:
                        # count how many beams
                        nbBeams += sumRow * sumOtherRow
                        # end iteration of otherRow
                        break
        return nbBeams
epsi = Solution()
print(epsi.numberOfBeamsBeta(["011001","000000","010100","001000"]))

# performance of ver beta much better than ver alpha