"""#104_maximum_depth_of_binary_tree.py
    Created by Aaron at 09-Apr-20"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def insert(self, root, n, middle, times):
        if times>0:
            if n<=middle:
                self.left.insert(root, n, middle-2, times-1)
            else:
                self.right.insert(root, n, middle+2, times-1)
        else:
            if n%2==1:
                self.left=TreeNode(root)
            elif n%2==0:
                self.right=TreeNode(root)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1 if root else 0

run = Solution()
# a = [1, 2, 2, 3, 4, 4, 3]
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
head=node = TreeNode(a[0])
bi=[2,4,8,16,32,64]
for x in range(1, len(a)):
    sum=0
    for y in range(len(bi)):
        sum+=bi[y]
        if x<=sum:
            node.insert(a[x], x, sum-bi[y]+(bi[y]/2), y)
            break
print(run.maxDepth(node))
# comparing depth of left or right of each root