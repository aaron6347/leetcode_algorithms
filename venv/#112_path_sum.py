"""#112_path_sum.py
    Created by Aaron at 22-Apr-20"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class Solution:
    # app1
    # def dfs(self, root, sum, cur):
    #     if root.val is not None:
    #         cur+=root.val
    #     if root.left is not None:
    #         self.dfs(root.left, sum, cur)
    #     if root.right is not None:
    #         self.dfs(root.right, sum, cur)
    #     if root.left is None and root.right is None:
    #         self.ar.append(cur)
    #
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     if root is None:
    #         return False
    #     self.ar=[]
    #     self.dfs(root, sum, 0)
    #     if sum in self.ar:
    #         return True
    #     return False

    # app2
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    # app3
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     if not root:
    #         return False
    #     stack = [(root, root.val)]
    #     while stack:
    #         curr, val = stack.pop()
    #         if not curr.left and not curr.right:
    #             if val == sum:
    #                 return True
    #         if curr.right:
    #             stack.append((curr.right, val + curr.right.val))
    #         if curr.left:
    #             stack.append((curr.left, val + curr.left.val))
    #     return False

    # app4
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     if not root:
    #         return False
    #     queue = [(root, sum - root.val)]
    #     while queue:
    #         curr, val = queue.pop(0)
    #         if not curr.left and not curr.right:
    #             if val == 0:
    #                 return True
    #         if curr.left:
    #             queue.append((curr.left, val - curr.left.val))
    #         if curr.right:
    #             queue.append((curr.right, val - curr.right.val))
    #     return False

run=Solution()
a,b=[5,4,8,11,None,13,4,7,2,None,None,None,1],22
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
print(run.hasPathSum(node, b))
# app1 dfs with recursively summing root. value and finally inserting into list to determine
# app2 dfs with recursively minus the sum
# app3 dfs with stack
# app4 bfs with queue