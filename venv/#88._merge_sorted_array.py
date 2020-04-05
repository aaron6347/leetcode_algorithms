from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for x in nums2:
        #     nums1[m]=x
        #     m+=1
        # nums1.sort()

        # nums1[m:]=nums2[:n]
        # nums1.sort()

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
# many ways to solve, make use of assignment then sorting or arrange with comparison