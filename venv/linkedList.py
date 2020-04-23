"""linkedList.py
    Created by Aaron at 22-Apr-20"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a=[1,2,4]
tail=head = ListNode(a[0])
for x in a[1:]:
    tail.next = ListNode(x)
    tail=tail.next
s='['
while head:
    s+=str(head.val)+','
    head=head.next
s=s[:len(s)-1]+']'
print(s)