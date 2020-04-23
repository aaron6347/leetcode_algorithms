"""#119_pascal's_triangle_2.py
    Created by Aaron at 24-Apr-20"""
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # app1
        # ar=[1]
        # x=0
        # while x<rowIndex:
        #     ar=[1 if y==0 else ar[y]+ar[y-1] for y in range(len(ar)) ]
        #     ar.append(1)
        #     x+=1
        # return ar

        # app2
        res = [1]
        for _ in range(1, rowIndex):
            res = list(map(lambda x, y: x + y, res + [0], [0] + res))
        return res

run=Solution()
a=33
print(run.getRow(a))
# app1 imagining ..., 121, 1331, ... prev and current of previous list added up for 1...k-1, dp
# app2 using map insert right 0 and left 0, 13310+01331=14641, dp
