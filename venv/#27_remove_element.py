"""#27_remove_element.py
    Created by Aaron at 03-Apr-20"""
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for _, value in enumerate(nums):
            if value == val:
                pass
            else:
                nums[count] = value
                count += 1
        return count

run=Solution()
a,b=[0,1,2,2,3,0,4,2],2
print(run.removeElement(a,b))
# make use of enum in comparing value and has the index for other operation