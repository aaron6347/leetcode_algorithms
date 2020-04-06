"""#70_climbing_stairs.py
    Created by Aaron at 05-Apr-20"""
class Solution:
    # app1
    def climbStairs(self, n: int) -> int:
        ar=[1,1]
        for x in range(2,n+1):
            ar.append(ar[x-1]+ar[x-2])
        return ar[n]


run=Solution()
a=5
print(run.climbStairs(a))
# app1 fibonacci, use dp O(n) in iterative or recursive
# app2 use matrix exponentiation O(log n)