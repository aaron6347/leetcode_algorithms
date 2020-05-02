"""#171_excel_sheet_column_number.py
    Created by Aaron at 02-May-20"""
class Solution:
    # app1
    # def titleToNumber(self, s: str) -> int:
    #     n=0
    #     pos=0
    #     x=len(s)-1
    #     while x>=0:
    #         n+=(ord(s[x])-64)*26**pos
    #         pos+=1
    #         x-=1
    #     return n

    # app2
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for c in s:
            ans = ans * 26 + ord(c) - ord('A') + 1
            print(ans)
        return ans

    # app3
    # def titleToNumber(self, s: str) -> int:
    #     return reduce(lambda x, y: 26 * x + ord(y) - 64, s, 0)

    # app4
    # def titleToNumber(self, s: str) -> int:
    #     return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, s))

run=Solution()
a='AAAZAAA'
print(run.titleToNumber(a))
# app1 scan from behind using ord -64 to get A as 1, the pattern is character index * 26 ** digit
# app2 scan from front, the pattern is what collected *26 more as it goes to the end
# app3 scan from front, using reduce with lambda
# app4 scan from front, using reduce with lambda and map for indexing