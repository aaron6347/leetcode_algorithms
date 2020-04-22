"""#125_valid_palindrome.py
    Created by Aaron at 22-Apr-20"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # app1
        # start=0
        # end=len(s)-1
        # while start<=end:
        #     if not s[start].isalpha() and not s[start].isdigit():
        #         start += 1
        #         continue
        #     if not s[end].isalpha() and not s[end].isdigit():
        #         end -= 1
        #         continue
        #     if s[start].isalpha() and s[end].isalpha() and s[start].lower()==s[end].lower():
        #         start+=1
        #         end-=1
        #     elif s[start].isdigit() and s[end].isdigit() and s[start]==s[end]:
        #         start+=1
        #         end-=1
        #     else:
        #         return False
        # return True

        # app2
        # a=[x.lower() for x in s if x.isalpha() or x.isdigit()]
        # for x in range(int(len(a)//2)):
        #     if a[x]!=a[len(a)-1-x]:
        #         return False
        # return True

        # app3
        # start=0
        # end=len(s)-1
        # while start<end:
        #     while start<end and not s[start].isalnum():
        #         start+=1
        #     while start<end and not s[end].isalnum():
        #         end-=1
        #     if s[start].lower() != s[end].lower():
        #         return False
        #     start += 1
        #     end -= 1
        # return True

        # app4
        s=''.join(x for x in s if x.isalnum()).lower()
        return s==s[::-1]

run=Solution()
a='A man, a plan, a canal: Panama'
print(run.isPalindrome(a))
# app1 without modfying use pointer to check
# app2 modfy and check
# app3 similar to app1 but looping while the pointer is not alphanumeric
# app4 using join to skip all non alphanumeric and check with reverse