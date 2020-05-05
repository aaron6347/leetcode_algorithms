"""#189_rotate_array.py
    Created by Aaron at 04-May-20"""
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # app1
        # n=len(nums)
        # ar=[0]*n
        # for x in range(n):
        # ar[(x+k)%n]=nums[x]
        # nums[:]=ar

        # app2
        # def rev(nums, start, end):
        #     while start < end:
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start += 1
        #         end -= 1
        # n = len(nums)
        # k %= n
        # rev(nums, 0, n - 1)
        # rev(nums, 0, k - 1)
        # rev(nums, k, n - 1)

        # app3
        n = len(nums)
        k %= n
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if start == current:
                    break
            start += 1

run=Solution()
a,b=[1,2,3,4,5,6,7],3
run.rotate(a, b)
print(a)
# app1 store the element in another list, time O(n) space O(n)
# app2 reverse entire list then reverse both sublist, time O(n) space O(1)
# app3 jump k of element, temp to store new and place prev then current as new, repeat until all done, time O(n) space O(1)