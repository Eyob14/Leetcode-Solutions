# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def traversal(node = root, x_cor=0, y_cor=0):
            if not node:
                return
            storage.append((x_cor, y_cor, node.val))
            if node.left: traversal(node.left, x_cor-1, y_cor+1)
            if node.right: traversal(node.right, x_cor+1, y_cor+1)
                
        
        storage = []
        traversal() # calling the function
        storage.sort()
        
        ans = [[]]
        last = storage[0][0]
        
        for value in storage:
            if last == value[0]:
                ans[-1].append(value[2])
            else:
                ans.append([value[2]])
                last = value[0]            
        
        return ans
        
        
        