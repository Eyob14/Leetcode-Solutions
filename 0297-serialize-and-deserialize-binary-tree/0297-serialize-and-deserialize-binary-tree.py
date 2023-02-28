# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        ans = []
        def dfs(node):
            if not node:
                ans.append("#")
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(ans)


    def deserialize(self, data):
        if not data: return None
        lst = data.split(",")
        self.index = 0
        def helper():
            if lst[self.index] == '#':
                self.index += 1
                return None
            root = TreeNode(int(lst[self.index]))
            self.index += 1
            root.left = helper()
            root.right = helper()

            return root
        return helper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))