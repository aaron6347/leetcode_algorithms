"""#100_same_tree.py
    Created by Aaron at 06-Apr-20"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def insert(self, root):
        if self.left is None:
            self.left = TreeNode(root)
        elif self.right is None:
            self.right = TreeNode(root)
        elif self.left.left is None or self.left.right is None:
            self.left.insert(root)
        elif self.right.left is None or self.right.right is None:
            self.right.insert(root)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

run = Solution()
a, b = [1, 2, 4], [1, 2, 4]
node = TreeNode(a[0])
node2 = TreeNode(b[0])
# short version symmetry binary tree
for x in range(1, len(a)):
    node.insert(a[x])
    node2.insert(b[x])
print(run.isSameTree(node, node2))
# sensitive test cases: empty, no node, unequal len, same value or not same value