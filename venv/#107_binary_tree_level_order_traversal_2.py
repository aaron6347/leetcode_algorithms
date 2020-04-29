"""#107_binary_tree_level_order_traversal_2.py
    Created by Aaron at 29-Apr-20"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # insert by 1,2,4,8,16,32,64
    def insert(self, root, n, middle, times):
        if times > 0:
            if n <= middle:
                self.left.insert(root, n, middle - 2, times - 1)
            else:
                self.right.insert(root, n, middle + 2, times - 1)
        else:
            if n % 2 == 1:
                self.left = TreeNode(root)
            elif n % 2 == 0:
                self.right = TreeNode(root)

    # print
    def printLevelOrder(self, root):
        h = self.height(root)
        ar = []
        for i in range(1, h + 1):
            self.printGivenLevel(root, i, ar)
        print(ar)

    def height(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def printGivenLevel(self, root, level, ar):
        if root is None:
            ar.append(None)
            return
        if level == 1:
            ar.append((root.val))
        elif level > 1:
            self.printGivenLevel(root.left, level - 1, ar)
            self.printGivenLevel(root.right, level - 1, ar)

class Solution:
    # app1
    # def dfs(self, root, ar, level):
    #     if root is None:
    #         return
    #     else:
    #         if len(ar) >= level + 1:
    #             ar[level].append(root.val)
    #         else:
    #             ar.append([root.val])
    #         self.dfs(root.left, ar, level + 1)
    #         self.dfs(root.right, ar, level + 1)
    #
    # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    #     ar = []
    #     self.dfs(root, ar, 0)
    #     return ar[::-1]

    # app2
    # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    #     stack = [(root, 0)]
    #     res = []
    #     while stack:
    #         node, level = stack.pop()
    #         if node:
    #             if len(res) < level + 1:
    #                 res.insert(0, [])
    #             res[-(level + 1)].append(node.val)
    #             stack.append((node.right, level + 1))
    #             stack.append((node.left, level + 1))
    #     return res

    # app3
    # def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    #     queue, res = collections.deque([(root, 0)]), []
    #     while queue:
    #         node, level = queue.popleft()
    #         if node:
    #             if len(res) < level + 1:
    #                 res.insert(0, [])
    #             res[-(level + 1)].append(node.val)
    #             queue.append((node.left, level + 1))
    #             queue.append((node.right, level + 1))
    #     return res

    # app4
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res, nodes = [], [root] if root else []
        while nodes:
            res.append(list(node.val for node in nodes))
            nodes = [x for node in nodes for x in (node.left, node.right) if x]
        return res[::-1]

run=Solution()
a=[3,9,20,None,None,15,7]
copy=a
i=0
while i<len(a):
    if all ( y is None for y in a[i:-1]):
        break
    if a[i]==None:
        copy.insert(i * 2 + 1, None)
        copy.insert(i * 2 + 2, None)
    i+=1
    a=copy
for x in range(len(a)-1, -1,-1):    # cutting the extra None at the end list
    if a[x]!=None:
        i=x
        break
a=a[:i+1]
node = TreeNode(a[0])
bi=[2,4,8,16,32,64] # symmetry binary tree
for x in range(1, len(a)):
    sum=0
    for y in range(len(bi)):
        sum+=bi[y]
        if x<=sum:
            node.insert(a[x], x, sum-bi[y]+(bi[y]/2), y)
            break
# node.printLevelOrder(node)
print(run.levelOrderBottom(node))
# app1 dfs with recursive, using level to detect list need to create or insert time O(n) space O(n)
# app2 dfs with iterative stack with right side and left side, so that pop left then right and using level as well, time O(n^2) space O(n+1)
# app3 dfs with iterative queue with left side and right side, so that pop left then right and using level as well, time O(n^2) space O(n+1)
# app4 bfs with smart iterative time O(n) spaced o(n)