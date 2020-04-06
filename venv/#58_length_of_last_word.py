"""#58_length_of_last_word.py
    Created by Aaron at 04-Apr-20"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # ar=list(map(str, s.split(' ')))
        # for x in range(len(ar)-1, -1, -1):
        #     if ar[x]!='':
        #         return len(ar[x])
        #     elif x==0:
        #         return 0
        return len(s.split()[-1]) if len(s.split())!= 0 else 0


run=Solution()
a="Hello World"
# a="hello "
# a=""
print(run.lengthOfLastWord(a))
# split() and sensitive test cases