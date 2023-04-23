# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
         - path - contain elements
         - we check and add the path if leaf node
         - backtracking
         - Time: O(n)
         - Space: O(n)
        """
        
        answer = []
        
        def dfs(cur_node, cur_sum, path):
            #base case
            if not cur_node:
                return
            if not cur_node.left and not cur_node.right:
                if cur_sum + cur_node.val == targetSum:
                    path.append(cur_node.val)
                    answer.append(path[:])
                    path.pop()
                return
            
            path.append(cur_node.val)
            cur_sum += cur_node.val
            dfs(cur_node.left, cur_sum, path)
            dfs(cur_node.right, cur_sum, path)
            path.pop()
        
        dfs(root, 0, [])
        
        return answer
        
        
        