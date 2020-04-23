"""binaryTree.py
    Created by Aaron at 22-Apr-20"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # insert by 1,2,4,8,16,32,64
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

    # print
    def printLevelOrder(self, root):
        h = self.height(root)
        ar=[]
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

# a = [1, 2, 2, 3, 4, 4, 3] # insert by 1,2,4,8,16,32,64
# node = TreeNode(a[0])
# bi=[2,4,8,16,32,64]   # symmetry binary tree
# for x in range(1, len(a)):
#     sum=0
#     for y in range(len(bi)):
#         sum+=bi[y]
#         if x<=sum:
#             node.insert(a[x], x, sum-bi[y]+(bi[y]/2), y)
#             break
# node.printLevelOrder(node)

a=[5,4,8,11,None,13,4,7,2,None,None,None,1] # insert by 1,2,4,8,16,32 with filling None
# [5,4,8,11,None,13,4,7,2,None,None, None, None, None, 1]
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
node.printLevelOrder(node)