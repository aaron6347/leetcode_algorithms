"""#35_search_insert_position.py
    Created by Aaron at 03-Apr-20"""
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x < target])

run=Solution()
a,b=[1,3,5,6],5
print(run.searchInsert(a,b))
# comparison and sometimes can make use of new list