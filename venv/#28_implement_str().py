"""#28_implement_str().py
    Created by Aaron at 03-Apr-20"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x= len(haystack)
        y=len(needle)
        for i in range(x+1):
            if haystack[i:i+y]== needle:
                return i
            elif y+i > x:
                return -1

run=Solution()
a,b="hello","ll"
print(run.strStr(a,b))
# spliting in list
