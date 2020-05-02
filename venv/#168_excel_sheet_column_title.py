"""#168_excel_sheet_column_title.py
    Created by Aaron at 02-May-20"""
class Solution:
    # app1
    # def convertToTitle(self, n: int) -> str:
    #     import string
    #     dic={ x+1:string.ascii_uppercase[x] for x in range(len(string.ascii_uppercase))}
    #     s=''
    #     while n>26:
    #         left=int(n/26)
    #         right=n-left*26
    #         if right==0:
    #             left-=1
    #             right=26
    #         n=left
    #         s=dic.get(right)+s
    #     return dic.get(n)+s

    # app2
    # def convertToTitle(self, n: int) -> str:
    #     title = []
    #     while n != 0:
    #         n, remainder = divmod(n - 1, 26)
    #         title.append(remainder + ord("A"))
    #     return "".join([chr(i) for i in title[::-1]])

    # app3
    def convertToTitle(self, n: int) -> str:
        def recConvert(n: int) -> str:
            return "" if n < 0 else recConvert(n // 26 - 1) + chr(ord("A") + n % 26)
        return recConvert(n - 1)

run=Solution()
a=703
print(run.convertToTitle(a))
# app1 declare index for alphabet and store in dic, divide the number and match the index
# app2 use ord and chr to generate alphabet, 65 as A
# app3 recursively