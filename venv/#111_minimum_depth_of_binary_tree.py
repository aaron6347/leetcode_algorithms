"""#111_minimum_depth_of_binary_tree.py
    Created by Aaron at 24-Apr-20"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    # def dfs(self, root, height):
    #     if root.left is None and root.right is None:
    #         return height
    #     elif root.left and root.right:
    #         return min(self.dfs(root.left, height + 1), self.dfs(root.right, height + 1))
    #     elif root.left:
    #         return self.dfs(root.left, height + 1)
    #     elif root.right:
    #         return self.dfs(root.right, height + 1)
    #
    # def minDepth(self, root: TreeNode) -> int:
    #     if root is None:
    #         return 0
    #     return self.dfs(root, 1)

    # app2
    # def minDepth(self, root: TreeNode) -> int:
    #     if root == None:
    #         return 0
    #     if root.left == None or root.right == None:
    #         return self.minDepth(root.left) + self.minDepth(root.right) + 1
    #     return min(self.minDepth(root.right), self.minDepth(root.left)) + 1

    # app3
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     if None in [root.left, root.right]:
    #         return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    #     else:
    #         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # app4
    # def minDepth(self, root: TreeNode) -> int:
        # if not root: return 0
        # d = list(map(self.minDepth, (root.left, root.right)))
        # return 1 + (min(d) or max(d))

    # app5
    def minDepth(self, root: TreeNode) -> int:
        l, i = [root], 1
        while l and root and all(n.left or n.right for n in l):
            l, i = [kid for n in l for kid in [n.left, n.right] if kid], i + 1
        return i if root else 0

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
print(run.minDepth(node))
# app1 dfs
# app2 dfs with better implement in if left or right is None, return by continue will become 0 and another is more than 0,
# if both left and right are None, both will continue and eventually 0
# app3 dfs same concept as app2 but using min and max at root return and every nodes except root return respectively
# app4 dfs with min max similar to app3 but also with map
# app5 bfs