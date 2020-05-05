"""#172_factortial_trailing_zeroes.py
    Created by Aaron at 03-May-20"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n // 5
            count += n
        return count

run=Solution()
a=1808548329
print(run.trailingZeroes(a))
# divide number with 5 recursively