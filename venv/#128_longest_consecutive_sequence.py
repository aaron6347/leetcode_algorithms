"""#128_longest_consecutive_sequence.py
    Created by Aaron at 20-Apr-20"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(x for x in nums)
        mx = 0
        for x in st:
            cur = x
            l = 1
            if not st.__contains__(cur-1):
                while st.__contains__(cur+1):
                    cur+=1
                    l+=1
                mx= max(l, mx)
        return mx

run=Solution()
a=[100,4,200,1,3,2]
a=[0,0,-1]
print(run.longestConsecutive(a))
# using set to have O(1) and use contain, if condition to find the smallest of the range while condition to find between and last