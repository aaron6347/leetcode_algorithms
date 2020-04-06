"""#88_merge_sorted_array.py
    Created by Aaron at 06-Apr-20"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # app1
        # for x in nums2:
        #     nums1[m]=x
        #     m+=1
        # nums1.sort()

        # app2
        # nums1[m:]=nums2[:n]
        # nums1.sort()

        # app3
        while n > 0:
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        print(nums1)

run=Solution()
a,b,c,d=[1,2,3,0,0,0],3,[2,5,6],3
run.merge(a,b,c,d)
# app1 add all into 1st list, sort
# app2 split and join, sort
# app3 compare then insert, make good use of pointer vs pointer