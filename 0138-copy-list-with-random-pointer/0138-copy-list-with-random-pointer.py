"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {}
        
        def builder(head):
            if not head:
                return
            if head in visited:
                return visited[head]
            node = Node(head.val, None, None)
            
            visited[head] = node
            
            node.next = builder(head.next)
            node.random = builder(head.random)
            
            return node
        
        res = builder(head)
        return res
        
        