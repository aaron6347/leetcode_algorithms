"""#118_pascal's_triangle.py
    Created by Aaron at 24-Apr-20"""
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # app1
        # ar=[]
        # for x in range(numRows):
        #     ar2=[]
        #     for y in range(x+1):
        #         if y==0 or y==x:
        #             ar2.append(1)
        #         else:
        #             ar2.append(ar[x-1][y-1]+ar[x-1][y])
        #     ar.append(ar2)
        # return ar

        # app2
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]

run=Solution()
a=5
print(run.generate(a))
# app1 imagining ..., 121, 1331, ... prev and current of previous list added up for 1...k-1, dp
# app2 using map insert right 0 and left 0, 13310+01331=14641, dp