"""#38_count_and_say.py
    Created by Aaron at 04-Apr-20"""
class Solution:
    def countAndSay(self, n: int) -> str:
        # ar=[1]
        # run = 1
        # while run<n:
        #     ar2=[]
        #     for x in range(len(ar)):
        #         if x==0:
        #             count=1
        #         else:
        #             if ar[x]== ar[x-1]:
        #                 count+=1
        #             if ar[x]!=ar[x-1]:
        #                 ar2.append(count)
        #                 ar2.append(ar[x-1])
        #                 count=1
        #         if x+1==len(ar):
        #             ar2.append(count)
        #             ar2.append(ar[x])
        #     ar=ar2
        #     run+=1
        # s=''
        # for x in ar:
        #     s+=str(x)
        # return s
        s='1'
        for _ in range(n-1):
            tc, count, st = s[0], 0, ''
            for x in s:
                if x == tc:
                    count+=1
                else:
                    st+=str(count)+tc
                    count=1
                    tc=x
            st+=str(count)+tc
            s=st
        return s

run=Solution()
a=6
print(run.countAndSay(a))
# solve counting of num in str, check with next, assign new str, repeat