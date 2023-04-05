class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_traversal = []
        if not root:
            return []
        queue = deque([root])

        while queue:
            cur_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    cur_level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            level_order_traversal.append(cur_level)
            
        return level_order_traversal