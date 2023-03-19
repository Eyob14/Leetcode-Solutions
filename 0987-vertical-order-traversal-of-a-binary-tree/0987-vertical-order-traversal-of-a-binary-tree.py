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
        
        container = defaultdict(list)
        for value in storage:
            container[value[0]].append(value[2])
        ans = []
        
        for value in container.values():
            ans.append(value)
        
        return ans