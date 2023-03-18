# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def preOrder(node, direction):
            nonlocal ans
            if node:
                if not node.left and not node.right and direction=="left":
                    ans += node.val
                preOrder(node.left, "left")
                preOrder(node.right, "right")
        
        preOrder(root, "")
        return ans
        