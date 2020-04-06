"""#1_two_sum.py
    Created by Aaron at 30-Mar-20"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

run=Solution()
a=[2,7,11,15]
b=9
print(run.twoSum(a,b))
# make use of dict since answer can be a pair