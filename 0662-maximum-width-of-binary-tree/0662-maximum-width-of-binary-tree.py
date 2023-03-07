# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root,0)])
        ans = 1
        last_node = root
        while queue:
            node, index = queue.popleft()
            if node.left:
                queue.append((node.left, index*2))
            if node.right:
                queue.append((node.right, index*2+1))
            if node == last_node:
                if len(queue)>0:
                    last_node = queue[-1][0]
                    ans = max(ans, queue[-1][1]-queue[0][1]+1)
        return ans
