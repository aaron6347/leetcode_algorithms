from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # string=''
        # for x in digits:
        #     string+=str(x)
        # string=str(int(string)+1)
        # ar=[]
        # for x in string:
        #     ar.append(x)
        # return ar

        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)

run=Solution()
a=[1,2,3]
# a=[9,9,9,9]
print(run.plusOne(a))
# sensitive test case