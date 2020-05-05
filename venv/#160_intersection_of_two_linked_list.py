"""#160_intersection_of_two_linked_list.py
    Created by Aaron at 02-May-20"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # app1
        # if headA is None or headB is None:
        #     return None
        # dic={}
        # while headA:
        #     dic[headA]=headA.val
        #     headA=headA.next
        # while headB:
        #     if headB in dic:
        #         return headB
        #     headB=headB.next
        # return None

        # app2
        if headA is None or headB is None:
            return None
        a, b = headA, headB
        count = 0
        while count < 3:
            if a is None:
                a = headB
                count += 1
            if b is None:
                b = headA
                count += 1
            if a == b:
                return a
            else:
                a = a.next
                b = b.next
        return None

run=Solution()
_,b,c,d,e=8,[4,1,8,4,5],[5,0,1,8,4,5],2,3
nodeA=headA=ListNode(b[0])
nodeB=headB=ListNode(c[0])
for x in range(1,d):
    nodeA.next=ListNode(b[x])
    nodeA=nodeA.next
for x in range(1,e):
    nodeB.next=ListNode(c[x])
    nodeB=nodeB.next
nodeC=headC=ListNode(b[d])
for x in range(d+1, len(b)):
    nodeC.next=ListNode(b[x])
    nodeC=nodeC.next
nodeA.next=headC
nodeB.next=headC
print(run.getIntersectionNode(headA, headB).val)
# app1 every node of first linked list added into dictionary, traverse second linked list and check visited, time O(m+n) space O(n) or O(m)
# app2 using two pointer, iterate each linked list, any pointer has reach the end, proceed with the other,
# each time check same node or not, time O(m+n) space O(1)