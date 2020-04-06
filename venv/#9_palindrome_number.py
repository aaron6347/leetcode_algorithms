"""#9_palindrome_number.py
    Created by Aaron at 31-Mar-20"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

run=Solution()
a=-121
print(run.isPalindrome(a))
# sensitive test case, negative need to be ignored