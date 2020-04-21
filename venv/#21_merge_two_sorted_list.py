"""#21_merge_two_sorted_list.py
    Created by Aaron at 02-Apr-20"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new = ListNode(0)
        head=new
        while l1 and l2:
            if l1.val <= l2.val:
                new.next=l1
                l1=l1.next
            else:
                new.next=l2
                l2=l2.next
            new= new.next
        if l1:
            new.next=l1
        else:
            new.next=l2
        return head.next

run=Solution()
a,b=[1,2,4],[1,3,4]
tail=head = ListNode(a[0])
tail2=head2 = ListNode(b[0])
# single list node
for x in a[1:]:
    tail.next = ListNode(x)
    tail=tail.next
for x in b[1:]:
    tail2.next = ListNode(x)
    tail2=tail2.next
run.mergeTwoLists(head,head2)
# output thingy
s='['
while head:
    s+=str(head.val)+','
    head=head.next
s=s[:len(s)-1]+']'
print(s)
# linked list connect new node