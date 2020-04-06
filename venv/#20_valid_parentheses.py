"""#20_valid_parentheses.py
    Created by Aaron at 01-Apr-20"""
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": 1, ")": 2, "{": 11, "}": 12, "[": 21, "]": 22}
        if s == "":
            return True
        elif len(s) % 2 != 0:
            return False
        st = [dic[s[0]]]
        for x in range(1, len(s)):
            if len(st) == 0:
                st.insert(0, dic[s[x]])
            elif dic[s[x]] == st[0] + 1:
                del st[0]
            else:
                st.insert(0, dic[s[x]])
        if not st:
            return True
        else:
            return False

run=Solution()
a="()[]{}"
print(run.isValid(a))
# use dict to key and value
# possibly can use binary value and XOR to determine