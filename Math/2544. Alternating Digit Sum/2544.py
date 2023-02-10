import numpy as np
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # try to solve it in a matlab style
        # the performance (runtime, memory) is not optimized though...

        # mapping vector
        tmp = []
        for i in range(len(str(n))):
            tmp.append((-1)**i)
        mapping = np.array(tmp)
        print(mapping)
        # input vector
        tmp = []
        for digit in [*str(n)]:
            tmp.append(int(digit))
        invect = np.array(tmp)
        # scalar product and sum up
        return np.dot(invect, mapping).sum()
epsi = Solution()
print(epsi.alternateDigitSum(111))