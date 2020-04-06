"""#14_longest_common_prefix.py
    Created by Aaron at 01-Apr-20"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        st = strs[0]
        for x in range(1, len(strs)):
            count = 0
            for y, z in zip(st, strs[x]):
                if y != z:
                    break
                count += 1
            st = st[:count]
        return st

run=Solution()
a=["flower","flow","flight"]
print(run.longestCommonPrefix(a))
# select first element and compare