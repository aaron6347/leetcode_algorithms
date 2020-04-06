"""#13_roman_to_integer.py
    Created by Aaron at 31-Mar-20"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return sum([-dic[var] if i < len(s) - 1 and dic[var] < dic[s[i + 1]] else dic[var] for i, var in enumerate(s)])

run=Solution()
a="MCMXCIV"
print(run.romanToInt(a))
# few special cases need to be focus, can make use of dict when it is key and value