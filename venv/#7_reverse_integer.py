"""#7_reverse_integer.py
    Created by Aaron at 30-Mar-20"""
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=0-int(str(-x)[::-1])
            if x<= -2147483648:
                return 0
            else:
                return x
        else:
            x= int(str(x)[::-1])
            if x>=2147483648:
                return 0
            else:
                return x

run=Solution()
a=-321
print(run.reverse(a))
# sensitive test case, negative number need to be in negative but number reversed