"""#26_remove_duplicates_from_sorted_array.py
    Created by Aaron at 02-Apr-20"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=1
        while x<len(nums):
            if nums[x]==nums[x-1]:
                del nums[x]
                continue
            x+=1
        return len(nums)

run=Solution()
a=[0,0,1,1,1,2,2,3,3,4]
print(run.removeDuplicates(a))
# commparison and remove