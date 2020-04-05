class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]
        return format((int(a,2)+int(b,2)),'b')


run=Solution()
a = "11"; b = "1"
print(run.addBinary(a,b))
# binary to decimal then to binary