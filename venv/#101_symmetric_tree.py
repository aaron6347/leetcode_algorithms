"""#101_symmetric_tree.py
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
    # app2
    def isMirror(self, root, root2):
        if root is None and root2 is None:
            return True
        elif root is None or root2 is None:
            return False
        else:
            return root.val==root2.val and self.isMirror(root.left, root2.right) and self.isMirror(root.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        # app1
        # if root is None:
        #     return True
        # stack=[[root.left, root.right]]
        # while len(stack)>0:
        #     match=stack.pop()
        #     left,right=match[0], match[1]
        #     if left is None and right is None:
        #         continue
        #     if left is None or right is None:
        #         return False
        #     if left.val!= right.val:
        #         return False
        #     else:
        #         stack.append([left.left, right.right])
        #         stack.append([left.right, right.left])
        # return True

        # app2
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

run = Solution()
a= [1, 2, 2, 3, 4, 4, 3]
node=TreeNode(a[0])
for x in range(1,len(a)):
    node.insert(a[x])
print(run.isSymmetric(node))
# sensitive test cases: empty, no node, not same value or same value
# app1 iterative with stack
# app2 recursive but only applicable to height 3