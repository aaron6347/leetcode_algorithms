"""#141_linked_list_cycle.py
    Created by Aaron at 24-Apr-20"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # app1
        # s = set()
        # if head is None:
        #     return False
        # while head:
        #     if head not in s:
        #         s.add(head)
        #     else:
        #         return True
        #     head = head.next
        # return False

        # app2
        if head is None:
            return False
        fast=head.next
        while fast!=head:
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            head=head.next
        return True

run=Solution()
a,b=[3,2,0,-4],1
c=0
head=root=ListNode(a[0])
for x in range(1,len(a)):
    if x==b+1:
        c=root
    root.next=ListNode(a[x])
    root=root.next
root.next=c
print(run.hasCycle(head))
# app1 using set to store all hash and if exist in hash means visited O(n) space
# app2 using slow and fast pointer to find same position means having cycle O(1) space