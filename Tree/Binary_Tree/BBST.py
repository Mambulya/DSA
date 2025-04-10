"""
Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).

Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
 You need to return the root node of the Binary Tree.

input:
 A : [1, 2, 3, 5, 10]
 output:
       3
    /   \
   2     5
  /       \
 1         10

 """

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if len(A) == None:
            return None

        root = Solution.create_node(A, 0, len(A) - 1)

        return root

    @staticmethod
    def create_node(A, indx_low, indx_high):
        if indx_low > indx_high:
            return None
        indx_mid = (indx_low + indx_high) // 2
        node = TreeNode(A[indx_mid])
        node.left = Solution.create_node(A, indx_low, indx_mid - 1)
        node.right = Solution.create_node(A, indx_mid + 1, indx_high)

        return node

  A = [1, 2, 3, 5, 10]
s = Solution()
root = s.sortedArrayToBST(A)
print("---------------")
print(root.val)
