"""#83_remove_duplicates_from_sorted_list.py
    Created by Aaron at 06-Apr-20"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current, nex= head, head.next if head else None
        while nex:
            if current.val== nex.val:
                nex=nex.next
                current.next=nex
            else:
                current=nex
                nex=nex.next
        return head

run=Solution()
a=[1,1,2,3]
tail=head = ListNode(a[0])
for x in a[1:]:
    tail.next = ListNode(x)
    tail=tail.next
run.deleteDuplicates(head)
s='['
while head:
    s+=str(head.val)+','
    head=head.next
s=s[:len(s)-1]+']'
print(s)
# linked list skipping node