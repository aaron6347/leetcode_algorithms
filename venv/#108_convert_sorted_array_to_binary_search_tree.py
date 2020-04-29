"""#108_convert_sorted_array_to_binary_search_tree.py
    Created by Aaron at 29-Apr-20"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    # def putleft(self, root, nums):
    #     l = len(nums)
    #     if l == 1:
    #         root.left = TreeNode(nums[0])
    #     else:
    #         middle = l // 2
    #         root.left = TreeNode(nums[middle])
    #         lnums = nums[:middle]
    #         rnums = nums[middle + 1:]
    #         if len(lnums) > 0:
    #             self.putleft(root.left, lnums)
    #         if len(rnums) > 0:
    #             self.putright(root.left, rnums)
    # def putright(self, root, nums):
    #     l = len(nums)
    #     if l == 1:
    #         root.right = TreeNode(nums[0])
    #     else:
    #         middle = l // 2
    #         root.right = TreeNode(nums[middle])
    #         lnums = nums[:middle]
    #         rnums = nums[middle + 1:]
    #         if len(lnums) > 0:
    #             self.putleft(root.right, lnums)
    #         if len(rnums) > 0:
    #             self.putright(root.right, rnums)
    #
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     l = len(nums)
    #     if l == 1:
    #         return TreeNode(nums[0])
    #     elif l == 0:
    #         return
    #     middle = l // 2
    #     root = TreeNode(nums[middle])
    #     lnums = nums[:middle]
    #     rnums = nums[middle + 1:]
    #     if len(lnums) > 0:
    #         self.putleft(root, lnums)
    #     if len(rnums) > 0:
    #         self.putright(root, rnums)
    #     return root

    # app2
    # def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    #     def convert(left, right):
    #         if left > right:
    #             return None
    #         mid = (left + right) // 2
    #         node = TreeNode(nums[mid])
    #         node.left = convert(left, mid - 1)
    #         node.right = convert(mid + 1, right)
    #         return node
    #     return convert(0, len(nums) - 1)

    # app3
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not num:
            return None
        median = len(num) // 2
        new_node = TreeNode(num[median])
        new_node.left = self.sortedArrayToBST(num[:median])
        new_node.right = self.sortedArrayToBST(num[median + 1:])
        return new_node

run=Solution()
a=[-10,-3,0,5,9]
ans=run.sortedArrayToBST(a)
ans.printLevelOrder(ans)
# app1 search middle of list and put it as one left/right and slice list into sublist recursively, time O(n)
# app2 search middle of list and put boundary of sublist instead of slciing which cost more time in large case, time O(n)
# app3 similar with app2 but with own function recursively only
